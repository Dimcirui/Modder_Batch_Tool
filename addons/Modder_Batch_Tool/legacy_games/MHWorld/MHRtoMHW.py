import bpy

# MHRise -> MHWorld 顶点组名称映射
_NAME_MAP = {
    # 躯干
    "Waist_00": "MHBone_013",
    "Spine_00": "MHBone_001",
    "Spine_01": "MHBone_002",
    "Neck_00": "MHBone_003",
    "Head_00": "MHBone_004",
    "Neck_00_S": "MHBone_254",
    
    # 手臂
    "L_Arm_00": "MHBone_005",
    "L_Arm_01": "MHBone_006",
    "L_Arm_02": "MHBone_007",
    "L_Arm_03": "MHBone_008",
    "R_Arm_00": "MHBone_009",
    "R_Arm_01": "MHBone_010",
    "R_Arm_02": "MHBone_011",
    "R_Arm_03": "MHBone_012",
    
    # 腿部
    "L_Leg_00": "MHBone_014",
    "L_Leg_01": "MHBone_015",
    "L_Leg_02": "MHBone_016",
    "L_Leg_03": "MHBone_017",
    "R_Leg_00": "MHBone_018",
    "R_Leg_01": "MHBone_019",
    "R_Leg_02": "MHBone_020",
    "R_Leg_03": "MHBone_021",
    
    # 左手指
    "L_Finger_00": "MHBone_031",
    "L_Finger_01": "MHBone_032",
    "L_Finger_02": "MHBone_033",
    "L_Finger_03": "MHBone_034",
    "L_Finger_04": "MHBone_035",
    "L_Finger_05": "MHBone_036",
    "L_Finger_06": "MHBone_037",
    "L_Finger_07": "MHBone_038",
    "L_Finger_08": "MHBone_039",
    "L_Finger_09": "MHBone_040",
    "L_Finger_10": "MHBone_041",
    "L_Finger_11": "MHBone_042",
    "L_Finger_12": "MHBone_043",
    "L_Finger_13": "MHBone_044",
    "L_Finger_14": "MHBone_045",
    "L_Finger_15": "MHBone_046",
    
    # 右手指
    "R_Finger_00": "MHBone_048",
    "R_Finger_01": "MHBone_049",
    "R_Finger_02": "MHBone_050",
    "R_Finger_03": "MHBone_051",
    "R_Finger_04": "MHBone_052",
    "R_Finger_05": "MHBone_053",
    "R_Finger_06": "MHBone_054",
    "R_Finger_07": "MHBone_055",
    "R_Finger_08": "MHBone_056",
    "R_Grip_00": "MHBone_057",
    "R_Finger_09": "MHBone_058",
    "R_Finger_10": "MHBone_059",
    "R_Finger_11": "MHBone_060",
    "R_Finger_12": "MHBone_061",
    "R_Finger_13": "MHBone_062",
    "R_Finger_14": "MHBone_063",
    
    # 扭转骨
    "L_Arm_00_W": "MHBone_070",
    "L_Arm_01_W": "MHBone_071",
    "R_Arm_00_W": "MHBone_072",
    "R_Arm_01_W": "MHBone_073",
    "L_Leg_00_W": "MHBone_074",
    "L_Leg_01_W": "MHBone_075",
    "R_Leg_00_W": "MHBone_076",
    "R_Leg_01_W": "MHBone_077",
    "L_Arm_01_T": "MHBone_080",
    "L_Arm_02_T": "MHBone_081",
    "R_Arm_01_T": "MHBone_082",
    "R_Arm_02_T": "MHBone_083",
}


def _rename_vertex_groups(obj, name_map):
    """重命名顶点组"""
    vgroups = obj.vertex_groups
    for old_name, new_name in name_map.items():
        if old_name in vgroups:
            vgroups[old_name].name = new_name


class MHW_OT_MHRtoMHW(bpy.types.Operator):
    """Convert MHRise vertex groups to MHWorld format"""
    bl_idname = "mhw.mhr_to_mhw"
    bl_label = "MHRise to MHWorld"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == "MESH" for obj in context.selected_objects)

    def execute(self, context):
        count = 0
        for obj in context.selected_objects:
            if obj.type == "MESH":
                _rename_vertex_groups(obj, _NAME_MAP)
                count += 1
        
        self.report({'INFO'}, f"Converted {count} mesh(es)")
        return {'FINISHED'}


classes = [
    MHW_OT_MHRtoMHW,
]