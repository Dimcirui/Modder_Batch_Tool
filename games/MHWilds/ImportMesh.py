import bpy
import os
from ...operators.general_function import getCollection

from .ToPose import Merge_MHWilds_Facial_Bones


def set_bone_scale(armature_name, scale_value):
    armature = bpy.data.objects.get(armature_name)
    if armature and armature.type == 'ARMATURE':
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        for bone in armature.data.edit_bones:
            bone.length = scale_value
        bpy.ops.object.mode_set(mode='OBJECT')


FemaleMesh = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "MHWilds_Female.fbx")


class importMHWildsfmesh(bpy.types.Operator):
    bl_idname = "mbt.import_mhwilds_fmesh"
    bl_label = "female mesh"
    bl_description = "Import MHWilds full-body nude model of female.\nThe imported model will be placed in a new collection.\nYou can click the wrench icon on the right to adjust the import settings"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 创建一个RE_MESH集合用于放置导入的基本模型
        meshCollection = getCollection("MHWilds_Female.mesh", None, makeNew=True)
        meshCollection.color_tag = "COLOR_01"
        meshCollection["~TYPE"] = "RE_MESH_COLLECTION"
        bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[
            meshCollection.name]

        bpy.ops.import_scene.fbx(filepath=FemaleMesh, use_custom_props=True, force_connect_children=False)
        ArmatureObj = bpy.context.active_object
        ArmatureName = ArmatureObj.data.name
        ArmatureObj["MBT_Armature_Type"] = "MHWilds"
        bpy.ops.object.mode_set(mode='EDIT')

        if bpy.context.scene.mbt_toolpanel.mhwilds_merge_facial_bones == True:
            Merge_MHWilds_Facial_Bones(ArmatureName)

        for bone in ArmatureObj.data.edit_bones:
            bone.length = 0.1
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        if bpy.context.scene.mbt_toolpanel.mhwilds_convert_to_tpose == True:
            bpy.ops.mbt.mhwilds_tpose()

        self.report({'INFO'}, 'import mesh completed')
        return {'FINISHED'}


class importMHWildsfmesh_Settings(bpy.types.Operator):
    bl_label = "import settings"
    bl_description = "Settings for importing model"
    bl_idname = "mbt.import_mhwilds_fmesh_settings"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def check(self, context):
        # Important for changing options
        return True

    def draw(self, context):
        scene = context.scene
        mbt_toolpanel = context.scene.mbt_toolpanel

        layout = self.layout
        col = layout.column(align=True)

        row = col.row(align=True)
        row.prop(mbt_toolpanel, "mhwilds_convert_to_tpose")
        row = col.row(align=True)
        row.prop(mbt_toolpanel, "mhwilds_merge_facial_bones")


classes = [importMHWildsfmesh, importMHWildsfmesh_Settings]
