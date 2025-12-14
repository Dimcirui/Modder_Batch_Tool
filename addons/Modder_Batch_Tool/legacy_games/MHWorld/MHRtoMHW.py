import bpy

# MHRise -> MHWorld 顶点组名称映射
_NAME_MAP = {
    # 躯干
    "Waist_00": "MhBone_013",
    "Spine_00": "MhBone_001",
    "Spine_01": "MhBone_002",
    "Neck_00": "MhBone_003",
    "Head_00": "MhBone_004",
    "Neck_00_S": "MhBone_254",
    
    # 手臂
    "L_Arm_00": "MhBone_005",
    "L_Arm_01": "MhBone_006",
    "L_Arm_02": "MhBone_007",
    "L_Arm_03": "MhBone_008",
    "R_Arm_00": "MhBone_009",
    "R_Arm_01": "MhBone_010",
    "R_Arm_02": "MhBone_011",
    "R_Arm_03": "MhBone_012",
    
    # 腿部
    "L_Leg_00": "MhBone_014",
    "L_Leg_01": "MhBone_015",
    "L_Leg_02": "MhBone_016",
    "L_Leg_03": "MhBone_017",
    "R_Leg_00": "MhBone_018",
    "R_Leg_01": "MhBone_019",
    "R_Leg_02": "MhBone_020",
    "R_Leg_03": "MhBone_021",
    
    # 左手指
    "L_Finger_00": "MhBone_031",
    "L_Finger_01": "MhBone_032",
    "L_Finger_02": "MhBone_033",
    "L_Finger_03": "MhBone_034",
    "L_Finger_04": "MhBone_035",
    "L_Finger_05": "MhBone_036",
    "L_Finger_06": "MhBone_037",
    "L_Finger_07": "MhBone_038",
    "L_Finger_08": "MhBone_039",
    "L_Finger_09": "MhBone_040",
    "L_Finger_10": "MhBone_041",
    "L_Finger_11": "MhBone_042",
    "L_Finger_12": "MhBone_043",
    "L_Finger_13": "MhBone_044",
    "L_Finger_14": "MhBone_045",
    "L_Finger_15": "MhBone_046",
    
    # 右手指
    "R_Finger_00": "MhBone_048",
    "R_Finger_01": "MhBone_049",
    "R_Finger_02": "MhBone_050",
    "R_Finger_03": "MhBone_051",
    "R_Finger_04": "MhBone_052",
    "R_Finger_05": "MhBone_053",
    "R_Finger_06": "MhBone_054",
    "R_Finger_07": "MhBone_055",
    "R_Finger_08": "MhBone_056",
    "R_Grip_00": "MhBone_057",
    "R_Finger_09": "MhBone_058",
    "R_Finger_10": "MhBone_059",
    "R_Finger_11": "MhBone_060",
    "R_Finger_12": "MhBone_061",
    "R_Finger_13": "MhBone_062",
    "R_Finger_14": "MhBone_063",
    
    # 扭转骨
    "L_Arm_00_W": "MhBone_070",
    "L_Arm_01_W": "MhBone_071",
    "R_Arm_00_W": "MhBone_072",
    "R_Arm_01_W": "MhBone_073",
    "L_Leg_00_W": "MhBone_074",
    "L_Leg_01_W": "MhBone_075",
    "R_Leg_00_W": "MhBone_076",
    "R_Leg_01_W": "MhBone_077",
    "L_Arm_01_T": "MhBone_080",
    "L_Arm_02_T": "MhBone_081",
    "R_Arm_01_T": "MhBone_082",
    "R_Arm_02_T": "MhBone_083",
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