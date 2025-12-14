import bpy
import copy

# MMD 日文骨骼 -> MHWorld MhBone 映射 (用于骨骼吸附)
_SNAP_MAP_UNFIXED = [
    # 躯干
    ("下半身", "MhBone_013"),
    ("上半身", "MhBone_001"),
    ("上半身2", "MhBone_002"),
    ("首", "MhBone_003"),
    ("頭", "MhBone_004"),
    ("首", "MhBone_254"),
    
    # 左臂
    ("肩.L", "MhBone_005"),
    ("腕.L", "MhBone_006"),
    ("ひじ.L", "MhBone_007"),
    ("手首.L", "MhBone_008"),
    ("手首.L", "MhBone_030"),
    ("親指０.L", "MhBone_031"),
    ("親指１.L", "MhBone_032"),
    ("親指２.L", "MhBone_033"),
    ("人指１.L", "MhBone_034"),
    ("人指２.L", "MhBone_035"),
    ("人指３.L", "MhBone_036"),
    ("中指１.L", "MhBone_037"),
    ("中指２.L", "MhBone_038"),
    ("中指３.L", "MhBone_039"),
    ("手首.L", "MhBone_040"),
    ("薬指１.L", "MhBone_041"),
    ("薬指２.L", "MhBone_042"),
    ("薬指３.L", "MhBone_043"),
    ("小指１.L", "MhBone_044"),
    ("小指２.L", "MhBone_045"),
    ("小指３.L", "MhBone_046"),
    
    # 右臂
    ("肩.R", "MhBone_009"),
    ("腕.R", "MhBone_010"),
    ("ひじ.R", "MhBone_011"),
    ("手首.R", "MhBone_012"),
    ("手首.R", "MhBone_047"),
    ("親指０.R", "MhBone_048"),
    ("親指１.R", "MhBone_049"),
    ("親指２.R", "MhBone_050"),
    ("人指１.R", "MhBone_051"),
    ("人指２.R", "MhBone_052"),
    ("人指３.R", "MhBone_053"),
    ("中指１.R", "MhBone_054"),
    ("中指２.R", "MhBone_055"),
    ("中指３.R", "MhBone_056"),
    ("手首.R", "MhBone_057"),
    ("薬指１.R", "MhBone_058"),
    ("薬指２.R", "MhBone_059"),
    ("薬指３.R", "MhBone_060"),
    ("小指１.R", "MhBone_061"),
    ("小指２.R", "MhBone_062"),
    ("小指３.R", "MhBone_063"),
    
    # 腿部
    ("足D.L", "MhBone_014"),
    ("ひざD.L", "MhBone_015"),
    ("足首D.L", "MhBone_016"),
    ("足先EX.L", "MhBone_017"),
    ("足D.R", "MhBone_018"),
    ("ひざD.R", "MhBone_019"),
    ("足首D.R", "MhBone_020"),
    ("足先EX.R", "MhBone_021"),
    
    # 辅助骨骼
    ("腕.L", "MhBone_070"),
    ("ひじ.L", "MhBone_071"),
    ("腕.L", "MhBone_080"),
    ("手捩.L", "MhBone_081"),
    ("腕.R", "MhBone_072"),
    ("ひじ.R", "MhBone_073"),
    ("腕.R", "MhBone_082"),
    ("手捩.R", "MhBone_083"),
    ("足D.L", "MhBone_074"),
    ("ひざD.L", "MhBone_075"),
    ("足首D.L", "MhBone_084"),
    ("足D.R", "MhBone_076"),
    ("ひざD.R", "MhBone_077"),
    ("足首D.R", "MhBone_085"),
]

# MMD 英文骨骼映射
_SNAP_MAP_FIXED = [
    # 躯干
    ("Hips", "MhBone_013"),
    ("Spine", "MhBone_001"),
    ("Chest", "MhBone_002"),
    ("Neck", "MhBone_003"),
    ("Head", "MhBone_004"),
    ("Neck", "MhBone_254"),
    
    # 左臂
    ("Left shoulder", "MhBone_005"),
    ("Left arm", "MhBone_006"),
    ("Left elbow", "MhBone_007"),
    ("Left wrist", "MhBone_008"),
    ("Left wrist", "MhBone_030"),
    ("Thumb0_L", "MhBone_031"),
    ("Thumb1_L", "MhBone_032"),
    ("Thumb2_L", "MhBone_033"),
    ("IndexFinger1_L", "MhBone_034"),
    ("IndexFinger2_L", "MhBone_035"),
    ("IndexFinger3_L", "MhBone_036"),
    ("MiddleFinger1_L", "MhBone_037"),
    ("MiddleFinger2_L", "MhBone_038"),
    ("MiddleFinger3_L", "MhBone_039"),
    ("Left wrist", "MhBone_040"),
    ("RingFinger1_L", "MhBone_041"),
    ("RingFinger2_L", "MhBone_042"),
    ("RingFinger3_L", "MhBone_043"),
    ("LittleFinger1_L", "MhBone_044"),
    ("LittleFinger2_L", "MhBone_045"),
    ("LittleFinger3_L", "MhBone_046"),
    
    # 右臂
    ("Right shoulder", "MhBone_009"),
    ("Right arm", "MhBone_010"),
    ("Right elbow", "MhBone_011"),
    ("Right wrist", "MhBone_012"),
    ("Right wrist", "MhBone_047"),
    ("Thumb0_R", "MhBone_048"),
    ("Thumb1_R", "MhBone_049"),
    ("Thumb2_R", "MhBone_050"),
    ("IndexFinger1_R", "MhBone_051"),
    ("IndexFinger2_R", "MhBone_052"),
    ("IndexFinger3_R", "MhBone_053"),
    ("MiddleFinger1_R", "MhBone_054"),
    ("MiddleFinger2_R", "MhBone_055"),
    ("MiddleFinger3_R", "MhBone_056"),
    ("Right wrist", "MhBone_057"),
    ("RingFinger1_R", "MhBone_058"),
    ("RingFinger2_R", "MhBone_059"),
    ("RingFinger3_R", "MhBone_060"),
    ("LittleFinger1_R", "MhBone_061"),
    ("LittleFinger2_R", "MhBone_062"),
    ("LittleFinger3_R", "MhBone_063"),
    
    # 腿部
    ("Left leg", "MhBone_014"),
    ("Left knee", "MhBone_015"),
    ("Left ankle", "MhBone_016"),
    ("Left toe", "MhBone_017"),
    ("Right leg", "MhBone_018"),
    ("Right knee", "MhBone_019"),
    ("Right ankle", "MhBone_020"),
    ("Right toe", "MhBone_021"),
    
    # 辅助骨骼
    ("Left arm", "MhBone_070"),
    ("Left elbow", "MhBone_071"),
    ("Left arm", "MhBone_080"),
    ("zHandTwist_L", "MhBone_081"),
    ("Right arm", "MhBone_072"),
    ("Right elbow", "MhBone_073"),
    ("Right arm", "MhBone_082"),
    ("zHandTwist_R", "MhBone_083"),
    ("Left leg", "MhBone_074"),
    ("Left knee", "MhBone_075"),
    ("Left ankle", "MhBone_084"),
    ("Right leg", "MhBone_076"),
    ("Right knee", "MhBone_077"),
    ("Right ankle", "MhBone_085"),
]

