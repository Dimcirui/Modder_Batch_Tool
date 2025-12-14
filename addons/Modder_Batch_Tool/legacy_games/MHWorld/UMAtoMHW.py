import bpy

# UMA -> MHWorld 顶点组映射
_NAME_MAP = {
    # 躯干
    "Waist": "MhBone_001",
    "Spine": "MhBone_002",
    "Neck": "MhBone_003",
    "Head": "MhBone_004",
    "Hip": "MhBone_013",
    
    # 左臂
    "Shoulder_L": "MhBone_005",
    "Arm_L": "MhBone_006",
    "Elbow_L": "MhBone_007",
    "Wrist_L": "MhBone_008",
    "ShoulderRoll_L": "MhBone_080",
    "ArmRoll_L": "MhBone_081",
    
    # 右臂
    "Shoulder_R": "MhBone_009",
    "Arm_R": "MhBone_010",
    "Elbow_R": "MhBone_011",
    "Wrist_R": "MhBone_012",
    "ShoulderRoll_R": "MhBone_082",
    "ArmRoll_R": "MhBone_083",
    
    # 左腿
    "Thigh_L": "MhBone_014",
    "Knee_L": "MhBone_015",
    "Ankle_offset_L": "MhBone_016",
    "Toe_offset_L": "MhBone_017",
    
    # 右腿
    "Thigh_R": "MhBone_018",
    "Knee_R": "MhBone_019",
    "Ankle_offset_R": "MhBone_020",
    "Toe_offset_R": "MhBone_021",
    
    # 左手指
    "Thumb_01_L": "MhBone_031",
    "Thumb_02_L": "MhBone_032",
    "Thumb_03_L": "MhBone_033",
    "Index_01_L": "MhBone_034",
    "Index_02_L": "MhBone_035",
    "Index_03_L": "MhBone_036",
    "Middle_01_L": "MhBone_037",
    "Middle_02_L": "MhBone_038",
    "Middle_03_L": "MhBone_039",
    "Ring_01_L": "MhBone_041",
    "Ring_02_L": "MhBone_042",
    "Ring_03_L": "MhBone_043",
    "Pinky_01_L": "MhBone_044",
    "Pinky_02_L": "MhBone_045",
    "Pinky_03_L": "MhBone_046",
    
    # 右手指
    "Thumb_01_R": "MhBone_048",
    "Thumb_02_R": "MhBone_049",
    "Thumb_03_R": "MhBone_050",
    "Index_01_R": "MhBone_051",
    "Index_02_R": "MhBone_052",
    "Index_03_R": "MhBone_053",
    "Middle_01_R": "MhBone_054",
    "Middle_02_R": "MhBone_055",
    "Middle_03_R": "MhBone_056",
    "Ring_01_R": "MhBone_058",
    "Ring_02_R": "MhBone_059",
    "Ring_03_R": "MhBone_060",
    "Pinky_01_R": "MhBone_061",
    "Pinky_02_R": "MhBone_062",
    "Pinky_03_R": "MhBone_063",
    
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