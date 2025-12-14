import bpy
import os
from ..config import __addon_name__
from ..operators.imagecombiner import globs
from ..operators.imagecombiner.icons import get_icon_id
from ....common.i18n.i18n import i18n
from ....common.types.framework import reg_order
from ..operators.imagecombiner.type_annotations import Scene

# class BasePanel(object):
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "Modder Batch Tool"
#
#     @classmethod
#     def poll(self, context: bpy.types.Context):
#         return context is not None

@reg_order(0)
class MBTShowPanel(bpy.types.Panel):
    bl_label = "Show Panel Settings"
    bl_idname = "OBJECT_PT_MBT_ShowPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder Batch Tool"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context: bpy.types.Context):
        return context is not None

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        scene = context.scene
        mbt_toolpanel = context.scene.mbt_toolpanel
        row.prop(mbt_toolpanel, "show_mhwilds")
        
        row = layout.row()
        row.prop(mbt_toolpanel, "show_mhrise")
        row = layout.row()
        row.prop(mbt_toolpanel, "show_mhworld")

@reg_order(1)
class UniversalFunction(bpy.types.Panel):
    bl_label = "Universal Function"
    bl_idname = "OBJECT_PT_MBT_UniversalFunction"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder Batch Tool"

    @classmethod
    def poll(self, context: bpy.types.Context):
        return context is not None

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("mbt.separate_by_materials", icon="OUTLINER_OB_MESH")

        row = layout.row()
        row.operator("mbt.clean_zero_vg", icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("mbt.remove_shapekeys", icon="OUTLINER_DATA_MESH")

        # layout.label(text="Batch delete unnecessary UVs and unify UV names")
        row = layout.row()
        row.operator("mbt.unify_uvs", icon="OUTLINER_DATA_MESH")

        # layout.label(text="Batch delete unnecessary UVs and unify UV names")
        row = layout.row()
        row.operator("mbt.merge_meshes_with_same_texture", icon="OUTLINER_OB_MESH")


@reg_order(2)
class MBTMHWilds(bpy.types.Panel):
    bl_label = "MHWilds"
    bl_idname = "OBJECT_PT_MBT_MHWilds"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder Batch Tool"
    # bl_context = "objectmode"
    # bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        mbt_toolpanel = context.scene.mbt_toolpanel
        return bool(mbt_toolpanel.show_mhwilds)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mbt_toolpanel = context.scene.mbt_toolpanel
        # row = layout.row()
        # row.scale_y = 1.2
        # row.label(text="Make sure you have installed <RE Mesh Editor> plugin", icon="INFO")

        # layout.label(text="Current MHWilds Armature:")
        # layout.prop_search(mbt_toolpanel, "Current_MHWilds_Armature", bpy.data, "armatures")

        layout.label(text="Import MHWilds basic mesh")
        # row = layout.row()
        # row.prop(mbt_toolpanel, "mhwilds_convert_to_tpose")
        # row = layout.row()
        # row.operator("mbt.import_mhwilds_fmesh", icon="OUTLINER_OB_MESH")
        # row.operator("tool.importmhwildsmmesh", icon="OUTLINER_OB_MESH")

        split = layout.row(align=True)
        row = split.row(align=True)
        row.operator("mbt.import_mhwilds_fmesh", icon="OUTLINER_OB_MESH")
        row = split.row(align=True)
        row.alignment = 'RIGHT'
        row.operator("mbt.import_mhwilds_fmesh_settings", text="", icon='MODIFIER')

        layout.label(text="Convert to t-pose")
        row = layout.row()
        row.operator("mbt.mhwilds_tpose", icon="OUTLINER_OB_ARMATURE")
        row = layout.row()

        layout.label(text="Batch absorb bones (only support t-pose)")
        row = layout.row()
        row.scale_y = 1.2
        row.label(text="Please select both the external skeleton and MHWilds skeleton, and then press absorb bones",
                  icon="ERROR")
        # row = layout.row()
        # row.prop(mbt_toolpanel, "mhwilds_merge_facial_bones")
        row = layout.row()
        row.prop(mbt_toolpanel, "MHWildsBoneList")
        row.operator("mbt.mhwilds_open_dictionary_folder", icon="FILEBROWSER")
        layout.operator("mbt.mhwilds_snapbone", icon="OUTLINER_OB_ARMATURE")

        # layout.label(text="Batch rename vertex groups")
        row = layout.row()
        row.operator("mbt.mhwilds_rename_vg", icon="OUTLINER_DATA_MESH")
        # row = layout.row()
        # row.operator("mbt.mhwilds_merge_bones")

        layout.label(text="Batch normalize and limit weight to 6wt")
        row = layout.row()
        row.operator("mbt.normalize_limit_6wt_vg", icon="OUTLINER_DATA_MESH")

        # layout.label(text="Batch split seam edge")
        # row = layout.row()
        # row.operator("mbt.split_seam_edge", icon="OUTLINER_DATA_MESH")

        layout.label(text="Batch rename meshes to re format")
        row = layout.row()
        row.operator("mbt.rename_mesh_to_reformat", icon="OUTLINER_DATA_MESH")

        # layout.label(text="Generate or export fbxskel")
        # row = layout.row()
        # row.operator("mbt.generate_fbxskel", icon="OUTLINER_OB_ARMATURE")
        # row.operator("mbt.export_fbxskel", icon="OUTLINER_OB_ARMATURE")

        # layout.label(text="Set mod directory")
        # row = layout.row()
        # row.prop(mbt_toolpanel, "MHWildsModDirectory")
        #
        # layout.label(text="Export fbxskel and json for bone system")
        # split = layout.row(align=True)
        # row = split.row(align=True)
        # row.operator("mbt.export_fbxskel_json", icon="OUTLINER_OB_ARMATURE")
        # row = split.row(align=True)
        # row.alignment = 'RIGHT'
        # row.operator("mbt.export_fbxskel_json_settings", text="", icon='MODIFIER')


@reg_order(3)
class MBTMHWildsFbxskel(bpy.types.Panel):
    bl_label = "Export fbxskel"
    bl_idname = "OBJECT_PT_MBT_MHWilds_Fbxskel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # bl_category = "Modder Batch Tool"
    bl_parent_id = "OBJECT_PT_MBT_MHWilds"
    # bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context: bpy.types.Context):
        return context is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mbt_toolpanel = context.scene.mbt_toolpanel

        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=False)
        row.scale_y = 1.2
        row.label(text="Please perform the operations in order", icon="ERROR")
        col.separator()
        row = col.row(align=False);
        row.scale_y = 0.75
        row.label(text="1.Download and install Bone System")

        col.separator()
        row = col.row();
        row.scale_y = 1.1
        button = row.operator("mtb.mhwilds_bonesystem_caimogu_website")

        col.separator()
        row = col.row(align=False);
        row.scale_y = 1.1
        row.label(text="2.Set the mod file path")

        col.separator()
        row = col.row();
        row.scale_y = 1.1
        row.prop(mbt_toolpanel, "MHWildsModDirectory")

        col.separator()
        row = col.row(align=False);
        row.scale_y = 1.1
        row.label(text="3.Set file name")

        col.separator()
        row = col.row();
        row.scale_y = 1.1
        row.prop(mbt_toolpanel, "MHWildsFbxskelName")

        col.separator()
        row = col.row(align=False);
        row.scale_y = 1.1
        row.label(text="4.Export fbxskel and json")

        col.separator()
        row = col.row();
        split = col.row(align=True)
        row = split.row(align=True)
        row.scale_y = 1.1
        row.operator("mbt.export_fbxskel_json", icon="OUTLINER_OB_ARMATURE")
        row = split.row(align=True)
        row.alignment = 'RIGHT'
        row.scale_y = 1.1
        row.operator("mbt.export_fbxskel_json_settings", text="", icon='MODIFIER')



