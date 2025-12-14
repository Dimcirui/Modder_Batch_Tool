import bpy

# UMA -> MHWorld 顶点组映射
_NAME_MAP = {
    # 躯干
    "Waist": "MHBone_001",
    "Spine": "MHBone_002",
    "Neck": "MHBone_003",
    "Head": "MHBone_004",
    "Hip": "MHBone_013",
    
    # 左臂
    "Shoulder_L": "MHBone_005",
    "Arm_L": "MHBone_006",
    "Elbow_L": "MHBone_007",
    "Wrist_L": "MHBone_008",
    "ShoulderRoll_L": "MHBone_080",
    "ArmRoll_L": "MHBone_081",
    
    # 右臂
    "Shoulder_R": "MHBone_009",
    "Arm_R": "MHBone_010",
    "Elbow_R": "MHBone_011",
    "Wrist_R": "MHBone_012",
    "ShoulderRoll_R": "MHBone_082",
    "ArmRoll_R": "MHBone_083",
    
    # 左腿
    "Thigh_L": "MHBone_014",
    "Knee_L": "MHBone_015",
    "Ankle_offset_L": "MHBone_016",
    "Toe_offset_L": "MHBone_017",
    
    # 右腿
    "Thigh_R": "MHBone_018",
    "Knee_R": "MHBone_019",
    "Ankle_offset_R": "MHBone_020",
    "Toe_offset_R": "MHBone_021",
    
    # 左手指
    "Thumb_01_L": "MHBone_031",
    "Thumb_02_L": "MHBone_032",
    "Thumb_03_L": "MHBone_033",
    "Index_01_L": "MHBone_034",
    "Index_02_L": "MHBone_035",
    "Index_03_L": "MHBone_036",
    "Middle_01_L": "MHBone_037",
    "Middle_02_L": "MHBone_038",
    "Middle_03_L": "MHBone_039",
    "Ring_01_L": "MHBone_041",
    "Ring_02_L": "MHBone_042",
    "Ring_03_L": "MHBone_043",
    "Pinky_01_L": "MHBone_044",
    "Pinky_02_L": "MHBone_045",
    "Pinky_03_L": "MHBone_046",
    
    # 右手指
    "Thumb_01_R": "MHBone_048",
    "Thumb_02_R": "MHBone_049",
    "Thumb_03_R": "MHBone_050",
    "Index_01_R": "MHBone_051",
    "Index_02_R": "MHBone_052",
    "Index_03_R": "MHBone_053",
    "Middle_01_R": "MHBone_054",
    "Middle_02_R": "MHBone_055",
    "Middle_03_R": "MHBone_056",
    "Ring_01_R": "MHBone_058",
    "Ring_02_R": "MHBone_059",
    "Ring_03_R": "MHBone_060",
    "Pinky_01_R": "MHBone_061",
    "Pinky_02_R": "MHBone_062",
    "Pinky_03_R": "MHBone_063",
    
    # 特殊骨骼
    "Sp_Ch_Bust0_L_01": "L_Oupai_00",
    "Sp_Ch_Bust0_R_01": "R_Oupai_00",
    "null1": "L_Arm_00_W",
    "null2": "L_Arm_01_W",
    "null3": "R_Arm_00_W",
    "null4": "R_Arm_01_W",
    "null5": "L_Leg_00_W",
    "null6": "L_Leg_01_W",
    "null7": "R_Leg_00_W",
    "null8": "R_Leg_01_W",
}


class MHW_OT_UMAtoMHW(bpy.types.Operator):
    """Convert UMA vertex groups to MHWorld format"""
    bl_idname = "mhw.uma_to_mhw"
    bl_label = "UMA to MHWorld"
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
    MHW_OT_UMAtoMHW,
]