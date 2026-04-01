import bpy
import copy
import importlib
import os
from ...operators.general_function import showErrorMessageBox

_ELBOW_AUX_BONES = [
    "MhBone_101",
    "MhBone_102",
    "MhBone_103",
    "MhBone_104",
]


class MHW_OT_OpenBoneDictionaryFolder(bpy.types.Operator):
    bl_label = "open dictionary folder"
    bl_description = "Open the dictionary folder in file explorer"
    bl_idname = "mhw.open_bone_dictionary_folder"

    def execute(self, context):
        presetsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bonenamelist")
        os.startfile(presetsPath)
        return {'FINISHED'}


class MHW_OT_SnapBones(bpy.types.Operator):
    """Snap external armature bones to MHWorld armature positions"""
    bl_idname = "mhw.snap_bones"
    bl_label = "Snap Bones"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
            any(obj.type == "ARMATURE" for obj in context.selected_objects)
            and context.mode == 'OBJECT'
        )

    def execute(self, context):
        enum_value = bpy.context.scene.mbt_toolpanel.MHWorldBoneList
        file_name = os.path.splitext(os.path.basename(enum_value))[0]

        preset_module = importlib.import_module(f".bonenamelist.{file_name}", package=__name__)
        importlib.reload(preset_module)

        snap_bone_list = preset_module.snap_bone_fixed_name_list
        mmd_corrections = getattr(preset_module, 'snap_mmd_corrections', False)

        if not snap_bone_list:
            self.report({'WARNING'}, "This preset has no snap bones defined (use the dedicated button instead)")
            return {'CANCELLED'}

        # Save original MHWorld bone names before join
        original_bones = [b.name for b in context.active_object.data.bones]

        # Join the selected armatures
        bpy.ops.object.join()

        armature = context.active_object.data
        armature_name = armature.name
        all_bone_names = [b.name for b in armature.bones]

        bpy.ops.object.mode_set(mode='EDIT')
        edit_bones = bpy.data.armatures[armature_name].edit_bones

        for src_name, dst_name in snap_bone_list:
            if src_name not in edit_bones or dst_name not in edit_bones:
                continue

            # MMD correction: record left elbow position before snap
            before_head = None
            before_tail = None
            if mmd_corrections and dst_name == "MhBone_007":
                before_head = copy.deepcopy(edit_bones["MhBone_007"].head)
                before_tail = copy.deepcopy(edit_bones["MhBone_007"].tail)

            # Snap dst bone to src bone position
            edit_bones.active = edit_bones[src_name]
            context.object.data.use_mirror_x = False
            bpy.ops.armature.select_all(action='DESELECT')
            edit_bones[src_name].select = True
            edit_bones[dst_name].select = True

            original_area = context.area.type
            context.area.type = 'VIEW_3D'
            bpy.ops.view3d.snap_selected_to_active()
            context.area.type = original_area

            # MMD correction: fix toe Y axis
            if mmd_corrections and dst_name in ("MhBone_017", "MhBone_021"):
                edit_bones.active = edit_bones[dst_name]
                context.active_bone.head[1] = -104.611
                context.active_bone.tail[1] = -104.607

            # MMD correction: move elbow aux bones with left elbow
            if mmd_corrections and dst_name == "MhBone_007" and before_head is not None:
                after_head = edit_bones["MhBone_007"].head
                after_tail = edit_bones["MhBone_007"].tail
                head_offset = after_head - before_head
                tail_offset = after_tail - before_tail

                for aux_bone in _ELBOW_AUX_BONES:
                    if aux_bone in edit_bones:
                        edit_bones[aux_bone].head += head_offset
                        edit_bones[aux_bone].tail += tail_offset

            bpy.ops.armature.select_all(action='DESELECT')

        # Show all bone layers/collections
        if hasattr(context.object.data, 'layers'):
            for i in range(32):
                context.object.data.layers[i] = True
        else:
            for coll in armature.collections:
                coll.is_visible = True

        # Delete non-original (external) bones
        for bone_name in all_bone_names:
            if bone_name not in original_bones:
                if bone_name in edit_bones:
                    edit_bones.active = edit_bones[bone_name]
                    bpy.ops.armature.delete()

        bpy.ops.object.mode_set(mode='OBJECT')
        self.report({'INFO'}, "Bone snap completed")
        return {'FINISHED'}


classes = [MHW_OT_OpenBoneDictionaryFolder, MHW_OT_SnapBones]
