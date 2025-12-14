import bpy
import copy

# Endfield 骨骼 -> MHWorld MhBone 映射
_ATTACH_MAP_ENDFIELD = [
    ("Pelvis", "MhBone_013"),
    ("Spine", "MhBone_001"),
    ("Spine2", "MhBone_002"),
    ("Neck", "MhBone_003"),
    ("Head", "MhBone_004"),
    ("L_Clavicle", "MhBone_005"),
    ("LUpArmTwist", "MhBone_080"),
    ("L_UpperArm_tz_plus", "MhBone_070"),
    ("L_UpperArm", "MhBone_006"),
    ("L_Forearm", "MhBone_007"),
    ("L_ForeTwist", "MhBone_081"),
    ("L_Hand", "MhBone_008"),
    ("L_Finger0", "MhBone_031"),
    ("L_Finger01", "MhBone_032"),
    ("L_Finger02", "MhBone_033"),
    ("L_Finger1", "MhBone_034"),
    ("L_Finger11", "MhBone_035"),
    ("L_Finger12", "MhBone_036"),
    ("L_Finger2", "MhBone_037"),
    ("L_Finger21", "MhBone_038"),
    ("L_Finger22", "MhBone_039"),
    ("L_Finger3", "MhBone_041"),
    ("L_Finger31", "MhBone_042"),
    ("L_Finger32", "MhBone_043"),
    ("L_Finger4", "MhBone_044"),
    ("L_Finger41", "MhBone_045"),
    ("L_Finger42", "MhBone_046"),
    ("R_Clavicle", "MhBone_009"),
    ("RUpArmTwist", "MhBone_082"),
    ("R_UpperArm_tz_plus", "MhBone_072"),
    ("R_UpperArm", "MhBone_010"),
    ("R_Forearm", "MhBone_011"),
    ("R_ForeTwist", "MhBone_083"),
    ("R_Hand", "MhBone_012"),
    ("R_Finger0", "MhBone_048"),
    ("R_Finger01", "MhBone_049"),
    ("R_Finger02", "MhBone_050"),
    ("R_Finger1", "MhBone_051"),
    ("R_Finger11", "MhBone_052"),
    ("R_Finger12", "MhBone_053"),
    ("R_Finger2", "MhBone_054"),
    ("R_Finger21", "MhBone_055"),
    ("R_Finger22", "MhBone_056"),
    ("R_Finger3", "MhBone_058"),
    ("R_Finger31", "MhBone_059"),
    ("R_Finger32", "MhBone_060"),
    ("R_Finger4", "MhBone_061"),
    ("R_Finger41", "MhBone_062"),
    ("R_Finger42", "MhBone_063"),
    ("L_Thigh", "MhBone_014"),
    ("L_Thigh_ty_minus", "MhBone_074"),
    ("L_Calf", "MhBone_015"),
    ("L_Calf_ty_plus", "MhBone_075"),
    ("L_Foot", "MhBone_016"),
    ("L_Toe0", "MhBone_017"),
    ("R_Thigh", "MhBone_018"),
    ("R_Thigh_ty_minus", "MhBone_076"),
    ("R_Calf", "MhBone_019"),
    ("R_Calf_ty_plus", "MhBone_077"),
    ("R_Foot", "MhBone_020"),
    ("R_Toe0", "MhBone_021"),
]

