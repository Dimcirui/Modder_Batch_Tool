import bpy

class EmptiedBlockLabel(bpy.types.Operator):
    bl_idname = "tool.emptiedblocklabel"
    bl_label = "emptied blocklabel"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )
    
    def execute(self, context):
        meshes_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])

        for n in meshes_sel_name:
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            emptyobj=bpy.context.active_object
            emptyobj.data["blockLabel"]=""
            bpy.context.view_layer.update() 
           
        bpy.context.view_layer.objects.active = bpy.data.objects[meshes_sel_name[0]]
        self.report({'INFO'}, 'emptied completed')
        return {'FINISHED'}


   

