import bpy
import pathlib

_mesh_dir = pathlib.Path(__file__).parent / "mesh"
_f_mesh_file = str(_mesh_dir / "f_shadow_mesh.fbx")
_m_mesh_file = str(_mesh_dir / "m_shadow_mesh.fbx")


class MHR_OT_ImportFemaleMesh(bpy.types.Operator):
    """Import MHRise Female Shadow Mesh"""
    bl_idname = "mhr.import_female_mesh"
    bl_label = "Female Shadow Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=_f_mesh_file)
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


class MHR_OT_ImportMaleMesh(bpy.types.Operator):
    """Import MHRise Male Shadow Mesh"""
    bl_idname = "mhr.import_male_mesh"
    bl_label = "Male Shadow Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=_m_mesh_file)
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


classes = [
    MHR_OT_ImportFemaleMesh,
    MHR_OT_ImportMaleMesh,
]