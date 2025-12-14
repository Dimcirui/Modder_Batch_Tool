import bpy
import copy

# MMD 日文骨骼 -> MHWorld MHBone 映射 (用于骨骼吸附)
_SNAP_MAP_UNFIXED = [
    # 躯干
    ("下半身", "MHBone_013"),
    ("上半身", "MHBone_001"),
    ("上半身2", "MHBone_002"),
    ("首", "MHBone_003"),
    ("頭", "MHBone_004"),
    ("首", "MHBone_254"),
    
    # 左臂
    ("肩.L", "MHBone_005"),
    ("腕.L", "MHBone_006"),
    ("ひじ.L", "MHBone_007"),
    ("手首.L", "MHBone_008"),
    ("手首.L", "MHBone_030"),
    ("親指０.L", "MHBone_031"),
    ("親指１.L", "MHBone_032"),
    ("親指２.L", "MHBone_033"),
    ("人指１.L", "MHBone_034"),
    ("人指２.L", "MHBone_035"),
    ("人指３.L", "MHBone_036"),
    ("中指１.L", "MHBone_037"),
    ("中指２.L", "MHBone_038"),
    ("中指３.L", "MHBone_039"),
    ("手首.L", "MHBone_040"),
    ("薬指１.L", "MHBone_041"),
    ("薬指２.L", "MHBone_042"),
    ("薬指３.L", "MHBone_043"),
    ("小指１.L", "MHBone_044"),
    ("小指２.L", "MHBone_045"),
    ("小指３.L", "MHBone_046"),
    
    # 右臂
    ("肩.R", "MHBone_009"),
    ("腕.R", "MHBone_010"),
    ("ひじ.R", "MHBone_011"),
    ("手首.R", "MHBone_012"),
    ("手首.R", "MHBone_047"),
    ("親指０.R", "MHBone_048"),
    ("親指１.R", "MHBone_049"),
    ("親指２.R", "MHBone_050"),
    ("人指１.R", "MHBone_051"),
    ("人指２.R", "MHBone_052"),
    ("人指３.R", "MHBone_053"),
    ("中指１.R", "MHBone_054"),
    ("中指２.R", "MHBone_055"),
    ("中指３.R", "MHBone_056"),
    ("手首.R", "MHBone_057"),
    ("薬指１.R", "MHBone_058"),
    ("薬指２.R", "MHBone_059"),
    ("薬指３.R", "MHBone_060"),
    ("小指１.R", "MHBone_061"),
    ("小指２.R", "MHBone_062"),
    ("小指３.R", "MHBone_063"),
    
    # 腿部
    ("足D.L", "MHBone_014"),
    ("ひざD.L", "MHBone_015"),
    ("足首D.L", "MHBone_016"),
    ("足先EX.L", "MHBone_017"),
    ("足D.R", "MHBone_018"),
    ("ひざD.R", "MHBone_019"),
    ("足首D.R", "MHBone_020"),
    ("足先EX.R", "MHBone_021"),
    
    # 辅助骨骼
    ("腕.L", "MHBone_070"),
    ("ひじ.L", "MHBone_071"),
    ("腕.L", "MHBone_080"),
    ("手捩.L", "MHBone_081"),
    ("腕.R", "MHBone_072"),
    ("ひじ.R", "MHBone_073"),
    ("腕.R", "MHBone_082"),
    ("手捩.R", "MHBone_083"),
    ("足D.L", "MHBone_074"),
    ("ひざD.L", "MHBone_075"),
    ("足首D.L", "MHBone_084"),
    ("足D.R", "MHBone_076"),
    ("ひざD.R", "MHBone_077"),
    ("足首D.R", "MHBone_085"),
]