def _attach_bones_endfield(context):
    """
    执行 Endfield 骨骼吸附 (Translation Only / Match Pivot)
    """
    active_obj = context.active_object
    selected_objects = [obj for obj in context.selected_objects if obj.type == 'ARMATURE']
    
    # 基本检查
    if not active_obj or active_obj.type != 'ARMATURE':
        return False, "请先激活(Active)目标骨架(MHWorld)，它应该显示为亮黄色轮廓"
    
    if len(selected_objects) != 2:
        return False, "请选择正好两个骨架：目标骨架(Active) 和 源骨架(Selected)"
        
    target_armature = active_obj
    source_armature = [obj for obj in selected_objects if obj != target_armature][0]
    
    # === 调试信息 ===
    print("\n[MBT Debug] 开始骨骼对齐检查...")
    print(f"[MBT Debug] 目标骨架 (Active/Target): {target_armature.name}")
    print(f"[MBT Debug] 源骨架 (Selected/Source): {source_armature.name}")
    
    # 确保进入对象模式以读取源数据
    bpy.ops.object.mode_set(mode='OBJECT')
    source_bones = source_armature.data.bones
    
    # 打印前5个骨骼名字，帮助排查命名问题
    s_names = [b.name for b in source_bones]
    print(f"[MBT Debug] 源骨架的前5个骨骼: {s_names[:5]}")
    
    # 切换目标骨架到编辑模式
    context.view_layer.objects.active = target_armature
    bpy.ops.object.mode_set(mode='EDIT')
    target_edit_bones = target_armature.data.edit_bones
    
    t_names = [b.name for b in target_edit_bones]
    print(f"[MBT Debug] 目标骨架的前5个骨骼: {t_names[:5]}")
    
    # 准备矩阵转换
    source_matrix = source_armature.matrix_world
    target_matrix_inv = target_armature.matrix_world.inverted()
    
    aligned_count = 0
    processed_targets = set()
    
    for src_name, dst_name in _ATTACH_MAP_ENDFIELD:
        # 检查源骨骼
        if src_name not in source_bones:
            # 仅在找不到 Pelvis 等关键骨骼时打印，避免刷屏
            if src_name in ["Pelvis", "Spine", "Hips"]:
                print(f"[MBT Debug] 警告: 源骨架中找不到骨骼 '{src_name}'")
            continue
            
        # 检查目标骨骼
        if dst_name not in target_edit_bones:
            # 仅在找不到 MhBone_001 等关键骨骼时打印
            if dst_name in ["MhBone_001", "MhBone_013"]:
                print(f"[MBT Debug] 警告: 目标骨架中找不到骨骼 '{dst_name}'")
            continue
            
        if dst_name in processed_targets:
            continue
            
        source_bone = source_bones[src_name]
        target_bone = target_edit_bones[dst_name]
        
        try:
            # 1. 断开连接，防止移动 Head 时影响父级
            target_bone.use_connect = False

            # 2. 记录目标骨骼原始向量 (长度和方向)
            original_vector = target_bone.tail - target_bone.head
            
            # 3. 计算源骨骼的世界坐标 Head
            source_head_world = source_matrix @ source_bone.head_local
            
            # 4. 将世界坐标转换为目标骨架的局部坐标
            new_head_local = target_matrix_inv @ source_head_world
            
            # 5. 应用新位置
            target_bone.head = new_head_local
            target_bone.tail = new_head_local + original_vector
            
            processed_targets.add(dst_name)
            aligned_count += 1
            
        except Exception as e:
            print(f"[MBT Error] 对齐 {src_name} -> {dst_name} 时发生错误: {e}")
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    if aligned_count == 0:
        print("[MBT Debug] 匹配失败：映射表中的所有对应关系都未在骨架中找到。")
        return False, "未找到任何匹配骨骼，请打开系统控制台(Window->Toggle System Console)查看调试信息"
        
    return True, f"成功对齐了 {aligned_count} 根骨骼的位置"

class MHW_OT_AttachBonesEndfield(bpy.types.Operator):
    """Attach Endfield armature bones to MHWorld armature positions (Keep Orientation)"""
    bl_idname = "mhw.attach_bones_endfield"
    bl_label = "Attach Endfield Armature"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
            context.active_object is not None 
            and context.active_object.type == 'ARMATURE'
            and len([o for o in context.selected_objects if o.type == 'ARMATURE']) == 2
        )

    def execute(self, context):
        success, message = _attach_bones_endfield(context)
        
        if success:
            self.report({'INFO'}, message)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, message)
            return {'CANCELLED'}

classes = [
    MHW_OT_AttachBonesEndfield,
]