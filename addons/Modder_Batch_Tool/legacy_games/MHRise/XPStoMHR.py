import bpy

# XPS/MMD 日文 -> MHRise 映射
_NAME_MAP = {
    # 躯干
    "下半身": "Waist_00",
    "上半身": "Spine_00",
    "上半身2": "Spine_01",
    "首": "Neck_00",
    "頭": "Head_00",
    
    # 胸部
    "胸２.L": "L_Oupai_00",
    "胸２.R": "R_Oupai_00",
    
    # 左臂
    "肩.L": "L_Arm_00",
    "腕.L": "L_Arm_01",
    "ひじ.L": "L_Arm_02",
    "手首.L": "L_Arm_03",
    "親指０.L": "L_Finger_00",
    "親指１.L": "L_Finger_01",
    "親指２.L": "L_Finger_02",
    "人指１.L": "L_Finger_03",
    "人指２.L": "L_Finger_04",
    "人指３.L": "L_Finger_05",
    "中指１.L": "L_Finger_06",
    "中指２.L": "L_Finger_07",
    "中指３.L": "L_Finger_08",
    "自定义L": "L_Finger_09",
    "薬指１.L": "L_Finger_10",
    "薬指２.L": "L_Finger_11",
    "薬指３.L": "L_Finger_12",
    "小指１.L": "L_Finger_13",
    "小指２.L": "L_Finger_14",
    "小指３.L": "L_Finger_15",
    
    # 右臂
    "肩.R": "R_Arm_00",
    "腕.R": "R_Arm_01",
    "ひじ.R": "R_Arm_02",
    "手首.R": "R_Arm_03",
    "親指０.R": "R_Finger_00",
    "親指１.R": "R_Finger_01",
    "親指２.R": "R_Finger_02",
    "人指１.R": "R_Finger_03",
    "人指２.R": "R_Finger_04",
    "人指３.R": "R_Finger_05",
    "中指１.R": "R_Finger_06",
    "中指２.R": "R_Finger_07",
    "中指３.R": "R_Finger_08",
    "自定义R": "R_Grip_00",
    "薬指１.R": "R_Finger_09",
    "薬指２.R": "R_Finger_10",
    "薬指３.R": "R_Finger_11",
    "小指１.R": "R_Finger_12",
    "小指２.R": "R_Finger_13",
    "小指３.R": "R_Finger_14",
    
    # 腿部
    "足D.L": "L_Leg_00",
    "ひざD.L": "L_Leg_01",
    "足首D.L": "L_Leg_02",
    "足先EX.L": "L_Leg_03",
    "足D.R": "R_Leg_00",
    "ひざD.R": "R_Leg_01",
    "足首D.R": "R_Leg_02",
    "足先EX.R": "R_Leg_03",
    
    # 辅助骨骼
    "自定义1": "L_Arm_00_W",
    "自定义2": "L_Arm_01_W",
    "自定义3": "L_Arm_01_T",
    "自定义4": "L_Arm_02_T",
    "自定义5": "R_Arm_00_W",
    "自定义6": "R_Arm_01_W",
    "自定义7": "R_Arm_01_T",
    "自定义8": "R_Arm_02_T",
    "自定义9": "L_Leg_00_W",
    "自定义10": "L_Leg_01_W",
    "自定义11": "L_Leg_02_T",
    "自定义12": "R_Leg_00_W",
    "自定义13": "R_Leg_01_W",
    "自定义14": "R_Leg_02_T",
}


class MHR_OT_XPStoMHR(bpy.types.Operator):
    """Convert XPS vertex groups to MHRise format"""
    bl_idname = "mhr.xps_to_mhr"
    bl_label = "XPS to MHRise"
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
    MHR_OT_XPStoMHR,
]