DIR_PATH = os.path.dirname(os.path.split(os.path.abspath(__file__))[0])
ICONS_PATH = os.path.join(DIR_PATH, "icons")
PCOLL = None
preview_collections = {}
@reg_order(4)
class MBTCredits(bpy.types.Panel):
    global PCOLL
    bl_label = "Credits"
    bl_idname = "OBJECT_PT_MBT_credits"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder Batch Tool"
    # bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context: bpy.types.Context):
        return context is not None

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=False)
        row.label(text = f"Modder Batch Tool", icon_value=preview_collections["icons"]["korone"].icon_id)
        col.separator()
        row = col.row(align=False) ; row.scale_y = 0.75
        row.label(text = "Modified by:")
        row = col.row(align=False) ; row.scale_y = 0.75
        row.label(text = "Korone, Dimcirui")
        col.separator()
        row = col.row(align=False) ; row.scale_y = 0.75
        row.label(text = "Special thanks:")
        row = col.row(align=False) ; row.scale_y = 0.75
        row.label(text = "ZJCS, Dytser, Shotariya, NSACloud")
        col.separator()
        row = col.row() ; row.scale_y = 1.1
        button = row.operator("mtb.github_website", icon_value=preview_collections["icons"]["github"].icon_id)
        row = col.row() ; row.scale_y = 1.1
        button = row.operator("mtb.bilibili_website", icon_value=preview_collections["icons"]["bilibili"].icon_id)
        row = col.row() ; row.scale_y = 1.1
        button = row.operator("mtb.qq_website", icon_value=preview_collections["icons"]["qq"].icon_id)
        row = col.row() ; row.scale_y = 1.1
        button = row.operator("mtb.caimogu_website", icon_value=preview_collections["icons"]["caimogu"].icon_id)

