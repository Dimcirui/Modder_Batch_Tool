import bpy

# VRCHAT/通用人形骨骼 -> MHWorld 顶点组映射
# 支持多种命名变体 (下划线、点号、空格等)
_NAME_MAP = {
    # 躯干
    "Hips": "MhBone_013",
    "Spine": "MhBone_001",
    "Chest": "MhBone_002",
    "Neck": "MhBone_003",
    "Head": "MhBone_004",
    
    # === 左臂 ===
    "Shoulder_L": "MhBone_005",
    "Left shoulder": "MhBone_005",
    "Shoulder.L": "MhBone_005",
    
    "UpperArm_L": "MhBone_006",
    "Left arm": "MhBone_006",
    "LeftUpperArm": "MhBone_006",
    "UpperArm.L": "MhBone_006",
    "Upper_arm.L": "MhBone_006",
    
    "LowerArm_L": "MhBone_007",
    "Left elbow": "MhBone_007",
    "LeftLowerArm": "MhBone_007",
    "LowerArm.L": "MhBone_007",
    "Lower_arm.L": "MhBone_007",
    
    "Hand_L": "MhBone_008",
    "Left wrist": "MhBone_008",
    "Hand.L": "MhBone_008",
    
    # === 右臂 ===
    "Shoulder_R": "MhBone_009",
    "Right shoulder": "MhBone_009",
    "Shoulder.R": "MhBone_009",
    
    "UpperArm_R": "MhBone_010",
    "Right arm": "MhBone_010",
    "RightUpperArm": "MhBone_010",
    "UpperArm.R": "MhBone_010",
    "Upper_arm.R": "MhBone_010",
    
    "LowerArm_R": "MhBone_011",
    "Right elbow": "MhBone_011",
    "RightLowerArm": "MhBone_011",
    "LowerArm.R": "MhBone_011",
    "Lower_arm.R": "MhBone_011",
    
    "Hand_R": "MhBone_012",
    "Right wrist": "MhBone_012",
    "Hand.R": "MhBone_012",
    
    # === 左腿 ===
    "UpperLeg_L": "MhBone_014",
    "Left leg": "MhBone_014",
    "LeftUpperLeg": "MhBone_014",
    "UpperLeg.L": "MhBone_014",
    "Upper_leg.L": "MhBone_014",
    
    "LowerLeg_L": "MhBone_015",
    "Left knee": "MhBone_015",
    "LeftLowerLeg": "MhBone_015",
    "LowerLeg.L": "MhBone_015",
    "Lower_leg.L": "MhBone_015",
    
    "Foot_L": "MhBone_016",
    "Left ankle": "MhBone_016",
    "Foot.L": "MhBone_016",
    
    "Toe_L": "MhBone_017",
    "Left toe": "MhBone_017",
    "Toe.L": "MhBone_017",
    
    # === 右腿 ===
    "UpperLeg_R": "MhBone_018",
    "Right leg": "MhBone_018",
    "RightUpperLeg": "MhBone_018",
    "UpperLeg.R": "MhBone_018",
    "Upper_leg.R": "MhBone_018",
    
    "LowerLeg_R": "MhBone_019",
    "Right knee": "MhBone_019",
    "RightLowerLeg": "MhBone_019",
    "LowerLeg.R": "MhBone_019",
    "Lower_leg.R": "MhBone_019",
    
    "Foot_R": "MhBone_020",
    "Right ankle": "MhBone_020",
    "Foot.R": "MhBone_020",
    
    "Toe_R": "MhBone_021",
    "Right toe": "MhBone_021",
    "Toe.R": "MhBone_021",
    
    # === 左手指 - 拇指 ===
    "ThumbProximal_L": "MhBone_031",
    "Thumb_Proximal_L": "MhBone_031",
    "LeftThumbProximal": "MhBone_031",
    "ThumbProximal.L": "MhBone_031",
    "Thumb1_L": "MhBone_031",
    "Thumb Proximal.L": "MhBone_031",
    
    "ThumbIntermediate_L": "MhBone_032",
    "Thumb_Intermediate_L": "MhBone_032",
    "LeftThumbIntermediate": "MhBone_032",
    "ThumbIntermediate.L": "MhBone_032",
    "Thumb2_L": "MhBone_032",
    "Thumb Intermediate.L": "MhBone_032",
    
    "ThumbDistal_L": "MhBone_033",
    "Thumb_Distal_L": "MhBone_033",
    "LeftThumbDistal": "MhBone_033",
    "ThumbDistal.L": "MhBone_033",
    "Thumb3_L": "MhBone_033",
    "Thumb Distal.L": "MhBone_033",
    
    # === 左手指 - 食指 ===
    "IndexProximal_L": "MhBone_034",
    "Index_Proximal_L": "MhBone_034",
    "LeftIndexProximal": "MhBone_034",
    "IndexProximal.L": "MhBone_034",
    "IndexFinger1_L": "MhBone_034",
    "Index Proximal.L": "MhBone_034",
    
    "IndexIntermediate_L": "MhBone_035",
    "Index_Intermediate_L": "MhBone_035",
    "LeftIndexIntermediate": "MhBone_035",
    "IndexIntermediate.L": "MhBone_035",
    "IndexFinger2_L": "MhBone_035",
    "Index Intermediate.L": "MhBone_035",
    
    "IndexDistal_L": "MhBone_036",
    "Index_Distal_L": "MhBone_036",
    "LeftIndexDistal": "MhBone_036",
    "IndexDistal.L": "MhBone_036",
    "IndexFinger3_L": "MhBone_036",
    "Index Distal.L": "MhBone_036",
    
    # === 左手指 - 中指 ===
    "MiddleProximal_L": "MhBone_037",
    "Middle_Proximal_L": "MhBone_037",
    "LeftMiddleProximal": "MhBone_037",
    "MiddleProximal.L": "MhBone_037",
    "MiddleFinger1_L": "MhBone_037",
    "Middle Proximal.L": "MhBone_037",
    
    "MiddleIntermediate_L": "MhBone_038",
    "Middle_Intermediate_L": "MhBone_038",
    "LeftMiddleIntermediate": "MhBone_038",
    "MiddleIntermediate.L": "MhBone_038",
    "MiddleFinger2_L": "MhBone_038",
    "Middle Intermediate.L": "MhBone_038",
    
    "MiddleDistal_L": "MhBone_039",
    "Middle_Distal_L": "MhBone_039",
    "LeftMiddleDistal": "MhBone_039",
    "MiddleDistal.L": "MhBone_039",
    "MiddleFinger3_L": "MhBone_039",
    "Middle Distal.L": "MhBone_039",
    
    # === 左手指 - 无名指 ===
    "RingProximal_L": "MhBone_041",
    "Ring_Proximal_L": "MhBone_041",
    "LeftRingProximal": "MhBone_041",
    "RingProximal.L": "MhBone_041",
    "RingFinger1_L": "MhBone_041",
    "Ring Proximal.L": "MhBone_041",
    
    "RingIntermediate_L": "MhBone_042",
    "Ring_Intermediate_L": "MhBone_042",
    "LeftRingIntermediate": "MhBone_042",
    "RingIntermediate.L": "MhBone_042",
    "RingFinger2_L": "MhBone_042",
    "Ring Intermediate.L": "MhBone_042",
    
    "RingDistal_L": "MhBone_043",
    "Ring_Distal_L": "MhBone_043",
    "LeftRingDistal": "MhBone_043",
    "RingDistal.L": "MhBone_043",
    "RingFinger3_L": "MhBone_043",
    "Ring Distal.L": "MhBone_043",
    
    # === 左手指 - 小指 ===
    "LittleProximal_L": "MhBone_044",
    "Little_Proximal_L": "MhBone_044",
    "LeftLittleProximal": "MhBone_044",
    "LittleProximal.L": "MhBone_044",
    "LittleFinger1_L": "MhBone_044",
    "Little Proximal.L": "MhBone_044",
    
    "LittleIntermediate_L": "MhBone_045",
    "Little_Intermediate_L": "MhBone_045",
    "LeftLittleIntermediate": "MhBone_045",
    "LittleIntermediate.L": "MhBone_045",
    "LittleFinger2_L": "MhBone_045",
    "Little Intermediate.L": "MhBone_045",
    
    "LittleDistal_L": "MhBone_046",
    "Little_Distal_L": "MhBone_046",
    "LeftLittleDistal": "MhBone_046",
    "LittleDistal.L": "MhBone_046",
    "LittleFinger3_L": "MhBone_046",
    "Little Distal.L": "MhBone_046",
    
    # === 右手指 - 拇指 ===
    "ThumbProximal_R": "MhBone_048",
    "Thumb_Proximal_R": "MhBone_048",
    "RightThumbProximal": "MhBone_048",
    "ThumbProximal.R": "MhBone_048",
    "Thumb1_R": "MhBone_048",
    "Thumb Proximal.R": "MhBone_048",
    
    "ThumbIntermediate_R": "MhBone_049",
    "Thumb_Intermediate_R": "MhBone_049",
    "RightThumbIntermediate": "MhBone_049",
    "ThumbIntermediate.R": "MhBone_049",
    "Thumb2_R": "MhBone_049",
    "Thumb Intermediate.R": "MhBone_049",
    
    "ThumbDistal_R": "MhBone_050",
    "Thumb_Distal_R": "MhBone_050",
    "RightThumbDistal": "MhBone_050",
    "ThumbDistal.R": "MhBone_050",
    "Thumb3_R": "MhBone_050",
    "Thumb Distal.R": "MhBone_050",
    
    # === 右手指 - 食指 ===
    "IndexProximal_R": "MhBone_051",
    "Index_Proximal_R": "MhBone_051",
    "RightIndexProximal": "MhBone_051",
    "IndexProximal.R": "MhBone_051",
    "IndexFinger1_R": "MhBone_051",
    "Index Proximal.R": "MhBone_051",
    
    "IndexIntermediate_R": "MhBone_052",
    "Index_Intermediate_R": "MhBone_052",
    "RightIndexIntermediate": "MhBone_052",
    "IndexIntermediate.R": "MhBone_052",
    "IndexFinger2_R": "MhBone_052",
    "Index Intermediate.R": "MhBone_052",
    
    "IndexDistal_R": "MhBone_053",
    "Index_Distal_R": "MhBone_053",
    "RightIndexDistal": "MhBone_053",
    "IndexDistal.R": "MhBone_053",
    "IndexFinger3_R": "MhBone_053",
    "Index Distal.R": "MhBone_053",
    
    # === 右手指 - 中指 ===
    "MiddleProximal_R": "MhBone_054",
    "Middle_Proximal_R": "MhBone_054",
    "RightMiddleProximal": "MhBone_054",
    "MiddleProximal.R": "MhBone_054",
    "MiddleFinger1_R": "MhBone_054",
    "Middle Proximal.R": "MhBone_054",
    
    "MiddleIntermediate_R": "MhBone_055",
    "Middle_Intermediate_R": "MhBone_055",
    "RightMiddleIntermediate": "MhBone_055",
    "MiddleIntermediate.R": "MhBone_055",
    "MiddleFinger2_R": "MhBone_055",
    "Middle Intermediate.R": "MhBone_055",
    
    "MiddleDistal_R": "MhBone_056",
    "Middle_Distal_R": "MhBone_056",
    "RightMiddleDistal": "MhBone_056",
    "MiddleDistal.R": "MhBone_056",
    "MiddleFinger3_R": "MhBone_056",
    "Middle Distal.R": "MhBone_056",
    
    # === 右手指 - 无名指 ===
    "RingProximal_R": "MhBone_058",
    "Ring_Proximal_R": "MhBone_058",
    "RightRingProximal": "MhBone_058",
    "RingProximal.R": "MhBone_058",
    "RingFinger1_R": "MhBone_058",
    "Ring Proximal.R": "MhBone_058",
    
    "RingIntermediate_R": "MhBone_059",
    "Ring_Intermediate_R": "MhBone_059",
    "RightRingIntermediate": "MhBone_059",
    "RingIntermediate.R": "MhBone_059",
    "RingFinger2_R": "MhBone_059",
    "Ring Intermediate.R": "MhBone_059",
    
    "RingDistal_R": "MhBone_060",
    "Ring_Distal_R": "MhBone_060",
    "RightRingDistal": "MhBone_060",
    "RingDistal.R": "MhBone_060",
    "RingFinger3_R": "MhBone_060",
    "Ring Distal.R": "MhBone_060",
    
    # === 右手指 - 小指 ===
    "LittleProximal_R": "MhBone_061",
    "Little_Proximal_R": "MhBone_061",
    "RightLittleProximal": "MhBone_061",
    "LittleProximal.R": "MhBone_061",
    "LittleFinger1_R": "MhBone_061",
    "Little Proximal.R": "MhBone_061",
    
    "LittleIntermediate_R": "MhBone_062",
    "Little_Intermediate_R": "MhBone_062",
    "RightLittleIntermediate": "MhBone_062",
    "LittleIntermediate.R": "MhBone_062",
    "LittleFinger2_R": "MhBone_062",
    "Little Intermediate.R": "MhBone_062",
    
    "LittleDistal_R": "MhBone_063",
    "Little_Distal_R": "MhBone_063",
    "RightLittleDistal": "MhBone_063",
    "LittleDistal.R": "MhBone_063",
    "LittleFinger3_R": "MhBone_063",
    "Little Distal.R": "MhBone_063",
    
    # === 辅助骨骼 ===
    "LowerArm_twist_L": "MhBone_081",
    "LowerArm_Twist_L": "MhBone_081",
    "LowerArm_twist_R": "MhBone_083",
    "LowerArm_Twist_R": "MhBone_083",
    
    "Hips_L": "MhBone_074",
    "Hips_R": "MhBone_076",
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