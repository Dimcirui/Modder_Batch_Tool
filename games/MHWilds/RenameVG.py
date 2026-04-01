import bpy
import importlib
import os


class MHWildsrenamevg(bpy.types.Operator):
    bl_idname = "mbt.mhwilds_rename_vg"
    bl_label = "rename vertex group"
    bl_description = "Change the vertex group name of the external model to the corresponding game model vertex group name"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        enumValue = bpy.context.scene.mbt_toolpanel.MHWildsBoneList
        file_name, file_extension = os.path.splitext(os.path.basename(enumValue))

        preset_module = importlib.import_module(f".bonenamelist.{file_name}", package=__name__)

        if "preset_module" in locals():
            importlib.reload(preset_module)

        fixed_name_list = preset_module.rename_vg_fixed_name_list

        for obj in bpy.context.selected_objects:
            v_groups = obj.vertex_groups

            if fixed_name_list[0][0] in v_groups:
                for n in fixed_name_list:
                    if n[0] in v_groups:
                        v_groups[n[0]].name = n[1]
            else:
                for n in fixed_name_list:
                    if n[0] in v_groups:
                        v_groups[n[0]].name = n[1]

        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}


classes = [MHWildsrenamevg]
