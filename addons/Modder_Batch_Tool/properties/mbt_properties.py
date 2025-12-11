import os

import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty
import math
from ..operators.rw_presets import reloadPresets

def update_MHWildsModDirectoryRelPathToAbs(self,context):
    try:
        if "//" in self.MHWildsModDirectory:
            self.MHWildsModDirectory = os.path.realpath(bpy.path.abspath(self.MHWildsModDirectory))
    except:
        pass


class MBTToolPanelPG(bpy.types.PropertyGroup):

    MHWildsModDirectory: bpy.props.StringProperty(
        name="",
        subtype="DIR_PATH",
        description="Please select a path at the same level as the natives folder",
        update=update_MHWildsModDirectoryRelPathToAbs
    )

    MHWildsFbxskelName: bpy.props.StringProperty(
        name="",
        description="The file name should be consistent with the GameObject name in the pfb file for the body part",
    )

    def getMHWildsBoneList(self, context):
        return reloadPresets("MHWilds")

    MHWildsBoneList: EnumProperty(
        name="",
        description="Dictionary for adsorbing bones and renaming vertex groups",
        items=getMHWildsBoneList
    )

    show_mhwilds: BoolProperty(
        name="MHWilds",
        description="Show MHWilds panel",
        default=True
    )

    mhwilds_convert_to_tpose: BoolProperty(
        name="convert to t-pose",
        description="Whether the imported model armature is converted to t-pose.\nNote that some bones will not be completely zeroed like thumbs, which takes into account the whole posture",
        default=True
    )

    mhwilds_merge_facial_bones: BoolProperty(
        name="merge facial bones",
        description="Whether to merge the facial bones.\nIf you need to make facial animations, don't check it",
        default=True
    )

    # Current_MHWilds_Armature: StringProperty(
    #     name="",
    #     description="",
    #     default=""
    # )

    mhwilds_json_hide_face: BoolProperty(
        name="hide face",
        description="",
        default=True
    )

    mhwilds_json_hide_hair: BoolProperty(
        name="hide hair",
        description="",
        default=True
    )

    mhwilds_json_hide_slinger: BoolProperty(
        name="hide slinger",
        description="",
        default=True
    )

    mhwilds_json_bind_facial: BoolProperty(
        name="bind facial",
        description="",
        default=True
    )

    mhwilds_json_bind_part: EnumProperty(
        name="bind part",
        description="",
        items=[("1", "helm", ""), ("2", "body", "")],
        default=0,
    )
    
    # === 添加 MHRise 开关 ===
    show_mhrise: BoolProperty(
        name="MHRise",
        description="Show MHRise Panel",
        default=False
    )

    # === 添加 MHWorld 开关 ===
    show_mhworld: BoolProperty(
        name="MHWorld",
        description="Show MHWorld Panel",
        default=False
    )