@reg_order(5)
class MBTMHRise(bpy.types.Panel):
    bl_label = "MHRise"
    bl_idname = "OBJECT_PT_MBT_MHRise"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder Batch Tool"

    @classmethod
    def poll(cls, context):
        try:
            return context.scene.mbt_toolpanel.show_mhrise
        except:
            return False

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Import MHRise shadow mesh")
        row = layout.row()
        row.operator("mhr.import_female_mesh", icon="OUTLINER_OB_MESH")
        row.operator("mhr.import_male_mesh", icon="OUTLINER_OB_MESH")
        
        layout.label(text="Batch Snap Bones")
        row = layout.row()
        row.operator("mhr.snap_bones_mmd", icon="OUTLINER_OB_ARMATURE")
        
        layout.label(text="Rename Vertex Groups")
        row = layout.row()
        row.operator("mhr.mmd_to_mhr", icon="OUTLINER_DATA_MESH")
        row.operator("mhr.uma_to_mhr", icon="OUTLINER_DATA_MESH")
        row.operator("mhr.mhw_to_mhr", icon="OUTLINER_DATA_MESH")
        
        row = layout.row()
        row.operator("mhr.xps_to_mhr", icon="OUTLINER_DATA_MESH")


@reg_order(6)
class MBTMHWorld(bpy.types.Panel):
    bl_label = "MHWorld"
    bl_idname = "OBJECT_PT_MBT_MHWorld"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder Batch Tool"

    @classmethod
    def poll(cls, context):
        try:
            return context.scene.mbt_toolpanel.show_mhworld
        except:
            return False

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Import MHWorld basic armature")
        row = layout.row()
        row.operator("mhw.import_female_mesh", icon="OUTLINER_OB_MESH")
        row.operator("mhw.import_male_mesh", icon="OUTLINER_OB_MESH")

        layout.label(text="Batch Snap Bones")
        row = layout.row()
        row.operator("mhw.snap_bones_mmd", icon="OUTLINER_OB_ARMATURE")
        row = layout.row()
        row.operator("mhw.attach_bones_endfield", text="Attach Endfield Bones", icon="OUTLINER_OB_ARMATURE")

        layout.label(text="Rename Vertex Groups")
        row = layout.row()
        row.operator("mhw.mmd_to_mhw", icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("mhw.vrchat_to_mhw", icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("mhw.uma_to_mhw", icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("mhw.mhr_to_mhw", icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("mhw.endfield_to_mhw", text="Endfield to MHW", icon="OUTLINER_DATA_MESH")
        
        layout.label(text="Utility")
        row = layout.row()
        row.operator("mhw.add_empty_mesh", icon="MESH_CUBE")
        
        layout.label(text="Auto Process (Check Settings First)")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("mhw.auto_export_process", icon="PLAY")
        row.operator("mhw.process_settings", text="", icon="PREFERENCES")