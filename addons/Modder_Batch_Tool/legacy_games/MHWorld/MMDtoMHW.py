import bpy

# MMD 日文骨骼名 -> MHWorld MHBone
_MMD_UNFIXED_MAP = {
    # 躯干
    "下半身": "MHBone_013",
    "上半身": "MHBone_001",
    "上半身2": "MHBone_002",
    "首": "MHBone_003",
    "頭": "MHBone_004",
    
    # 左臂
    "肩.L": "MHBone_005",
    "腕.L": "MHBone_006",
    "ひじ.L": "MHBone_007",
    "手首.L": "MHBone_008",
    "親指０.L": "MHBone_031",
    "親指１.L": "MHBone_032",
    "親指２.L": "MHBone_033",
    "人指１.L": "MHBone_034",
    "人指２.L": "MHBone_035",
    "人指３.L": "MHBone_036",
    "中指１.L": "MHBone_037",
    "中指２.L": "MHBone_038",
    "中指３.L": "MHBone_039",
    "自定义L": "MHBone_040",
    "薬指１.L": "MHBone_041",
    "薬指２.L": "MHBone_042",
    "薬指３.L": "MHBone_043",
    "小指１.L": "MHBone_044",
    "小指２.L": "MHBone_045",
    "小指３.L": "MHBone_046",
    
    # 右臂
    "肩.R": "MHBone_009",
    "腕.R": "MHBone_010",
    "ひじ.R": "MHBone_011",
    "手首.R": "MHBone_012",
    "親指０.R": "MHBone_048",
    "親指１.R": "MHBone_049",
    "親指２.R": "MHBone_050",
    "人指１.R": "MHBone_051",
    "人指２.R": "MHBone_052",
    "人指３.R": "MHBone_053",
    "中指１.R": "MHBone_054",
    "中指２.R": "MHBone_055",
    "中指３.R": "MHBone_056",
    "自定义R": "MHBone_057",
    "薬指１.R": "MHBone_058",
    "薬指２.R": "MHBone_059",
    "薬指３.R": "MHBone_060",
    "小指１.R": "MHBone_061",
    "小指２.R": "MHBone_062",
    "小指３.R": "MHBone_063",
    
    # 左腿
    "足D.L": "MHBone_014",
    "ひざD.L": "MHBone_015",
    "足首D.L": "MHBone_016",
    "足先EX.L": "MHBone_017",
    
    # 右腿
    "足D.R": "MHBone_018",
    "ひざD.R": "MHBone_019",
    "足首D.R": "MHBone_020",
    "足先EX.R": "MHBone_021",
    
    # 辅助骨骼
    "自定义1": "MHBone_070",
    "+ひじ補助.L": "MHBone_071",
    "ひじ補助.L": "MHBone_071",
    "自定义3": "MHBone_080",
    "自定义4": "MHBone_081",
    "自定义5": "MHBone_072",
    "+ひじ補助.R": "MHBone_073",
    "ひじ補助.R": "MHBone_073",
    "自定义7": "MHBone_082",
    "自定义8": "MHBone_083",
    "お尻.L": "MHBone_074",
    "+ひざ補助.L": "MHBone_075",
    "ひざ補助.L": "MHBone_075",
    "自定义11": "MHBone_084",
    "お尻.R": "MHBone_076",
    "+ひざ補助.R": "MHBone_077",
    "ひざ補助.R": "MHBone_077",
    "自定义14": "MHBone_085",
}

