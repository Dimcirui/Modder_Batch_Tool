import bpy

# MHWorld MhBone -> MHRise 映射
_NAME_MAP = {
    # 躯干
    "MhBone_013": "Waist_00",
    "MhBone_001": "Spine_00",
    "MhBone_002": "Spine_01",
    "MhBone_003": "Neck_00",
    "MhBone_004": "Head_00",
    "MhBone_254": "Neck_00_S",
    
    # 左臂
    "MhBone_005": "L_Arm_00",
    "MhBone_006": "L_Arm_01",
    "MhBone_007": "L_Arm_02",
    "MhBone_008": "L_Arm_03",
    
    # 右臂
    "MhBone_009": "R_Arm_00",
    "MhBone_010": "R_Arm_01",
    "MhBone_011": "R_Arm_02",
    "MhBone_012": "R_Arm_03",
    
    # 左腿
    "MhBone_014": "L_Leg_00",
    "MhBone_015": "L_Leg_01",
    "MhBone_016": "L_Leg_02",
    "MhBone_017": "L_Leg_03",
    
    # 右腿
    "MhBone_018": "R_Leg_00",
    "MhBone_019": "R_Leg_01",
    "MhBone_020": "R_Leg_02",
    "MhBone_021": "R_Leg_03",
    
    # 左手指
    "MhBone_031": "L_Finger_00",
    "MhBone_032": "L_Finger_01",
    "MhBone_033": "L_Finger_02",
    "MhBone_034": "L_Finger_03",
    "MhBone_035": "L_Finger_04",
    "MhBone_036": "L_Finger_05",
    "MhBone_037": "L_Finger_06",
    "MhBone_038": "L_Finger_07",
    "MhBone_039": "L_Finger_08",
    "MhBone_040": "L_Finger_09",
    "MhBone_041": "L_Finger_10",
    "MhBone_042": "L_Finger_11",
    "MhBone_043": "L_Finger_12",
    "MhBone_044": "L_Finger_13",
    "MhBone_045": "L_Finger_14",
    "MhBone_046": "L_Finger_15",
    
    # 右手指
    "MhBone_048": "R_Finger_00",
    "MhBone_049": "R_Finger_01",
    "MhBone_050": "R_Finger_02",
    "MhBone_051": "R_Finger_03",
    "MhBone_052": "R_Finger_04",
    "MhBone_053": "R_Finger_05",
    "MhBone_054": "R_Finger_06",
    "MhBone_055": "R_Finger_07",
    "MhBone_056": "R_Finger_08",
    "MhBone_057": "R_Grip_00",
    "MhBone_058": "R_Finger_09",
    "MhBone_059": "R_Finger_10",
    "MhBone_060": "R_Finger_11",
    "MhBone_061": "R_Finger_12",
    "MhBone_062": "R_Finger_13",
    "MhBone_063": "R_Finger_14",
    
    # 辅助骨骼
    "MhBone_070": "L_Arm_00_W",
    "MhBone_071": "L_Arm_01_W",
    "MhBone_072": "R_Arm_00_W",
    "MhBone_073": "R_Arm_01_W",
    "MhBone_074": "L_Leg_00_W",
    "MhBone_075": "L_Leg_01_W",
    "MhBone_076": "R_Leg_00_W",
    "MhBone_077": "R_Leg_01_W",
    "MhBone_080": "L_Arm_01_T",
    "MhBone_081": "L_Arm_02_T",
    "MhBone_082": "R_Arm_01_T",
    "MhBone_083": "R_Arm_02_T",
}


class MHR_OT_MHWtoMHR(bpy.types.Operator):
    """Convert MHWorld vertex groups to MHRise format"""
    bl_idname = "mhr.mhw_to_mhr"
    bl_label = "MHWorld to MHRise"
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
    MHR_OT_MHWtoMHR,
]