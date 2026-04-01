import bpy

# MMD 日文骨骼名 -> MHWorld MhBone
_MMD_UNFIXED_MAP = {
    # 躯干
    "下半身": "MhBone_013",
    "上半身": "MhBone_001",
    "上半身2": "MhBone_002",
    "首": "MhBone_003",
    "頭": "MhBone_004",
    
    # 左臂
    "肩.L": "MhBone_005",
    "腕.L": "MhBone_006",
    "ひじ.L": "MhBone_007",
    "手首.L": "MhBone_008",
    "親指０.L": "MhBone_031",
    "親指１.L": "MhBone_032",
    "親指２.L": "MhBone_033",
    "人指１.L": "MhBone_034",
    "人指２.L": "MhBone_035",
    "人指３.L": "MhBone_036",
    "中指１.L": "MhBone_037",
    "中指２.L": "MhBone_038",
    "中指３.L": "MhBone_039",
    "自定义L": "MhBone_040",
    "薬指１.L": "MhBone_041",
    "薬指２.L": "MhBone_042",
    "薬指３.L": "MhBone_043",
    "小指１.L": "MhBone_044",
    "小指２.L": "MhBone_045",
    "小指３.L": "MhBone_046",
    
    # 右臂
    "肩.R": "MhBone_009",
    "腕.R": "MhBone_010",
    "ひじ.R": "MhBone_011",
    "手首.R": "MhBone_012",
    "親指０.R": "MhBone_048",
    "親指１.R": "MhBone_049",
    "親指２.R": "MhBone_050",
    "人指１.R": "MhBone_051",
    "人指２.R": "MhBone_052",
    "人指３.R": "MhBone_053",
    "中指１.R": "MhBone_054",
    "中指２.R": "MhBone_055",
    "中指３.R": "MhBone_056",
    "自定义R": "MhBone_057",
    "薬指１.R": "MhBone_058",
    "薬指２.R": "MhBone_059",
    "薬指３.R": "MhBone_060",
    "小指１.R": "MhBone_061",
    "小指２.R": "MhBone_062",
    "小指３.R": "MhBone_063",
    
    # 左腿
    "足D.L": "MhBone_014",
    "ひざD.L": "MhBone_015",
    "足首D.L": "MhBone_016",
    "足先EX.L": "MhBone_017",
    
    # 右腿
    "足D.R": "MhBone_018",
    "ひざD.R": "MhBone_019",
    "足首D.R": "MhBone_020",
    "足先EX.R": "MhBone_021",
    
    # 辅助骨骼
    "自定义1": "MhBone_070",
    "+ひじ補助.L": "MhBone_071",
    "ひじ補助.L": "MhBone_071",
    "自定义3": "MhBone_080",
    "自定义4": "MhBone_081",
    "自定义5": "MhBone_072",
    "+ひじ補助.R": "MhBone_073",
    "ひじ補助.R": "MhBone_073",
    "自定义7": "MhBone_082",
    "自定义8": "MhBone_083",
    "お尻.L": "MhBone_074",
    "+ひざ補助.L": "MhBone_075",
    "ひざ補助.L": "MhBone_075",
    "自定义11": "MhBone_084",
    "お尻.R": "MhBone_076",
    "+ひざ補助.R": "MhBone_077",
    "ひざ補助.R": "MhBone_077",
    "自定义14": "MhBone_085",
}

# MMD 英文骨骼名 -> MHWorld MhBone
_MMD_FIXED_MAP = {
    # 躯干
    "Hips": "MhBone_013",
    "Spine": "MhBone_001",
    "Chest": "MhBone_002",
    "Neck": "MhBone_003",
    "Head": "MhBone_004",
    
    # 左臂
    "Left shoulder": "MhBone_005",
    "zArmTwist_L": "MhBone_006",
    "Left elbow": "MhBone_007",
    "Left wrist": "MhBone_008",
    "Thumb0_L": "MhBone_031",
    "Thumb1_L": "MhBone_032",
    "Thumb2_L": "MhBone_033",
    "IndexFinger1_L": "MhBone_034",
    "IndexFinger2_L": "MhBone_035",
    "IndexFinger3_L": "MhBone_036",
    "MiddleFinger1_L": "MhBone_037",
    "MiddleFinger2_L": "MhBone_038",
    "MiddleFinger3_L": "MhBone_039",
    "自定义L": "MhBone_040",
    "RingFinger1_L": "MhBone_041",
    "RingFinger2_L": "MhBone_042",
    "RingFinger3_L": "MhBone_043",
    "LittleFinger1_L": "MhBone_044",
    "LittleFinger2_L": "MhBone_045",
    "LittleFinger3_L": "MhBone_046",
    
    # 右臂
    "Right shoulder": "MhBone_009",
    "zArmTwist_R": "MhBone_010",
    "Right elbow": "MhBone_011",
    "Right wrist": "MhBone_012",
    "Thumb0_R": "MhBone_048",
    "Thumb1_R": "MhBone_049",
    "Thumb2_R": "MhBone_050",
    "IndexFinger1_R": "MhBone_051",
    "IndexFinger2_R": "MhBone_052",
    "IndexFinger3_R": "MhBone_053",
    "MiddleFinger1_R": "MhBone_054",
    "MiddleFinger2_R": "MhBone_055",
    "MiddleFinger3_R": "MhBone_056",
    "自定义R": "MhBone_057",
    "RingFinger1_R": "MhBone_058",
    "RingFinger2_R": "MhBone_059",
    "RingFinger3_R": "MhBone_060",
    "LittleFinger1_R": "MhBone_061",
    "LittleFinger2_R": "MhBone_062",
    "LittleFinger3_R": "MhBone_063",
    
    # 左腿
    "Left leg": "MhBone_014",
    "Left knee": "MhBone_015",
    "Left ankle": "MhBone_016",
    "Left toe": "MhBone_017",
    
    # 右腿
    "Right leg": "MhBone_018",
    "Right knee": "MhBone_019",
    "Right ankle": "MhBone_020",
    "Right toe": "MhBone_021",
    
    # 辅助骨骼
    "自定义1": "MhBone_070",
    "+ElbowAux_L": "MhBone_071",
    "ElbowAux_L": "MhBone_071",
    "Left arm": "MhBone_080",
    "zHandTwist_L": "MhBone_081",
    "自定义5": "MhBone_072",
    "+ElbowAux_R": "MhBone_073",
    "ElbowAux_R": "MhBone_073",
    "Right arm": "MhBone_082",
    "zHandTwist_R": "MhBone_083",
    "OhButt_L": "MhBone_074",
    "+KneeAux_L": "MhBone_075",
    "KneeAux_L": "MhBone_075",
    "自定义11": "MhBone_084",
    "OhButt_R": "MhBone_076",
    "+KneeAux_R": "MhBone_077",
    "KneeAux_R": "MhBone_077",
    "自定义14": "MhBone_085",
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