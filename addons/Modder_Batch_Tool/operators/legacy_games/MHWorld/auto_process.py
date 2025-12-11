import bpy
from bpy.types import Scene
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty

class AutoExportProcess(bpy.types.Operator):
    bl_idname = "tool.autoexportprocess"
    bl_label = "auto export process"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )
    
    def execute(self, context):
        if context.scene.use_quadstotris:
            bpy.ops.object.mode_set(mode='EDIT') 
            bpy.ops.mesh.select_all(action = 'SELECT')
            bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
            bpy.ops.object.mode_set(mode='OBJECT') 
        if context.scene.use_splitseam:
            bpy.ops.object.mode_set(mode='OBJECT') 
            bpy.ops.tool.split_seam_edge() 
        if context.scene.use_unifyuvs:
            bpy.ops.tool.unifyuvs()
        if context.scene.use_separatebymaterials:
            bpy.ops.tool.separatebymaterials()
        if context.scene.use_cleanzerovg:
            bpy.ops.tool.cleanzerovg()
        if context.scene.use_emptiedbl:
            bpy.ops.tool.emptiedblocklabel()
        if context.scene.use_limitvg:
            bpy.ops.tool.normalizelimitvg()
             
        self.report({'INFO'}, 'process completed')
        return {'FINISHED'}


class ProcessSettings(bpy.types.Operator):
    bl_idname = "tool.processsettings"
    bl_label = "Process Settings"
    bl_description = ""

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):       
        return context.window_manager.invoke_props_dialog(self)

    def check(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)

        row = col.row(align=True)
        row.prop(context.scene, "use_quadstotris")
        row = col.row(align=True)
        row.prop(context.scene, "use_splitseam")
        row = col.row(align=True)
        row.prop(context.scene, "use_unifyuvs")
        row = col.row(align=True)
        row.prop(context.scene, "use_separatebymaterials")
        row = col.row(align=True)
        row.prop(context.scene, "use_cleanzerovg")
        row = col.row(align=True)
        row.prop(context.scene, "use_emptiedbl")
        row = col.row(align=True)
        row.prop(context.scene, "use_limitvg")

# === 手动注册/注销属性 ===
def register():
    Scene.use_quadstotris = BoolProperty(
        name="convert quads to tris",
        description="", default=True)   
    Scene.use_splitseam = BoolProperty(
        name="split seam edge",
        description="", default=True)   
    Scene.use_unifyuvs = BoolProperty(
        name="unify UVs",
        description="", default=True)      
    Scene.use_separatebymaterials = BoolProperty(
        name="separate by materials",
        description="", default=True)   
    Scene.use_cleanzerovg = BoolProperty(
        name="clean zero weight vg",
        description="", default=True)  
    Scene.use_emptiedbl = BoolProperty(
        name="emptied blocklabel",
        description="", default=True)   
    Scene.use_limitvg = BoolProperty(
        name="convert 8wt to 4wt",
        description="", default=True) 

def unregister():
    del Scene.use_quadstotris
    del Scene.use_splitseam
    del Scene.use_unifyuvs
    del Scene.use_separatebymaterials
    del Scene.use_cleanzerovg
    del Scene.use_emptiedbl
    del Scene.use_limitvg