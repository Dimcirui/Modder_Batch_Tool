import bpy
import copy

# Endfield 骨骼 -> MHWorld MhBone 映射
_ATTACH_MAP_ENDFIELD = [
# 躯干
    ("Pelvis", "MhBone_013"),
    ("Spine", "MhBone_001"),
    ("Spine1", "MhBone_001"),
    ("Spine2", "MhBone_002"),
    ("Neck", "MhBone_003"),
    ("Head", "MhBone_004"),
    
    # 左臂
    ("L_Clavicle", "MhBone_005"),
    ("LUpArmTwist", "MhBone_080"),
    ("LUpArmTwist1", "MhBone_080"),
    ("L_UpperArm_ty_minus", "MhBone_080"),
    ("L_UpperArm_ty_plus", "MhBone_080"),
    ("L_UpperArm_tz_minus", "MhBone_080"),
    ("L_UpperArm_tz_plus", "MhBone_070"),
    ("L_UpperArm", "MhBone_006"),
    ("L_Forearm", "MhBone_007"),
    ("L_ForeTwist", "MhBone_081"),
    ("L_ForeTwist1", "MhBone_081"),
    ("L_Hand", "MhBone_008"),
    ("L_Hand_ty_minus", "MhBone_008"),
    ("L_Hand_ty_plus", "MhBone_008"),
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
    
    # 右臂
    ("R_Clavicle", "MhBone_009"),
    ("RUpArmTwist", "MhBone_082"),
    ("RUpArmTwist1", "MhBone_082"),
    ("R_UpperArm_ty_minus", "MhBone_082"),
    ("R_UpperArm_ty_plus", "MhBone_082"),
    ("R_UpperArm_tz_minus", "MhBone_082"),
    ("R_UpperArm_tz_plus", "MhBone_072"),
    ("R_UpperArm", "MhBone_010"),
    ("R_Forearm", "MhBone_011"),
    ("R_ForeTwist", "MhBone_083"),
    ("R_ForeTwist1", "MhBone_083"),
    ("R_Hand", "MhBone_012"),
    ("R_Hand_ty_minus", "MhBone_012"),
    ("R_Hand_ty_plus", "MhBone_012"),
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
    
    # 左腿
    ("L_Thigh", "MhBone_014"),
    ("LThighTwist", "MhBone_014"),
    ("LThighTwist1", "MhBone_014"),
    ("L_Thigh_ty_minus", "MhBone_074"),
    ("L_Thigh_ty_plus", "MhBone_014"),
    ("L_Thigh_tz_minus", "MhBone_014"),
    ("L_Calf", "MhBone_015"),
    ("LCalfTwist", "MhBone_015"),
    ("LCalfTwist1", "MhBone_015"),
    ("L_Calf_ty_minus", "MhBone_015"),
    ("L_Calf_ty_plus", "MhBone_075"),
    ("L_Foot", "MhBone_016"),
    ("L_Foot_ty_minus", "MhBone_016"),
    ("L_Foot_ty_plus", "MhBone_016"),
    ("L_Toe0", "MhBone_017"),
    
    # 右腿
    ("R_Thigh", "MhBone_018"),
    ("RThighTwist", "MhBone_018"),
    ("RThighTwist1", "MhBone_018"),
    ("R_Thigh_ty_minus", "MhBone_076"),
    ("R_Thigh_ty_plus", "MhBone_018"),
    ("R_Thigh_tz_minus", "MhBone_018"),
    ("R_Calf", "MhBone_019"),
    ("RCalfTwist", "MhBone_019"),
    ("RCalfTwist1", "MhBone_019"),
    ("R_Calf_ty_minus", "MhBone_019"),
    ("R_Calf_ty_plus", "MhBone_077"),
    ("R_Foot", "MhBone_020"),
    ("R_Foot_ty_minus", "MhBone_020"),
    ("R_Foot_ty_plus", "MhBone_020"),
    ("R_Toe0", "MhBone_021"),
    
    # 头部
    ("face_Head", "MhBone_004"),
    
    # 面部细节骨骼
    ## 眉毛
    ("browLf01Joint", "MhBone_308"),
    ("browLf02Joint", "MhBone_308"),
    ("browLf03Joint", "MhBone_307"),
    ("browLf04Joint", "MhBone_306"),
    ("browLf05Joint", "MhBone_305"),
    ("browLineLfUp01Joint", "MhBone_316"),
    ("browLineLfUp02Joint", "MhBone_317"),
    ("browLineLfUp03Joint", "MhBone_318"),
    ("browLineLf01Joint", "MhBone_320"),
    ("browLineLf02Joint", "MhBone_321"),
    ("browLineLf03Joint", "MhBone_322"),
    
    ("browRt01Joint", "MhBone_310"),
    ("browRt02Joint", "MhBone_310"),
    ("browRt03Joint", "MhBone_311"),
    ("browRt04Joint", "MhBone_312"),
    ("browRt05Joint", "MhBone_313"),
    ("browLineRtUp01Joint", "MhBone_329"),
    ("browLineRtUp02Joint", "MhBone_330"),
    ("browLineRtUp03Joint", "MhBone_331"),
    ("browLineRf01Joint", "MhBone_333"),
    ("browLineRf02Joint", "MhBone_334"),
    ("browLineRf03Joint", "MhBone_335"),
    
    
    ## 眼睛
    ("faceLfIrisJoint", "MhBone_315"),
    ("faceLfHighlightJoint", "MhBone_315"),
    ("faceLfHighlightJointA", "MhBone_315"),
    ("faceLfHighlightJointB", "MhBone_315"),
    ("faceLfPupilJoint", "MhBone_315"),
    ("eyeLf01Joint", "MhBone_319"),
    ("eyeLf02Joint", "MhBone_320"),
    ("eyeLf03Joint", "MhBone_321"),
    ("eyeLf03IrissdJoint", "MhBone_321"),
    ("eyeLf04Joint", "MhBone_322"),
    ("eyeLf01EyelashJoint", "MhBone_319"),
    ("eyeLf02EyelashJoint", "MhBone_320"),
    ("eyeLf03EyelashJoint", "MhBone_321"),
    ("eyeLf04EyelashJoint", "MhBone_322"),
    ("eyeLf05Joint", "MhBone_323"),
    ("eyeLf05EyelashJoint", "MhBone_323"),
    ("eyeLf06Joint", "MhBone_324"),
    ("eyeLf07Joint", "MhBone_325"),
    ("eyeLf08Joint", "MhBone_326"),
    
    ("faceRtIrisJoint", "MhBone_328"),
    ("faceRtHighlightJoint", "MhBone_328"),
    ("faceRtHighlightJointA", "MhBone_328"),
    ("faceRtHighlightJointB", "MhBone_328"),
    ("faceRtPupilJoint", "MhBone_328"),
    ("eyeRt01Joint", "MhBone_332"),
    ("eyeRt02Joint", "MhBone_333"),
    ("eyeRt03Joint", "MhBone_334"),
    ("eyeRt03IrissdJoint", "MhBone_334"),
    ("eyeRt04Joint", "MhBone_335"),
    ("eyeRt01EyelashJoint", "MhBone_332"),
    ("eyeRt02EyelashJoint", "MhBone_333"),
    ("eyeRt03EyelashJoint", "MhBone_334"),
    ("eyeRt04EyelashJoint", "MhBone_335"),
    ("eyeRt05Joint", "MhBone_336"),
    ("eyeRt05EyelashJoint", "MhBone_336"),
    ("eyeRt06Joint", "MhBone_337"),
    ("eyeRt07Joint", "MhBone_338"),
    ("eyeRt08Joint", "MhBone_339"),
    
    
    ## 鼻子
    ("NoseMd01Joint", "MhBone_344"),
    
    ## 嘴巴
    ("lineJoint", "MhBone_004"),
    ("faceMdToothUpJoint", "MhBone_004"),
    ("line_toothJoint", "MhBone_004"),
    ("faceMdToothDnJoint", "MhBone_372"),
    ("TongueMd04Joint", "MhBone_372"),
    ("TongueMd03Joint", "MhBone_372"),
    ("TongueMd02Joint", "MhBone_372"),
    ("TongueMd01Joint", "MhBone_373"),
    
    ("lipLdn1Joint", "MhBone_384"),
    ("lipLdn2Joint", "MhBone_386"),
    ("lipLdn3Joint", "MhBone_387"),
    ("lipLdn4Joint", "MhBone_387"),
    ("lipMdnJoint", "MhBone_388"),
    ("lipRdn1Joint", "MhBone_385"),
    ("lipRdn2Joint", "MhBone_390"),
    ("lipRdn3Joint", "MhBone_389"),
    ("lipRdn4Joint", "MhBone_389"),
    
    ("lipLup1Joint", "MhBone_384"),
    ("lipLup2Joint", "MhBone_383"),
    ("lipLup3Joint", "MhBone_382"),
    ("lipLup4Joint", "MhBone_382"),
    ("lipMupJoint", "MhBone_381"),
    ("lipRup1Joint", "MhBone_385"),
    ("lipRup2Joint", "MhBone_379"),
    ("lipRup3Joint", "MhBone_380"),
    ("lipRup4Joint", "MhBone_380"),
    
    ("faceMdJawDnJoint", "MhBone_407"),
    
    ## 其他面部细节
    ("faceLfCheekOtDnJoint", "MhBone_408"),
    ("faceLfCheekOtInJoint", "MhBone_409"),
    ("faceLfCheekOtJoint", "MhBone_396"),
    ("faceLfCheekOtUpJoint", "MhBone_410"),
    ("faceRtCheekOtDnJoint", "MhBone_406"),
    ("faceRtCheekOtInJoint", "MhBone_412"),
    ("faceRtCheekOtJoint", "MhBone_402"),
    ("faceRtCheekOtUpJoint", "MhBone_413"),
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