import bpy
import copy

# MMD 日文骨骼 -> MHWorld bonefunction 映射 (用于骨骼吸附)
_SNAP_MAP_UNFIXED = [
    # 躯干
    ("下半身", "bonefunction_013"),
    ("上半身", "bonefunction_001"),
    ("上半身2", "bonefunction_002"),
    ("首", "bonefunction_003"),
    ("頭", "bonefunction_004"),
    ("首", "bonefunction_254"),
    
    # 左臂
    ("肩.L", "bonefunction_005"),
    ("腕.L", "bonefunction_006"),
    ("ひじ.L", "bonefunction_007"),
    ("手首.L", "bonefunction_008"),
    ("手首.L", "bonefunction_030"),
    ("親指０.L", "bonefunction_031"),
    ("親指１.L", "bonefunction_032"),
    ("親指２.L", "bonefunction_033"),
    ("人指１.L", "bonefunction_034"),
    ("人指２.L", "bonefunction_035"),
    ("人指３.L", "bonefunction_036"),
    ("中指１.L", "bonefunction_037"),
    ("中指２.L", "bonefunction_038"),
    ("中指３.L", "bonefunction_039"),
    ("手首.L", "bonefunction_040"),
    ("薬指１.L", "bonefunction_041"),
    ("薬指２.L", "bonefunction_042"),
    ("薬指３.L", "bonefunction_043"),
    ("小指１.L", "bonefunction_044"),
    ("小指２.L", "bonefunction_045"),
    ("小指３.L", "bonefunction_046"),
    
    # 右臂
    ("肩.R", "bonefunction_009"),
    ("腕.R", "bonefunction_010"),
    ("ひじ.R", "bonefunction_011"),
    ("手首.R", "bonefunction_012"),
    ("手首.R", "bonefunction_047"),
    ("親指０.R", "bonefunction_048"),
    ("親指１.R", "bonefunction_049"),
    ("親指２.R", "bonefunction_050"),
    ("人指１.R", "bonefunction_051"),
    ("人指２.R", "bonefunction_052"),
    ("人指３.R", "bonefunction_053"),
    ("中指１.R", "bonefunction_054"),
    ("中指２.R", "bonefunction_055"),
    ("中指３.R", "bonefunction_056"),
    ("手首.R", "bonefunction_057"),
    ("薬指１.R", "bonefunction_058"),
    ("薬指２.R", "bonefunction_059"),
    ("薬指３.R", "bonefunction_060"),
    ("小指１.R", "bonefunction_061"),
    ("小指２.R", "bonefunction_062"),
    ("小指３.R", "bonefunction_063"),
    
    # 腿部
    ("足D.L", "bonefunction_014"),
    ("ひざD.L", "bonefunction_015"),
    ("足首D.L", "bonefunction_016"),
    ("足先EX.L", "bonefunction_017"),
    ("足D.R", "bonefunction_018"),
    ("ひざD.R", "bonefunction_019"),
    ("足首D.R", "bonefunction_020"),
    ("足先EX.R", "bonefunction_021"),
    
    # 辅助骨骼
    ("腕.L", "bonefunction_070"),
    ("ひじ.L", "bonefunction_071"),
    ("腕.L", "bonefunction_080"),
    ("手捩.L", "bonefunction_081"),
    ("腕.R", "bonefunction_072"),
    ("ひじ.R", "bonefunction_073"),
    ("腕.R", "bonefunction_082"),
    ("手捩.R", "bonefunction_083"),
    ("足D.L", "bonefunction_074"),
    ("ひざD.L", "bonefunction_075"),
    ("足首D.L", "bonefunction_084"),
    ("足D.R", "bonefunction_076"),
    ("ひざD.R", "bonefunction_077"),
    ("足首D.R", "bonefunction_085"),
]

