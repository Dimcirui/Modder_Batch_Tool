import bpy

# UMA -> MHRise 映射
_NAME_MAP = {
    # 躯干
    "Waist": "Spine_00",
    "Spine": "Spine_01",
    "Neck": "Neck_00",
    "Head": "Head_00",
    "Hip": "Waist_00",
    
    # 左臂
    "Shoulder_L": "L_Arm_00",
    "Arm_L": "L_Arm_01",
    "Elbow_L": "L_Arm_02",
    "Wrist_L": "L_Arm_03",
    "ShoulderRoll_L": "L_Arm_01_T",
    "ArmRoll_L": "L_Arm_02_T",
    
    # 右臂
    "Shoulder_R": "R_Arm_00",
    "Arm_R": "R_Arm_01",
    "Elbow_R": "R_Arm_02",
    "Wrist_R": "R_Arm_03",
    "ShoulderRoll_R": "R_Arm_01_T",
    "ArmRoll_R": "R_Arm_02_T",
    
    # 左腿
    "Thigh_L": "L_Leg_00",
    "Knee_L": "L_Leg_01",
    "Ankle_offset_L": "L_Leg_02",
    "Toe_offset_L": "L_Leg_03",
    
    # 右腿
    "Thigh_R": "R_Leg_00",
    "Knee_R": "R_Leg_01",
    "Ankle_offset_R": "R_Leg_02",
    "Toe_offset_R": "R_Leg_03",
    
    # 左手指
    "Thumb_01_L": "L_Finger_00",
    "Thumb_02_L": "L_Finger_01",
    "Thumb_03_L": "L_Finger_02",
    "Index_01_L": "L_Finger_03",
    "Index_02_L": "L_Finger_04",
    "Index_03_L": "L_Finger_05",
    "Middle_01_L": "L_Finger_06",
    "Middle_02_L": "L_Finger_07",
    "Middle_03_L": "L_Finger_08",
    "Ring_01_L": "L_Finger_10",
    "Ring_02_L": "L_Finger_11",
    "Ring_03_L": "L_Finger_12",
    "Pinky_01_L": "L_Finger_13",
    "Pinky_02_L": "L_Finger_14",
    "Pinky_03_L": "L_Finger_15",
    
    # 右手指
    "Thumb_01_R": "R_Finger_00",
    "Thumb_02_R": "R_Finger_01",
    "Thumb_03_R": "R_Finger_02",
    "Index_01_R": "R_Finger_03",
    "Index_02_R": "R_Finger_04",
    "Index_03_R": "R_Finger_05",
    "Middle_01_R": "R_Finger_06",
    "Middle_02_R": "R_Finger_07",
    "Middle_03_R": "R_Finger_08",
    "Ring_01_R": "R_Finger_09",
    "Ring_02_R": "R_Finger_10",
    "Ring_03_R": "R_Finger_11",
    "Pinky_01_R": "R_Finger_12",
    "Pinky_02_R": "R_Finger_13",
    "Pinky_03_R": "R_Finger_14",
    
    # 特殊骨骼
    "Sp_Ch_Bust0_L_01": "L_Oupai_00",
    "Sp_Ch_Bust0_R_01": "R_Oupai_00",
    "MHBone070": "L_Arm_00_W",
    "MHBone071": "L_Arm_01_W",
    "MHBone072": "R_Arm_00_W",
    "MHBone073": "R_Arm_01_W",
    "MHBone074": "L_Leg_00_W",
    "MHBone075": "L_Leg_01_W",
    "MHBone076": "R_Leg_00_W",
    "MHBone077": "R_Leg_01_W",
}


class MHR_OT_UMAtoMHR(bpy.types.Operator):
    """Convert UMA vertex groups to MHRise format"""
    bl_idname = "mhr.uma_to_mhr"
    bl_label = "UMA to MHRise"
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
    MHR_OT_UMAtoMHR,
]