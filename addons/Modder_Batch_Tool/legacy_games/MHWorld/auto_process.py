import bpy
from bpy.types import Scene
from bpy.props import BoolProperty


class MHW_OT_AutoExportProcess(bpy.types.Operator):
    """Auto export process for selected meshes"""
    bl_idname = "mhw.auto_export_process"
    bl_label = "Auto Export Process"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == "MESH" for obj in context.selected_objects)

    def execute(self, context):
        scene = context.scene
        
        if scene.mhw_use_quadstotris:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
            bpy.ops.object.mode_set(mode='OBJECT')
            
        if scene.mhw_use_splitseam:
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.tool.split_seam_edge()
            
        if scene.mhw_use_unifyuvs:
            bpy.ops.tool.unifyuvs()
            
        if scene.mhw_use_separatebymaterials:
            bpy.ops.tool.separatebymaterials()
            
        if scene.mhw_use_cleanzerovg:
            bpy.ops.tool.cleanzerovg()
            
        if scene.mhw_use_limitvg:
            bpy.ops.tool.normalizelimitvg()

        self.report({'INFO'}, "Process completed")
        return {'FINISHED'}


class MHW_OT_ProcessSettings(bpy.types.Operator):
    """Open process settings dialog"""
    bl_idname = "mhw.process_settings"
    bl_label = "Process Settings"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        col = layout.column(align=True)
        col.prop(scene, "mhw_use_quadstotris")
        col.prop(scene, "mhw_use_splitseam")
        col.prop(scene, "mhw_use_unifyuvs")
        col.prop(scene, "mhw_use_separatebymaterials")
        col.prop(scene, "mhw_use_cleanzerovg")
        col.prop(scene, "mhw_use_limitvg")


# === 类列表 ===
classes = [
    MHW_OT_AutoExportProcess,
    MHW_OT_ProcessSettings,
]


# === 属性注册 (加前缀避免冲突) ===
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    Scene.mhw_use_quadstotris = BoolProperty(
        name="Convert Quads to Tris",
        default=True
    )
    Scene.mhw_use_splitseam = BoolProperty(
        name="Split Seam Edge",
        default=True
    )
    Scene.mhw_use_unifyuvs = BoolProperty(
        name="Unify UVs",
        default=True
    )
    Scene.mhw_use_separatebymaterials = BoolProperty(
        name="Separate by Materials",
        default=True
    )
    Scene.mhw_use_cleanzerovg = BoolProperty(
        name="Clean Zero Weight VG",
        default=True
    )
    Scene.mhw_use_limitvg = BoolProperty(
        name="Convert 8wt to 4wt",
        default=True
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del Scene.mhw_use_quadstotris
    del Scene.mhw_use_splitseam
    del Scene.mhw_use_unifyuvs
    del Scene.mhw_use_separatebymaterials
    del Scene.mhw_use_cleanzerovg
    del Scene.mhw_use_limitvg