# MMD 英文骨骼映射
_SNAP_MAP_FIXED = [
    # 躯干
    ("Hips", "bonefunction_013"),
    ("Spine", "bonefunction_001"),
    ("Chest", "bonefunction_002"),
    ("Neck", "bonefunction_003"),
    ("Head", "bonefunction_004"),
    ("Neck", "bonefunction_254"),
    
    # 左臂
    ("Left shoulder", "bonefunction_005"),
    ("Left arm", "bonefunction_006"),
    ("Left elbow", "bonefunction_007"),
    ("Left wrist", "bonefunction_008"),
    ("Left wrist", "bonefunction_030"),
    ("Thumb0_L", "bonefunction_031"),
    ("Thumb1_L", "bonefunction_032"),
    ("Thumb2_L", "bonefunction_033"),
    ("IndexFinger1_L", "bonefunction_034"),
    ("IndexFinger2_L", "bonefunction_035"),
    ("IndexFinger3_L", "bonefunction_036"),
    ("MiddleFinger1_L", "bonefunction_037"),
    ("MiddleFinger2_L", "bonefunction_038"),
    ("MiddleFinger3_L", "bonefunction_039"),
    ("Left wrist", "bonefunction_040"),
    ("RingFinger1_L", "bonefunction_041"),
    ("RingFinger2_L", "bonefunction_042"),
    ("RingFinger3_L", "bonefunction_043"),
    ("LittleFinger1_L", "bonefunction_044"),
    ("LittleFinger2_L", "bonefunction_045"),
    ("LittleFinger3_L", "bonefunction_046"),
    
    # 右臂
    ("Right shoulder", "bonefunction_009"),
    ("Right arm", "bonefunction_010"),
    ("Right elbow", "bonefunction_011"),
    ("Right wrist", "bonefunction_012"),
    ("Right wrist", "bonefunction_047"),
    ("Thumb0_R", "bonefunction_048"),
    ("Thumb1_R", "bonefunction_049"),
    ("Thumb2_R", "bonefunction_050"),
    ("IndexFinger1_R", "bonefunction_051"),
    ("IndexFinger2_R", "bonefunction_052"),
    ("IndexFinger3_R", "bonefunction_053"),
    ("MiddleFinger1_R", "bonefunction_054"),
    ("MiddleFinger2_R", "bonefunction_055"),
    ("MiddleFinger3_R", "bonefunction_056"),
    ("Right wrist", "bonefunction_057"),
    ("RingFinger1_R", "bonefunction_058"),
    ("RingFinger2_R", "bonefunction_059"),
    ("RingFinger3_R", "bonefunction_060"),
    ("LittleFinger1_R", "bonefunction_061"),
    ("LittleFinger2_R", "bonefunction_062"),
    ("LittleFinger3_R", "bonefunction_063"),
    
    # 腿部
    ("Left leg", "bonefunction_014"),
    ("Left knee", "bonefunction_015"),
    ("Left ankle", "bonefunction_016"),
    ("Left toe", "bonefunction_017"),
    ("Right leg", "bonefunction_018"),
    ("Right knee", "bonefunction_019"),
    ("Right ankle", "bonefunction_020"),
    ("Right toe", "bonefunction_021"),
    
    # 辅助骨骼
    ("Left arm", "bonefunction_070"),
    ("Left elbow", "bonefunction_071"),
    ("Left arm", "bonefunction_080"),
    ("zHandTwist_L", "bonefunction_081"),
    ("Right arm", "bonefunction_072"),
    ("Right elbow", "bonefunction_073"),
    ("Right arm", "bonefunction_082"),
    ("zHandTwist_R", "bonefunction_083"),
    ("Left leg", "bonefunction_074"),
    ("Left knee", "bonefunction_075"),
    ("Left ankle", "bonefunction_084"),
    ("Right leg", "bonefunction_076"),
    ("Right knee", "bonefunction_077"),
    ("Right ankle", "bonefunction_085"),
]

# 需要特殊处理的肘部辅助骨骼
_ELBOW_AUX_BONES = [
    "bonefunction_101",
    "bonefunction_102", 
    "bonefunction_103",
    "bonefunction_104",
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
            
        # 特殊处理：记录 bonefunction_007 吸附前的位置
        before_head = None
        before_tail = None
        if dst_name == "bonefunction_007":
            before_head = copy.deepcopy(edit_bones["bonefunction_007"].head)
            before_tail = copy.deepcopy(edit_bones["bonefunction_007"].tail)
        
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
        if dst_name in ("bonefunction_017", "bonefunction_021"):
            edit_bones.active = edit_bones[dst_name]
            context.active_bone.head[1] = -104.611
            context.active_bone.tail[1] = -104.607
        
        # 特殊处理：肘部吸附后移动辅助骨骼
        if dst_name == "bonefunction_007" and before_head is not None:
            after_head = edit_bones["bonefunction_007"].head
            after_tail = edit_bones["bonefunction_007"].tail
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