# MMD 英文骨骼名 -> MHWorld MHBone
_MMD_FIXED_MAP = {
    # 躯干
    "Hips": "MHBone_013",
    "Spine": "MHBone_001",
    "Chest": "MHBone_002",
    "Neck": "MHBone_003",
    "Head": "MHBone_004",
    
    # 左臂
    "Left shoulder": "MHBone_005",
    "zArmTwist_L": "MHBone_006",
    "Left elbow": "MHBone_007",
    "Left wrist": "MHBone_008",
    "Thumb0_L": "MHBone_031",
    "Thumb1_L": "MHBone_032",
    "Thumb2_L": "MHBone_033",
    "IndexFinger1_L": "MHBone_034",
    "IndexFinger2_L": "MHBone_035",
    "IndexFinger3_L": "MHBone_036",
    "MiddleFinger1_L": "MHBone_037",
    "MiddleFinger2_L": "MHBone_038",
    "MiddleFinger3_L": "MHBone_039",
    "自定义L": "MHBone_040",
    "RingFinger1_L": "MHBone_041",
    "RingFinger2_L": "MHBone_042",
    "RingFinger3_L": "MHBone_043",
    "LittleFinger1_L": "MHBone_044",
    "LittleFinger2_L": "MHBone_045",
    "LittleFinger3_L": "MHBone_046",
    
    # 右臂
    "Right shoulder": "MHBone_009",
    "zArmTwist_R": "MHBone_010",
    "Right elbow": "MHBone_011",
    "Right wrist": "MHBone_012",
    "Thumb0_R": "MHBone_048",
    "Thumb1_R": "MHBone_049",
    "Thumb2_R": "MHBone_050",
    "IndexFinger1_R": "MHBone_051",
    "IndexFinger2_R": "MHBone_052",
    "IndexFinger3_R": "MHBone_053",
    "MiddleFinger1_R": "MHBone_054",
    "MiddleFinger2_R": "MHBone_055",
    "MiddleFinger3_R": "MHBone_056",
    "自定义R": "MHBone_057",
    "RingFinger1_R": "MHBone_058",
    "RingFinger2_R": "MHBone_059",
    "RingFinger3_R": "MHBone_060",
    "LittleFinger1_R": "MHBone_061",
    "LittleFinger2_R": "MHBone_062",
    "LittleFinger3_R": "MHBone_063",
    
    # 左腿
    "Left leg": "MHBone_014",
    "Left knee": "MHBone_015",
    "Left ankle": "MHBone_016",
    "Left toe": "MHBone_017",
    
    # 右腿
    "Right leg": "MHBone_018",
    "Right knee": "MHBone_019",
    "Right ankle": "MHBone_020",
    "Right toe": "MHBone_021",
    
    # 辅助骨骼
    "自定义1": "MHBone_070",
    "+ElbowAux_L": "MHBone_071",
    "ElbowAux_L": "MHBone_071",
    "Left arm": "MHBone_080",
    "zHandTwist_L": "MHBone_081",
    "自定义5": "MHBone_072",
    "+ElbowAux_R": "MHBone_073",
    "ElbowAux_R": "MHBone_073",
    "Right arm": "MHBone_082",
    "zHandTwist_R": "MHBone_083",
    "OhButt_L": "MHBone_074",
    "+KneeAux_L": "MHBone_075",
    "KneeAux_L": "MHBone_075",
    "自定义11": "MHBone_084",
    "OhButt_R": "MHBone_076",
    "+KneeAux_R": "MHBone_077",
    "KneeAux_R": "MHBone_077",
    "自定义14": "MHBone_085",
}


def _detect_and_rename(obj):
    """自动检测 MMD 骨骼类型并重命名"""
    vgroups = obj.vertex_groups
    
    # 检测是日文还是英文命名
    if "下半身" in vgroups:
        name_map = _MMD_UNFIXED_MAP
    elif "Hips" in vgroups:
        name_map = _MMD_FIXED_MAP
    else:
        # 默认尝试英文
        name_map = _MMD_FIXED_MAP
    
    for old_name, new_name in name_map.items():
        if old_name in vgroups:
            vgroups[old_name].name = new_name


class MHW_OT_MMDtoMHW(bpy.types.Operator):
    """Convert MMD vertex groups to MHWorld format"""
    bl_idname = "mhw.mmd_to_mhw"
    bl_label = "MMD to MHWorld"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == "MESH" for obj in context.selected_objects)

    def execute(self, context):
        count = 0
        for obj in context.selected_objects:
            if obj.type == "MESH":
                _detect_and_rename(obj)
                count += 1
        
        self.report({'INFO'}, f"Converted {count} mesh(es)")
        return {'FINISHED'}


classes = [
    MHW_OT_MMDtoMHW,
]