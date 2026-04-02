import bpy
import importlib
import os


class MHW_OT_RenameVG(bpy.types.Operator):
    """Rename vertex groups of selected meshes to MHWorld format"""
    bl_idname = "mhw.rename_vg"
    bl_label = "Rename Vertex Groups"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            for obj in context.selected_objects:
                if obj.type != "MESH":
                    return False
            return True
        return False

    def execute(self, context):
        enum_value = bpy.context.scene.mbt_toolpanel.MHWorldBoneList
        file_name = os.path.splitext(os.path.basename(enum_value))[0]

        preset_module = importlib.import_module(f".bonenamelist.{file_name}", package=__package__)
        importlib.reload(preset_module)

        rename_list = preset_module.rename_vg_fixed_name_list

        count = 0
        for obj in context.selected_objects:
            if obj.type == "MESH":
                vgroups = obj.vertex_groups
                for old_name, new_name in rename_list:
                    if old_name in vgroups:
                        vgroups[old_name].name = new_name
                count += 1

        self.report({'INFO'}, f"Converted {count} mesh(es)")
        return {'FINISHED'}


classes = [MHW_OT_RenameVG]