# 需要特殊处理的肘部辅助骨骼
_ELBOW_AUX_BONES = [
    "MhBone_101",
    "MhBone_102", 
    "MhBone_103",
    "MhBone_104",
]


def _snap_bones(context):
    """执行骨骼吸附"""
    # 保存原始骨骼名称
    original_bones = [b.name for b in context.active_object.data.bones]
    
    # 合并骨架
    bpy.ops.object.join()
    
    armature = context.active_object.data
    armature_name = armature.name
    all_bone_names = [b.name for b in armature.bones]
    
    # 检测使用哪个映射表
    if "下半身" in all_bone_names:
        snap_map = _SNAP_MAP_UNFIXED
    elif "Hips" in all_bone_names:
        snap_map = _SNAP_MAP_FIXED
    else:
        return False
    
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = bpy.data.armatures[armature_name].edit_bones
    
    for src_name, dst_name in snap_map:
        if src_name not in all_bone_names:
            continue
        if dst_name not in edit_bones:
            continue
            
        # 特殊处理：记录 MhBone_007 吸附前的位置
        before_head = None
        before_tail = None
        if dst_name == "MhBone_007":
            before_head = copy.deepcopy(edit_bones["MhBone_007"].head)
            before_tail = copy.deepcopy(edit_bones["MhBone_007"].tail)
        
        # 执行吸附
        edit_bones.active = edit_bones[src_name]
        context.object.data.use_mirror_x = False
        bpy.ops.armature.select_all(action='DESELECT')
        edit_bones[src_name].select = True
        edit_bones[dst_name].select = True
        
        # 切换到 3D 视图执行 snap
        original_area = context.area.type
        context.area.type = 'VIEW_3D'
        bpy.ops.view3d.snap_selected_to_active()
        context.area.type = original_area
        
        # 特殊处理：脚趾骨骼 Y 轴位置修正
        if dst_name in ("MhBone_017", "MhBone_021"):
            edit_bones.active = edit_bones[dst_name]
            context.active_bone.head[1] = -104.611
            context.active_bone.tail[1] = -104.607
        
        # 特殊处理：肘部吸附后移动辅助骨骼
        if dst_name == "MhBone_007" and before_head is not None:
            after_head = edit_bones["MhBone_007"].head
            after_tail = edit_bones["MhBone_007"].tail
            head_offset = after_head - before_head
            tail_offset = after_tail - before_tail
            
            for aux_bone in _ELBOW_AUX_BONES:
                if aux_bone in edit_bones:
                    edit_bones[aux_bone].head += head_offset
                    edit_bones[aux_bone].tail += tail_offset
        
        bpy.ops.armature.select_all(action='DESELECT')
    
    # 显示所有骨骼层
    if hasattr(context.object.data, 'layers'):
        for i in range(32):
            context.object.data.layers[i] = True
    else:
        for coll in armature.collections:
            coll.is_visible = True
    
    # 删除非原始骨骼
    for bone_name in all_bone_names:
        if bone_name not in original_bones:
            if bone_name in edit_bones:
                edit_bones.active = edit_bones[bone_name]
                bpy.ops.armature.delete()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return True


class MHW_OT_SnapBonesMMD(bpy.types.Operator):
    """Snap MMD armature bones to MHWorld armature positions"""
    bl_idname = "mhw.snap_bones_mmd"
    bl_label = "Snap MMD Armature"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
            any(obj.type == "ARMATURE" for obj in context.selected_objects)
            and context.mode == 'OBJECT'
        )

    def execute(self, context):
        if _snap_bones(context):
            self.report({'INFO'}, "Bone snap completed")
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Could not detect MMD bone naming")
            return {'CANCELLED'}


classes = [
    MHW_OT_SnapBonesMMD,
]