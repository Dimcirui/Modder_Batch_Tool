import bpy
import pathlib

_mesh_dir = pathlib.Path(__file__).parent / "mesh"
_f_mesh_file = str(_mesh_dir / "f_mesh.mod3")
_m_mesh_file = str(_mesh_dir / "m_mesh.mod3")


def _check_mod3_importer():
    """检查 MHW MOD3 导入器是否可用"""
    return hasattr(bpy.ops.mhw_mod3, 'import_mhw_mod3')


class MHW_OT_ImportFemaleMesh(bpy.types.Operator):
    """Import MHWorld Female Armature"""
    bl_idname = "mhw.import_female_mesh"
    bl_label = "Female Armature"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _check_mod3_importer()

    def execute(self, context):
        if not _check_mod3_importer():
            self.report({'ERROR'}, "MHW Model Editor not installed!")
            return {'CANCELLED'}
        
        bpy.ops.mhw_mod3.import_mhw_mod3(filepath=_f_mesh_file)
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


class MHW_OT_ImportMaleMesh(bpy.types.Operator):
    """Import MHWorld Male Armature"""
    bl_idname = "mhw.import_male_mesh"
    bl_label = "Male Armature"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _check_mod3_importer()

    def execute(self, context):
        if not _check_mod3_importer():
            self.report({'ERROR'}, "MHW Model Editor not installed!")
            return {'CANCELLED'}
        
        bpy.ops.mhw_mod3.import_mhw_mod3(filepath=_m_mesh_file)
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


classes = [
    MHW_OT_ImportFemaleMesh,
    MHW_OT_ImportMaleMesh,
]