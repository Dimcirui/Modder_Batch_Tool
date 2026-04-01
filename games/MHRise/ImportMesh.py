import bpy
import os

_mesh_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mesh")
_f_mesh_file = "f_shadow.mesh.2109148288"
_m_mesh_file = "m_shadow.mesh.2109148288"


def _check_re_mesh():
    return hasattr(bpy.ops, 're_mesh') and hasattr(bpy.ops.re_mesh, 'importfile')


class MHR_OT_ImportFemaleMesh(bpy.types.Operator):
    """Import MHRise Female Shadow Mesh"""
    bl_idname = "mhr.import_female_mesh"
    bl_label = "Female Shadow Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _check_re_mesh()

    def execute(self, context):
        bpy.ops.re_mesh.importfile(
            'EXEC_DEFAULT',
            directory=_mesh_dir + os.sep,
            files=[{"name": _f_mesh_file}],
            clearScene=False,
            loadMaterials=False,
            rotate90=True,
            importAllLODs=False,
        )
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


class MHR_OT_ImportMaleMesh(bpy.types.Operator):
    """Import MHRise Male Shadow Mesh"""
    bl_idname = "mhr.import_male_mesh"
    bl_label = "Male Shadow Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _check_re_mesh()

    def execute(self, context):
        bpy.ops.re_mesh.importfile(
            'EXEC_DEFAULT',
            directory=_mesh_dir + os.sep,
            files=[{"name": _m_mesh_file}],
            clearScene=False,
            loadMaterials=False,
            rotate90=True,
            importAllLODs=False,
        )
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


classes = [
    MHR_OT_ImportFemaleMesh,
    MHR_OT_ImportMaleMesh,
]
