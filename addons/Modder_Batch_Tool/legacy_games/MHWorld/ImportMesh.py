import bpy
import pathlib

# 使用 pathlib 更简洁
_mesh_dir = pathlib.Path(__file__).parent / "mesh"
_f_mesh_file = str(_mesh_dir / "f_mesh.mod3")
_m_mesh_file = str(_mesh_dir / "m_mesh.mod3")


class MHW_OT_ImportFemaleMesh(bpy.types.Operator):
    """Import MHWorld Female Armature"""
    bl_idname = "mhw.import_female_mesh"
    bl_label = "Female Armature"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.custom_import.import_mhw_mod3(filepath=_f_mesh_file)
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


class MHW_OT_ImportMaleMesh(bpy.types.Operator):
    """Import MHWorld Male Armature"""
    bl_idname = "mhw.import_male_mesh"
    bl_label = "Male Armature"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.custom_import.import_mhw_mod3(filepath=_m_mesh_file)
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


# 导出类列表
classes = [
    MHW_OT_ImportFemaleMesh,
    MHW_OT_ImportMaleMesh,
]