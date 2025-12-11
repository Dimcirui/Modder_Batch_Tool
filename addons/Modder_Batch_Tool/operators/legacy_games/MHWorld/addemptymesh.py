import bpy
import pathlib
import os

main_dir = pathlib.Path(os.path.dirname(__file__)).parent.resolve()
resources_dir = os.path.join(str(main_dir), "MHWorld")
mesh_dir = os.path.join(str(resources_dir), "mesh")
empty_mesh_file = os.path.join(mesh_dir, "emptymesh.mod3")
 

class AddMHWorldemptymesh(bpy.types.Operator):
    bl_idname = "tool.addmhworldemptymesh"
    bl_label = "add empty meshes"
    bl_options = {'REGISTER', 'UNDO'}
 
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "ARMATURE" ) 
   
    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        armature_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "ARMATURE"])
        for n in armature_sel_name:
            bpy.ops.custom_import.import_mhw_mod3(filepath=empty_mesh_file)
            mesh_import_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])
            armature_import_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "ARMATURE"])
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
            
            
            bpy.context.view_layer.objects.active = bpy.data.objects[mesh_import_name[0]]
            emptyobj=bpy.context.active_object
            emptyobj.data["blockLabel"]=""
            bpy.context.view_layer.update() 
            bpy.ops.object.modifier_remove()
            modifier =  emptyobj.modifiers[0]
            modifier.object = bpy.data.objects[n]
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')
            emptyobj.vertex_groups.remove(emptyobj.vertex_groups[0])
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=armature_import_name[0], case_sensitive=False, extend=False)
            bpy.ops.object.delete(use_global=False)

        bpy.context.view_layer.objects.active = bpy.data.objects[armature_sel_name[0]]
        for n in armature_sel_name:
            bpy.ops.object.select_pattern(pattern=n, case_sensitive=False, extend=True)
        self.report({'INFO'}, 'add completed')     
        return {'FINISHED'}