# MMD 英文骨骼映射
_SNAP_MAP_FIXED = [
    # 躯干
    ("Hips", "MHBone_013"),
    ("Spine", "MHBone_001"),
    ("Chest", "MHBone_002"),
    ("Neck", "MHBone_003"),
    ("Head", "MHBone_004"),
    ("Neck", "MHBone_254"),
    
    # 左臂
    ("Left shoulder", "MHBone_005"),
    ("Left arm", "MHBone_006"),
    ("Left elbow", "MHBone_007"),
    ("Left wrist", "MHBone_008"),
    ("Left wrist", "MHBone_030"),
    ("Thumb0_L", "MHBone_031"),
    ("Thumb1_L", "MHBone_032"),
    ("Thumb2_L", "MHBone_033"),
    ("IndexFinger1_L", "MHBone_034"),
    ("IndexFinger2_L", "MHBone_035"),
    ("IndexFinger3_L", "MHBone_036"),
    ("MiddleFinger1_L", "MHBone_037"),
    ("MiddleFinger2_L", "MHBone_038"),
    ("MiddleFinger3_L", "MHBone_039"),
    ("Left wrist", "MHBone_040"),
    ("RingFinger1_L", "MHBone_041"),
    ("RingFinger2_L", "MHBone_042"),
    ("RingFinger3_L", "MHBone_043"),
    ("LittleFinger1_L", "MHBone_044"),
    ("LittleFinger2_L", "MHBone_045"),
    ("LittleFinger3_L", "MHBone_046"),
    
    # 右臂
    ("Right shoulder", "MHBone_009"),
    ("Right arm", "MHBone_010"),
    ("Right elbow", "MHBone_011"),
    ("Right wrist", "MHBone_012"),
    ("Right wrist", "MHBone_047"),
    ("Thumb0_R", "MHBone_048"),
    ("Thumb1_R", "MHBone_049"),
    ("Thumb2_R", "MHBone_050"),
    ("IndexFinger1_R", "MHBone_051"),
    ("IndexFinger2_R", "MHBone_052"),
    ("IndexFinger3_R", "MHBone_053"),
    ("MiddleFinger1_R", "MHBone_054"),
    ("MiddleFinger2_R", "MHBone_055"),
    ("MiddleFinger3_R", "MHBone_056"),
    ("Right wrist", "MHBone_057"),
    ("RingFinger1_R", "MHBone_058"),
    ("RingFinger2_R", "MHBone_059"),
    ("RingFinger3_R", "MHBone_060"),
    ("LittleFinger1_R", "MHBone_061"),
    ("LittleFinger2_R", "MHBone_062"),
    ("LittleFinger3_R", "MHBone_063"),
    
    # 腿部
    ("Left leg", "MHBone_014"),
    ("Left knee", "MHBone_015"),
    ("Left ankle", "MHBone_016"),
    ("Left toe", "MHBone_017"),
    ("Right leg", "MHBone_018"),
    ("Right knee", "MHBone_019"),
    ("Right ankle", "MHBone_020"),
    ("Right toe", "MHBone_021"),
    
    # 辅助骨骼
    ("Left arm", "MHBone_070"),
    ("Left elbow", "MHBone_071"),
    ("Left arm", "MHBone_080"),
    ("zHandTwist_L", "MHBone_081"),
    ("Right arm", "MHBone_072"),
    ("Right elbow", "MHBone_073"),
    ("Right arm", "MHBone_082"),
    ("zHandTwist_R", "MHBone_083"),
    ("Left leg", "MHBone_074"),
    ("Left knee", "MHBone_075"),
    ("Left ankle", "MHBone_084"),
    ("Right leg", "MHBone_076"),
    ("Right knee", "MHBone_077"),
    ("Right ankle", "MHBone_085"),
]

# 需要特殊处理的肘部辅助骨骼
_ELBOW_AUX_BONES = [
    "MHBone_101",
    "MHBone_102", 
    "MHBone_103",
    "MHBone_104",
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
            
        # 特殊处理：记录 MHBone_007 吸附前的位置
        before_head = None
        before_tail = None
        if dst_name == "MHBone_007":
            before_head = copy.deepcopy(edit_bones["MHBone_007"].head)
            before_tail = copy.deepcopy(edit_bones["MHBone_007"].tail)
        
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
        if dst_name in ("MHBone_017", "MHBone_021"):
            edit_bones.active = edit_bones[dst_name]
            context.active_bone.head[1] = -104.611
            context.active_bone.tail[1] = -104.607
        
        # 特殊处理：肘部吸附后移动辅助骨骼
        if dst_name == "MHBone_007" and before_head is not None:
            after_head = edit_bones["MHBone_007"].head
            after_tail = edit_bones["MHBone_007"].tail
            head_offset = after_head - before_head
            tail_offset = after_tail - before_tail
            
            for aux_bone in _ELBOW_AUX_BONES:
                if aux_bone in edit_bones:
                    edit_bones[aux_bone].head += head_offset
                    edit_bones[aux_bone].tail += tail_offset
        
        bpy.ops.armature.select_all(action='DESELECT')
    
    # 显示所有骨骼层 (Blender 4.x 用 collections)
    if hasattr(context.object.data, 'layers'):
        # Blender 3.x 及以下
        for i in range(32):
            context.object.data.layers[i] = True
    else:
        # Blender 4.x 使用 bone collections
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