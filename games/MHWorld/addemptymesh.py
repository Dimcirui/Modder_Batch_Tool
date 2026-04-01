import os
import bpy
import pathlib

_mesh_dir = pathlib.Path(__file__).parent / "mesh"


def _check_mod3_importer():
    return hasattr(bpy.ops.mhw_mod3, 'import_mhw_mod3')


class MHW_OT_AddEmptyMesh(bpy.types.Operator):
    """Import an empty mod3 mesh for merging purposes"""
    bl_idname = "mhw.add_empty_mesh"
    bl_label = "Add Empty Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _check_mod3_importer()

    def execute(self, context):
        if not _check_mod3_importer():
            self.report({'ERROR'}, "MHW Model Editor not installed!")
            return {'CANCELLED'}

        bpy.ops.mhw_mod3.import_mhw_mod3('EXEC_DEFAULT', directory=str(_mesh_dir) + os.sep, files=[{"name": "emptymesh.mod3"}])
        self.report({'INFO'}, "Import completed")
        return {'FINISHED'}


classes = [MHW_OT_AddEmptyMesh]