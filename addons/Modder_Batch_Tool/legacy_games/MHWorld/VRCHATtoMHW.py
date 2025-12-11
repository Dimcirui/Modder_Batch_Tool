import bpy

# VRCHAT/通用人形骨骼 -> MHWorld 顶点组映射
# 支持多种命名变体 (下划线、点号、空格等)
_NAME_MAP = {
    # 躯干
    "Hips": "bonefunction_013",
    "Spine": "bonefunction_001",
    "Chest": "bonefunction_002",
    "Neck": "bonefunction_003",
    "Head": "bonefunction_004",
    
    # === 左臂 ===
    "Shoulder_L": "bonefunction_005",
    "Left shoulder": "bonefunction_005",
    "Shoulder.L": "bonefunction_005",
    
    "UpperArm_L": "bonefunction_006",
    "Left arm": "bonefunction_006",
    "LeftUpperArm": "bonefunction_006",
    "UpperArm.L": "bonefunction_006",
    "Upper_arm.L": "bonefunction_006",
    
    "LowerArm_L": "bonefunction_007",
    "Left elbow": "bonefunction_007",
    "LeftLowerArm": "bonefunction_007",
    "LowerArm.L": "bonefunction_007",
    "Lower_arm.L": "bonefunction_007",
    
    "Hand_L": "bonefunction_008",
    "Left wrist": "bonefunction_008",
    "Hand.L": "bonefunction_008",
    
    # === 右臂 ===
    "Shoulder_R": "bonefunction_009",
    "Right shoulder": "bonefunction_009",
    "Shoulder.R": "bonefunction_009",
    
    "UpperArm_R": "bonefunction_010",
    "Right arm": "bonefunction_010",
    "RightUpperArm": "bonefunction_010",
    "UpperArm.R": "bonefunction_010",
    "Upper_arm.R": "bonefunction_010",
    
    "LowerArm_R": "bonefunction_011",
    "Right elbow": "bonefunction_011",
    "RightLowerArm": "bonefunction_011",
    "LowerArm.R": "bonefunction_011",
    "Lower_arm.R": "bonefunction_011",
    
    "Hand_R": "bonefunction_012",
    "Right wrist": "bonefunction_012",
    "Hand.R": "bonefunction_012",
    
    # === 左腿 ===
    "UpperLeg_L": "bonefunction_014",
    "Left leg": "bonefunction_014",
    "LeftUpperLeg": "bonefunction_014",
    "UpperLeg.L": "bonefunction_014",
    "Upper_leg.L": "bonefunction_014",
    
    "LowerLeg_L": "bonefunction_015",
    "Left knee": "bonefunction_015",
    "LeftLowerLeg": "bonefunction_015",
    "LowerLeg.L": "bonefunction_015",
    "Lower_leg.L": "bonefunction_015",
    
    "Foot_L": "bonefunction_016",
    "Left ankle": "bonefunction_016",
    "Foot.L": "bonefunction_016",
    
    "Toe_L": "bonefunction_017",
    "Left toe": "bonefunction_017",
    "Toe.L": "bonefunction_017",
    
    # === 右腿 ===
    "UpperLeg_R": "bonefunction_018",
    "Right leg": "bonefunction_018",
    "RightUpperLeg": "bonefunction_018",
    "UpperLeg.R": "bonefunction_018",
    "Upper_leg.R": "bonefunction_018",
    
    "LowerLeg_R": "bonefunction_019",
    "Right knee": "bonefunction_019",
    "RightLowerLeg": "bonefunction_019",
    "LowerLeg.R": "bonefunction_019",
    "Lower_leg.R": "bonefunction_019",
    
    "Foot_R": "bonefunction_020",
    "Right ankle": "bonefunction_020",
    "Foot.R": "bonefunction_020",
    
    "Toe_R": "bonefunction_021",
    "Right toe": "bonefunction_021",
    "Toe.R": "bonefunction_021",
    
    # === 左手指 - 拇指 ===
    "ThumbProximal_L": "bonefunction_031",
    "Thumb_Proximal_L": "bonefunction_031",
    "LeftThumbProximal": "bonefunction_031",
    "ThumbProximal.L": "bonefunction_031",
    "Thumb1_L": "bonefunction_031",
    "Thumb Proximal.L": "bonefunction_031",
    
    "ThumbIntermediate_L": "bonefunction_032",
    "Thumb_Intermediate_L": "bonefunction_032",
    "LeftThumbIntermediate": "bonefunction_032",
    "ThumbIntermediate.L": "bonefunction_032",
    "Thumb2_L": "bonefunction_032",
    "Thumb Intermediate.L": "bonefunction_032",
    
    "ThumbDistal_L": "bonefunction_033",
    "Thumb_Distal_L": "bonefunction_033",
    "LeftThumbDistal": "bonefunction_033",
    "ThumbDistal.L": "bonefunction_033",
    "Thumb3_L": "bonefunction_033",
    "Thumb Distal.L": "bonefunction_033",
    
    # === 左手指 - 食指 ===
    "IndexProximal_L": "bonefunction_034",
    "Index_Proximal_L": "bonefunction_034",
    "LeftIndexProximal": "bonefunction_034",
    "IndexProximal.L": "bonefunction_034",
    "IndexFinger1_L": "bonefunction_034",
    "Index Proximal.L": "bonefunction_034",
    
    "IndexIntermediate_L": "bonefunction_035",
    "Index_Intermediate_L": "bonefunction_035",
    "LeftIndexIntermediate": "bonefunction_035",
    "IndexIntermediate.L": "bonefunction_035",
    "IndexFinger2_L": "bonefunction_035",
    "Index Intermediate.L": "bonefunction_035",
    
    "IndexDistal_L": "bonefunction_036",
    "Index_Distal_L": "bonefunction_036",
    "LeftIndexDistal": "bonefunction_036",
    "IndexDistal.L": "bonefunction_036",
    "IndexFinger3_L": "bonefunction_036",
    "Index Distal.L": "bonefunction_036",
    
    # === 左手指 - 中指 ===
    "MiddleProximal_L": "bonefunction_037",
    "Middle_Proximal_L": "bonefunction_037",
    "LeftMiddleProximal": "bonefunction_037",
    "MiddleProximal.L": "bonefunction_037",
    "MiddleFinger1_L": "bonefunction_037",
    "Middle Proximal.L": "bonefunction_037",
    
    "MiddleIntermediate_L": "bonefunction_038",
    "Middle_Intermediate_L": "bonefunction_038",
    "LeftMiddleIntermediate": "bonefunction_038",
    "MiddleIntermediate.L": "bonefunction_038",
    "MiddleFinger2_L": "bonefunction_038",
    "Middle Intermediate.L": "bonefunction_038",
    
    "MiddleDistal_L": "bonefunction_039",
    "Middle_Distal_L": "bonefunction_039",
    "LeftMiddleDistal": "bonefunction_039",
    "MiddleDistal.L": "bonefunction_039",
    "MiddleFinger3_L": "bonefunction_039",
    "Middle Distal.L": "bonefunction_039",
    
    # === 左手指 - 无名指 ===
    "RingProximal_L": "bonefunction_041",
    "Ring_Proximal_L": "bonefunction_041",
    "LeftRingProximal": "bonefunction_041",
    "RingProximal.L": "bonefunction_041",
    "RingFinger1_L": "bonefunction_041",
    "Ring Proximal.L": "bonefunction_041",
    
    "RingIntermediate_L": "bonefunction_042",
    "Ring_Intermediate_L": "bonefunction_042",
    "LeftRingIntermediate": "bonefunction_042",
    "RingIntermediate.L": "bonefunction_042",
    "RingFinger2_L": "bonefunction_042",
    "Ring Intermediate.L": "bonefunction_042",
    
    "RingDistal_L": "bonefunction_043",
    "Ring_Distal_L": "bonefunction_043",
    "LeftRingDistal": "bonefunction_043",
    "RingDistal.L": "bonefunction_043",
    "RingFinger3_L": "bonefunction_043",
    "Ring Distal.L": "bonefunction_043",
    
    # === 左手指 - 小指 ===
    "LittleProximal_L": "bonefunction_044",
    "Little_Proximal_L": "bonefunction_044",
    "LeftLittleProximal": "bonefunction_044",
    "LittleProximal.L": "bonefunction_044",
    "LittleFinger1_L": "bonefunction_044",
    "Little Proximal.L": "bonefunction_044",
    
    "LittleIntermediate_L": "bonefunction_045",
    "Little_Intermediate_L": "bonefunction_045",
    "LeftLittleIntermediate": "bonefunction_045",
    "LittleIntermediate.L": "bonefunction_045",
    "LittleFinger2_L": "bonefunction_045",
    "Little Intermediate.L": "bonefunction_045",
    
    "LittleDistal_L": "bonefunction_046",
    "Little_Distal_L": "bonefunction_046",
    "LeftLittleDistal": "bonefunction_046",
    "LittleDistal.L": "bonefunction_046",
    "LittleFinger3_L": "bonefunction_046",
    "Little Distal.L": "bonefunction_046",
    
    # === 右手指 - 拇指 ===
    "ThumbProximal_R": "bonefunction_048",
    "Thumb_Proximal_R": "bonefunction_048",
    "RightThumbProximal": "bonefunction_048",
    "ThumbProximal.R": "bonefunction_048",
    "Thumb1_R": "bonefunction_048",
    "Thumb Proximal.R": "bonefunction_048",
    
    "ThumbIntermediate_R": "bonefunction_049",
    "Thumb_Intermediate_R": "bonefunction_049",
    "RightThumbIntermediate": "bonefunction_049",
    "ThumbIntermediate.R": "bonefunction_049",
    "Thumb2_R": "bonefunction_049",
    "Thumb Intermediate.R": "bonefunction_049",
    
    "ThumbDistal_R": "bonefunction_050",
    "Thumb_Distal_R": "bonefunction_050",
    "RightThumbDistal": "bonefunction_050",
    "ThumbDistal.R": "bonefunction_050",
    "Thumb3_R": "bonefunction_050",
    "Thumb Distal.R": "bonefunction_050",
    
    # === 右手指 - 食指 ===
    "IndexProximal_R": "bonefunction_051",
    "Index_Proximal_R": "bonefunction_051",
    "RightIndexProximal": "bonefunction_051",
    "IndexProximal.R": "bonefunction_051",
    "IndexFinger1_R": "bonefunction_051",
    "Index Proximal.R": "bonefunction_051",
    
    "IndexIntermediate_R": "bonefunction_052",
    "Index_Intermediate_R": "bonefunction_052",
    "RightIndexIntermediate": "bonefunction_052",
    "IndexIntermediate.R": "bonefunction_052",
    "IndexFinger2_R": "bonefunction_052",
    "Index Intermediate.R": "bonefunction_052",
    
    "IndexDistal_R": "bonefunction_053",
    "Index_Distal_R": "bonefunction_053",
    "RightIndexDistal": "bonefunction_053",
    "IndexDistal.R": "bonefunction_053",
    "IndexFinger3_R": "bonefunction_053",
    "Index Distal.R": "bonefunction_053",
    
    # === 右手指 - 中指 ===
    "MiddleProximal_R": "bonefunction_054",
    "Middle_Proximal_R": "bonefunction_054",
    "RightMiddleProximal": "bonefunction_054",
    "MiddleProximal.R": "bonefunction_054",
    "MiddleFinger1_R": "bonefunction_054",
    "Middle Proximal.R": "bonefunction_054",
    
    "MiddleIntermediate_R": "bonefunction_055",
    "Middle_Intermediate_R": "bonefunction_055",
    "RightMiddleIntermediate": "bonefunction_055",
    "MiddleIntermediate.R": "bonefunction_055",
    "MiddleFinger2_R": "bonefunction_055",
    "Middle Intermediate.R": "bonefunction_055",
    
    "MiddleDistal_R": "bonefunction_056",
    "Middle_Distal_R": "bonefunction_056",
    "RightMiddleDistal": "bonefunction_056",
    "MiddleDistal.R": "bonefunction_056",
    "MiddleFinger3_R": "bonefunction_056",
    "Middle Distal.R": "bonefunction_056",
    
    # === 右手指 - 无名指 ===
    "RingProximal_R": "bonefunction_058",
    "Ring_Proximal_R": "bonefunction_058",
    "RightRingProximal": "bonefunction_058",
    "RingProximal.R": "bonefunction_058",
    "RingFinger1_R": "bonefunction_058",
    "Ring Proximal.R": "bonefunction_058",
    
    "RingIntermediate_R": "bonefunction_059",
    "Ring_Intermediate_R": "bonefunction_059",
    "RightRingIntermediate": "bonefunction_059",
    "RingIntermediate.R": "bonefunction_059",
    "RingFinger2_R": "bonefunction_059",
    "Ring Intermediate.R": "bonefunction_059",
    
    "RingDistal_R": "bonefunction_060",
    "Ring_Distal_R": "bonefunction_060",
    "RightRingDistal": "bonefunction_060",
    "RingDistal.R": "bonefunction_060",
    "RingFinger3_R": "bonefunction_060",
    "Ring Distal.R": "bonefunction_060",
    
    # === 右手指 - 小指 ===
    "LittleProximal_R": "bonefunction_061",
    "Little_Proximal_R": "bonefunction_061",
    "RightLittleProximal": "bonefunction_061",
    "LittleProximal.R": "bonefunction_061",
    "LittleFinger1_R": "bonefunction_061",
    "Little Proximal.R": "bonefunction_061",
    
    "LittleIntermediate_R": "bonefunction_062",
    "Little_Intermediate_R": "bonefunction_062",
    "RightLittleIntermediate": "bonefunction_062",
    "LittleIntermediate.R": "bonefunction_062",
    "LittleFinger2_R": "bonefunction_062",
    "Little Intermediate.R": "bonefunction_062",
    
    "LittleDistal_R": "bonefunction_063",
    "Little_Distal_R": "bonefunction_063",
    "RightLittleDistal": "bonefunction_063",
    "LittleDistal.R": "bonefunction_063",
    "LittleFinger3_R": "bonefunction_063",
    "Little Distal.R": "bonefunction_063",
    
    # === 辅助骨骼 ===
    "LowerArm_twist_L": "bonefunction_081",
    "LowerArm_Twist_L": "bonefunction_081",
    "LowerArm_twist_R": "bonefunction_083",
    "LowerArm_Twist_R": "bonefunction_083",
    
    "Hips_L": "bonefunction_074",
    "Hips_R": "bonefunction_076",
}


class MHW_OT_VRCHATtoMHW(bpy.types.Operator):
    """Convert VRCHAT/Humanoid vertex groups to MHWorld format"""
    bl_idname = "mhw.vrchat_to_mhw"
    bl_label = "VRCHAT to MHWorld"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == "MESH" for obj in context.selected_objects)

    def execute(self, context):
        count = 0
        for obj in context.selected_objects:
            if obj.type == "MESH":
                vgroups = obj.vertex_groups
                for old_name, new_name in _NAME_MAP.items():
                    if old_name in vgroups:
                        vgroups[old_name].name = new_name
                count += 1
        
        self.report({'INFO'}, f"Converted {count} mesh(es)")
        return {'FINISHED'}


classes = [
    MHW_OT_VRCHATtoMHW,
]