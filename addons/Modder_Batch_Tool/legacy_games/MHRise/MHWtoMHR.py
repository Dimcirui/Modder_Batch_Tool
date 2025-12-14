import bpy

# MHWorld MHBone -> MHRise 映射
_NAME_MAP = {
    # 躯干
    "MHBone_013": "Waist_00",
    "MHBone_001": "Spine_00",
    "MHBone_002": "Spine_01",
    "MHBone_003": "Neck_00",
    "MHBone_004": "Head_00",
    "MHBone_254": "Neck_00_S",
    
    # 左臂
    "MHBone_005": "L_Arm_00",
    "MHBone_006": "L_Arm_01",
    "MHBone_007": "L_Arm_02",
    "MHBone_008": "L_Arm_03",
    
    # 右臂
    "MHBone_009": "R_Arm_00",
    "MHBone_010": "R_Arm_01",
    "MHBone_011": "R_Arm_02",
    "MHBone_012": "R_Arm_03",
    
    # 左腿
    "MHBone_014": "L_Leg_00",
    "MHBone_015": "L_Leg_01",
    "MHBone_016": "L_Leg_02",
    "MHBone_017": "L_Leg_03",
    
    # 右腿
    "MHBone_018": "R_Leg_00",
    "MHBone_019": "R_Leg_01",
    "MHBone_020": "R_Leg_02",
    "MHBone_021": "R_Leg_03",
    
    # 左手指
    "MHBone_031": "L_Finger_00",
    "MHBone_032": "L_Finger_01",
    "MHBone_033": "L_Finger_02",
    "MHBone_034": "L_Finger_03",
    "MHBone_035": "L_Finger_04",
    "MHBone_036": "L_Finger_05",
    "MHBone_037": "L_Finger_06",
    "MHBone_038": "L_Finger_07",
    "MHBone_039": "L_Finger_08",
    "MHBone_040": "L_Finger_09",
    "MHBone_041": "L_Finger_10",
    "MHBone_042": "L_Finger_11",
    "MHBone_043": "L_Finger_12",
    "MHBone_044": "L_Finger_13",
    "MHBone_045": "L_Finger_14",
    "MHBone_046": "L_Finger_15",
    
    # 右手指
    "MHBone_048": "R_Finger_00",
    "MHBone_049": "R_Finger_01",
    "MHBone_050": "R_Finger_02",
    "MHBone_051": "R_Finger_03",
    "MHBone_052": "R_Finger_04",
    "MHBone_053": "R_Finger_05",
    "MHBone_054": "R_Finger_06",
    "MHBone_055": "R_Finger_07",
    "MHBone_056": "R_Finger_08",
    "MHBone_057": "R_Grip_00",
    "MHBone_058": "R_Finger_09",
    "MHBone_059": "R_Finger_10",
    "MHBone_060": "R_Finger_11",
    "MHBone_061": "R_Finger_12",
    "MHBone_062": "R_Finger_13",
    "MHBone_063": "R_Finger_14",
    
    # 辅助骨骼
    "MHBone_070": "L_Arm_00_W",
    "MHBone_071": "L_Arm_01_W",
    "MHBone_072": "R_Arm_00_W",
    "MHBone_073": "R_Arm_01_W",
    "MHBone_074": "L_Leg_00_W",
    "MHBone_075": "L_Leg_01_W",
    "MHBone_076": "R_Leg_00_W",
    "MHBone_077": "R_Leg_01_W",
    "MHBone_080": "L_Arm_01_T",
    "MHBone_081": "L_Arm_02_T",
    "MHBone_082": "R_Arm_01_T",
    "MHBone_083": "R_Arm_02_T",
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