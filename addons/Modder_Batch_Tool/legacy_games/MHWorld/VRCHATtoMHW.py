import bpy

# VRCHAT/通用人形骨骼 -> MHWorld 顶点组映射
# 支持多种命名变体 (下划线、点号、空格等)
_NAME_MAP = {
    # 躯干
    "Hips": "MHBone_013",
    "Spine": "MHBone_001",
    "Chest": "MHBone_002",
    "Neck": "MHBone_003",
    "Head": "MHBone_004",
    
    # === 左臂 ===
    "Shoulder_L": "MHBone_005",
    "Left shoulder": "MHBone_005",
    "Shoulder.L": "MHBone_005",
    
    "UpperArm_L": "MHBone_006",
    "Left arm": "MHBone_006",
    "LeftUpperArm": "MHBone_006",
    "UpperArm.L": "MHBone_006",
    "Upper_arm.L": "MHBone_006",
    
    "LowerArm_L": "MHBone_007",
    "Left elbow": "MHBone_007",
    "LeftLowerArm": "MHBone_007",
    "LowerArm.L": "MHBone_007",
    "Lower_arm.L": "MHBone_007",
    
    "Hand_L": "MHBone_008",
    "Left wrist": "MHBone_008",
    "Hand.L": "MHBone_008",
    
    # === 右臂 ===
    "Shoulder_R": "MHBone_009",
    "Right shoulder": "MHBone_009",
    "Shoulder.R": "MHBone_009",
    
    "UpperArm_R": "MHBone_010",
    "Right arm": "MHBone_010",
    "RightUpperArm": "MHBone_010",
    "UpperArm.R": "MHBone_010",
    "Upper_arm.R": "MHBone_010",
    
    "LowerArm_R": "MHBone_011",
    "Right elbow": "MHBone_011",
    "RightLowerArm": "MHBone_011",
    "LowerArm.R": "MHBone_011",
    "Lower_arm.R": "MHBone_011",
    
    "Hand_R": "MHBone_012",
    "Right wrist": "MHBone_012",
    "Hand.R": "MHBone_012",
    
    # === 左腿 ===
    "UpperLeg_L": "MHBone_014",
    "Left leg": "MHBone_014",
    "LeftUpperLeg": "MHBone_014",
    "UpperLeg.L": "MHBone_014",
    "Upper_leg.L": "MHBone_014",
    
    "LowerLeg_L": "MHBone_015",
    "Left knee": "MHBone_015",
    "LeftLowerLeg": "MHBone_015",
    "LowerLeg.L": "MHBone_015",
    "Lower_leg.L": "MHBone_015",
    
    "Foot_L": "MHBone_016",
    "Left ankle": "MHBone_016",
    "Foot.L": "MHBone_016",
    
    "Toe_L": "MHBone_017",
    "Left toe": "MHBone_017",
    "Toe.L": "MHBone_017",
    
    # === 右腿 ===
    "UpperLeg_R": "MHBone_018",
    "Right leg": "MHBone_018",
    "RightUpperLeg": "MHBone_018",
    "UpperLeg.R": "MHBone_018",
    "Upper_leg.R": "MHBone_018",
    
    "LowerLeg_R": "MHBone_019",
    "Right knee": "MHBone_019",
    "RightLowerLeg": "MHBone_019",
    "LowerLeg.R": "MHBone_019",
    "Lower_leg.R": "MHBone_019",
    
    "Foot_R": "MHBone_020",
    "Right ankle": "MHBone_020",
    "Foot.R": "MHBone_020",
    
    "Toe_R": "MHBone_021",
    "Right toe": "MHBone_021",
    "Toe.R": "MHBone_021",
    
    # === 左手指 - 拇指 ===
    "ThumbProximal_L": "MHBone_031",
    "Thumb_Proximal_L": "MHBone_031",
    "LeftThumbProximal": "MHBone_031",
    "ThumbProximal.L": "MHBone_031",
    "Thumb1_L": "MHBone_031",
    "Thumb Proximal.L": "MHBone_031",
    
    "ThumbIntermediate_L": "MHBone_032",
    "Thumb_Intermediate_L": "MHBone_032",
    "LeftThumbIntermediate": "MHBone_032",
    "ThumbIntermediate.L": "MHBone_032",
    "Thumb2_L": "MHBone_032",
    "Thumb Intermediate.L": "MHBone_032",
    
    "ThumbDistal_L": "MHBone_033",
    "Thumb_Distal_L": "MHBone_033",
    "LeftThumbDistal": "MHBone_033",
    "ThumbDistal.L": "MHBone_033",
    "Thumb3_L": "MHBone_033",
    "Thumb Distal.L": "MHBone_033",
    
    # === 左手指 - 食指 ===
    "IndexProximal_L": "MHBone_034",
    "Index_Proximal_L": "MHBone_034",
    "LeftIndexProximal": "MHBone_034",
    "IndexProximal.L": "MHBone_034",
    "IndexFinger1_L": "MHBone_034",
    "Index Proximal.L": "MHBone_034",
    
    "IndexIntermediate_L": "MHBone_035",
    "Index_Intermediate_L": "MHBone_035",
    "LeftIndexIntermediate": "MHBone_035",
    "IndexIntermediate.L": "MHBone_035",
    "IndexFinger2_L": "MHBone_035",
    "Index Intermediate.L": "MHBone_035",
    
    "IndexDistal_L": "MHBone_036",
    "Index_Distal_L": "MHBone_036",
    "LeftIndexDistal": "MHBone_036",
    "IndexDistal.L": "MHBone_036",
    "IndexFinger3_L": "MHBone_036",
    "Index Distal.L": "MHBone_036",
    
    # === 左手指 - 中指 ===
    "MiddleProximal_L": "MHBone_037",
    "Middle_Proximal_L": "MHBone_037",
    "LeftMiddleProximal": "MHBone_037",
    "MiddleProximal.L": "MHBone_037",
    "MiddleFinger1_L": "MHBone_037",
    "Middle Proximal.L": "MHBone_037",
    
    "MiddleIntermediate_L": "MHBone_038",
    "Middle_Intermediate_L": "MHBone_038",
    "LeftMiddleIntermediate": "MHBone_038",
    "MiddleIntermediate.L": "MHBone_038",
    "MiddleFinger2_L": "MHBone_038",
    "Middle Intermediate.L": "MHBone_038",
    
    "MiddleDistal_L": "MHBone_039",
    "Middle_Distal_L": "MHBone_039",
    "LeftMiddleDistal": "MHBone_039",
    "MiddleDistal.L": "MHBone_039",
    "MiddleFinger3_L": "MHBone_039",
    "Middle Distal.L": "MHBone_039",
    
    # === 左手指 - 无名指 ===
    "RingProximal_L": "MHBone_041",
    "Ring_Proximal_L": "MHBone_041",
    "LeftRingProximal": "MHBone_041",
    "RingProximal.L": "MHBone_041",
    "RingFinger1_L": "MHBone_041",
    "Ring Proximal.L": "MHBone_041",
    
    "RingIntermediate_L": "MHBone_042",
    "Ring_Intermediate_L": "MHBone_042",
    "LeftRingIntermediate": "MHBone_042",
    "RingIntermediate.L": "MHBone_042",
    "RingFinger2_L": "MHBone_042",
    "Ring Intermediate.L": "MHBone_042",
    
    "RingDistal_L": "MHBone_043",
    "Ring_Distal_L": "MHBone_043",
    "LeftRingDistal": "MHBone_043",
    "RingDistal.L": "MHBone_043",
    "RingFinger3_L": "MHBone_043",
    "Ring Distal.L": "MHBone_043",
    
    # === 左手指 - 小指 ===
    "LittleProximal_L": "MHBone_044",
    "Little_Proximal_L": "MHBone_044",
    "LeftLittleProximal": "MHBone_044",
    "LittleProximal.L": "MHBone_044",
    "LittleFinger1_L": "MHBone_044",
    "Little Proximal.L": "MHBone_044",
    
    "LittleIntermediate_L": "MHBone_045",
    "Little_Intermediate_L": "MHBone_045",
    "LeftLittleIntermediate": "MHBone_045",
    "LittleIntermediate.L": "MHBone_045",
    "LittleFinger2_L": "MHBone_045",
    "Little Intermediate.L": "MHBone_045",
    
    "LittleDistal_L": "MHBone_046",
    "Little_Distal_L": "MHBone_046",
    "LeftLittleDistal": "MHBone_046",
    "LittleDistal.L": "MHBone_046",
    "LittleFinger3_L": "MHBone_046",
    "Little Distal.L": "MHBone_046",
    
    # === 右手指 - 拇指 ===
    "ThumbProximal_R": "MHBone_048",
    "Thumb_Proximal_R": "MHBone_048",
    "RightThumbProximal": "MHBone_048",
    "ThumbProximal.R": "MHBone_048",
    "Thumb1_R": "MHBone_048",
    "Thumb Proximal.R": "MHBone_048",
    
    "ThumbIntermediate_R": "MHBone_049",
    "Thumb_Intermediate_R": "MHBone_049",
    "RightThumbIntermediate": "MHBone_049",
    "ThumbIntermediate.R": "MHBone_049",
    "Thumb2_R": "MHBone_049",
    "Thumb Intermediate.R": "MHBone_049",
    
    "ThumbDistal_R": "MHBone_050",
    "Thumb_Distal_R": "MHBone_050",
    "RightThumbDistal": "MHBone_050",
    "ThumbDistal.R": "MHBone_050",
    "Thumb3_R": "MHBone_050",
    "Thumb Distal.R": "MHBone_050",
    
    # === 右手指 - 食指 ===
    "IndexProximal_R": "MHBone_051",
    "Index_Proximal_R": "MHBone_051",
    "RightIndexProximal": "MHBone_051",
    "IndexProximal.R": "MHBone_051",
    "IndexFinger1_R": "MHBone_051",
    "Index Proximal.R": "MHBone_051",
    
    "IndexIntermediate_R": "MHBone_052",
    "Index_Intermediate_R": "MHBone_052",
    "RightIndexIntermediate": "MHBone_052",
    "IndexIntermediate.R": "MHBone_052",
    "IndexFinger2_R": "MHBone_052",
    "Index Intermediate.R": "MHBone_052",
    
    "IndexDistal_R": "MHBone_053",
    "Index_Distal_R": "MHBone_053",
    "RightIndexDistal": "MHBone_053",
    "IndexDistal.R": "MHBone_053",
    "IndexFinger3_R": "MHBone_053",
    "Index Distal.R": "MHBone_053",
    
    # === 右手指 - 中指 ===
    "MiddleProximal_R": "MHBone_054",
    "Middle_Proximal_R": "MHBone_054",
    "RightMiddleProximal": "MHBone_054",
    "MiddleProximal.R": "MHBone_054",
    "MiddleFinger1_R": "MHBone_054",
    "Middle Proximal.R": "MHBone_054",
    
    "MiddleIntermediate_R": "MHBone_055",
    "Middle_Intermediate_R": "MHBone_055",
    "RightMiddleIntermediate": "MHBone_055",
    "MiddleIntermediate.R": "MHBone_055",
    "MiddleFinger2_R": "MHBone_055",
    "Middle Intermediate.R": "MHBone_055",
    
    "MiddleDistal_R": "MHBone_056",
    "Middle_Distal_R": "MHBone_056",
    "RightMiddleDistal": "MHBone_056",
    "MiddleDistal.R": "MHBone_056",
    "MiddleFinger3_R": "MHBone_056",
    "Middle Distal.R": "MHBone_056",
    
    # === 右手指 - 无名指 ===
    "RingProximal_R": "MHBone_058",
    "Ring_Proximal_R": "MHBone_058",
    "RightRingProximal": "MHBone_058",
    "RingProximal.R": "MHBone_058",
    "RingFinger1_R": "MHBone_058",
    "Ring Proximal.R": "MHBone_058",
    
    "RingIntermediate_R": "MHBone_059",
    "Ring_Intermediate_R": "MHBone_059",
    "RightRingIntermediate": "MHBone_059",
    "RingIntermediate.R": "MHBone_059",
    "RingFinger2_R": "MHBone_059",
    "Ring Intermediate.R": "MHBone_059",
    
    "RingDistal_R": "MHBone_060",
    "Ring_Distal_R": "MHBone_060",
    "RightRingDistal": "MHBone_060",
    "RingDistal.R": "MHBone_060",
    "RingFinger3_R": "MHBone_060",
    "Ring Distal.R": "MHBone_060",
    
    # === 右手指 - 小指 ===
    "LittleProximal_R": "MHBone_061",
    "Little_Proximal_R": "MHBone_061",
    "RightLittleProximal": "MHBone_061",
    "LittleProximal.R": "MHBone_061",
    "LittleFinger1_R": "MHBone_061",
    "Little Proximal.R": "MHBone_061",
    
    "LittleIntermediate_R": "MHBone_062",
    "Little_Intermediate_R": "MHBone_062",
    "RightLittleIntermediate": "MHBone_062",
    "LittleIntermediate.R": "MHBone_062",
    "LittleFinger2_R": "MHBone_062",
    "Little Intermediate.R": "MHBone_062",
    
    "LittleDistal_R": "MHBone_063",
    "Little_Distal_R": "MHBone_063",
    "RightLittleDistal": "MHBone_063",
    "LittleDistal.R": "MHBone_063",
    "LittleFinger3_R": "MHBone_063",
    "Little Distal.R": "MHBone_063",
    
    # === 辅助骨骼 ===
    "LowerArm_twist_L": "MHBone_081",
    "LowerArm_Twist_L": "MHBone_081",
    "LowerArm_twist_R": "MHBone_083",
    "LowerArm_Twist_R": "MHBone_083",
    
    "Hips_L": "MHBone_074",
    "Hips_R": "MHBone_076",
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