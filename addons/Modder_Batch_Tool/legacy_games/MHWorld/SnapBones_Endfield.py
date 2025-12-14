import bpy
import copy

# Endfield 骨骼 -> MHWorld MHBone 映射
# 包含冗余映射，逻辑上通过"先到先得"处理吸附
_SNAP_MAP_ENDFIELD = [
    # 躯干
    ("Pelvis", "MHBone_013"),
    ("Spine", "MHBone_001"),
    ("Spine1", "MHBone_001"),
    ("Spine2", "MHBone_002"),
    ("Neck", "MHBone_003"),
    ("Head", "MHBone_004"),
    
    # 左臂
    ("L_Clavicle", "MHBone_005"),
    ("LUpArmTwist", "MHBone_080"),
    ("LUpArmTwist1", "MHBone_080"),
    ("L_UpperArm", "MHBone_006"),
    ("L_UpperArm_ty_minus", "MHBone_006"),
    ("L_UpperArm_ty_plus", "MHBone_006"),
    ("L_UpperArm_tz_minus", "MHBone_006"),
    ("L_UpperArm_ty_plus", "MHBone_070"),
    ("L_Forearm", "MHBone_007"),
    ("L_ForeTwist", "MHBone_081"),
    ("L_ForeTwist1", "MHBone_081"),
    ("L_Hand", "MHBone_008"),
    ("L_Hand_ty_minus", "MHBone_008"),
    ("L_Hand_ty_plus", "MHBone_008"),
    ("L_Finger0", "MHBone_031"),
    ("L_Finger01", "MHBone_032"),
    ("L_Finger02", "MHBone_033"),
    ("L_Finger1", "MHBone_034"),
    ("L_Finger11", "MHBone_035"),
    ("L_Finger12", "MHBone_036"),
    ("L_Finger2", "MHBone_037"),
    ("L_Finger21", "MHBone_038"),
    ("L_Finger22", "MHBone_039"),
    ("L_Finger3", "MHBone_041"),
    ("L_Finger31", "MHBone_042"),
    ("L_Finger32", "MHBone_043"),
    ("L_Finger4", "MHBone_044"),
    ("L_Finger41", "MHBone_045"),
    ("L_Finger42", "MHBone_046"),
    
    # 右臂
    ("R_Clavicle", "MHBone_009"),
    ("RUpArmTwist", "MHBone_082"),
    ("RUpArmTwist1", "MHBone_082"),
    ("R_UpperArm", "MHBone_010"),
    ("R_UpperArm_ty_minus", "MHBone_010"),
    ("R_UpperArm_ty_plus", "MHBone_010"),
    ("R_UpperArm_tz_minus", "MHBone_010"),
    ("R_UpperArm_ty_plus", "MHBone_072"),
    ("R_Forearm", "MHBone_011"),
    ("R_ForeTwist", "MHBone_083"),
    ("R_ForeTwist1", "MHBone_083"),
    ("R_Hand", "MHBone_012"),
    ("R_Hand_ty_minus", "MHBone_012"),
    ("R_Hand_ty_plus", "MHBone_012"),
    ("R_Finger0", "MHBone_048"),
    ("R_Finger01", "MHBone_049"),
    ("R_Finger02", "MHBone_050"),
    ("R_Finger1", "MHBone_051"),
    ("R_Finger11", "MHBone_052"),
    ("R_Finger12", "MHBone_053"),
    ("R_Finger2", "MHBone_054"),
    ("R_Finger21", "MHBone_055"),
    ("R_Finger22", "MHBone_056"),
    ("R_Finger3", "MHBone_058"),
    ("R_Finger31", "MHBone_059"),
    ("R_Finger32", "MHBone_060"),
    ("R_Finger4", "MHBone_061"),
    ("R_Finger41", "MHBone_062"),
    ("R_Finger42", "MHBone_063"),
    
    # 左腿
    ("L_Thigh", "MHBone_014"),
    ("LThighTwist", "MHBone_014"),
    ("LThighTwist1", "MHBone_014"),
    ("L_Thigh_ty_minus", "MHBone_074"),
    ("L_Thigh_ty_plus", "MHBone_014"),
    ("L_Thigh_tz_minus", "MHBone_014"),
    ("L_Calf", "MHBone_015"),
    ("LCalfTwist", "MHBone_015"),
    ("LCalfTwist1", "MHBone_015"),
    ("L_Calf_ty_minus", "MHBone_015"),
    ("L_Calf_ty_plus", "MHBone_075"),
    ("L_Foot", "MHBone_016"),
    ("L_Foot_ty_minus", "MHBone_016"),
    ("L_Foot_ty_plus", "MHBone_016"),
    ("L_Toe0", "MHBone_017"),
    
    # 右腿
    ("R_Thigh", "MHBone_018"),
    ("RThighTwist", "MHBone_018"),
    ("RThighTwist1", "MHBone_018"),
    ("R_Thigh_ty_minus", "MHBone_076"),
    ("R_Thigh_ty_plus", "MHBone_018"),
    ("R_Thigh_tz_minus", "MHBone_018"),
    ("R_Calf", "MHBone_019"),
    ("RCalfTwist", "MHBone_019"),
    ("RCalfTwist1", "MHBone_019"),
    ("R_Calf_ty_minus", "MHBone_019"),
    ("R_Calf_ty_plus", "MHBone_077"),
    ("R_Foot", "MHBone_020"),
    ("R_Foot_ty_minus", "MHBone_020"),
    ("R_Foot_ty_plus", "MHBone_020"),
    ("R_Toe0", "MHBone_021"),
    
    # 头部
    ("face_Head", "MHBone_004"),
    
    # 面部细节骨骼
    ## 眉毛
    ("browLf01Joint", "MHBone_308"),
    ("browLf02Joint", "MHBone_308"),
    ("browLf03Joint", "MHBone_307"),
    ("browLf04Joint", "MHBone_306"),
    ("browLf05Joint", "MHBone_305"),
    ("browLineLfUp01Joint", "MHBone_316"),
    ("browLineLfUp02Joint", "MHBone_317"),
    ("browLineLfUp03Joint", "MHBone_318"),
    ("browLineLf01Joint", "MHBone_320"),
    ("browLineLf02Joint", "MHBone_321"),
    ("browLineLf03Joint", "MHBone_322"),
    
    ("browRt01Joint", "MHBone_310"),
    ("browRt02Joint", "MHBone_310"),
    ("browRt03Joint", "MHBone_311"),
    ("browRt04Joint", "MHBone_312"),
    ("browRt05Joint", "MHBone_313"),
    ("browLineRtUp01Joint", "MHBone_329"),
    ("browLineRtUp02Joint", "MHBone_330"),
    ("browLineRtUp03Joint", "MHBone_331"),
    ("browLineRf01Joint", "MHBone_333"),
    ("browLineRf02Joint", "MHBone_334"),
    ("browLineRf03Joint", "MHBone_335"),
    
    
    ## 眼睛
    ("faceLfIrisJoint", "MHBone_315"),
    ("faceLfHighlightJoint", "MHBone_315"),
    ("faceLfHighLightJointA", "MHBone_315"),
    ("faceLfHighlightJointB", "MHBone_315"),
    ("faceLfPupilJoint", "MHBone_315"),
    ("eyeLf01Joint", "MHBone_319"),
    ("eyeLf02Joint", "MHBone_320"),
    ("eyeLf03Joint", "MHBone_321"),
    ("eyeLf03IrissdJoint", "MHBone_321"),
    ("eyeLf04Joint", "MHBone_322"),
    ("eyeLf01EyelashJoint", "MHBone_319"),
    ("eyeLf02EyelashJoint", "MHBone_320"),
    ("eyeLf03EyelashJoint", "MHBone_321"),
    ("eyeLf04EyelashJoint", "MHBone_322"),
    ("eyeLf05Joint", "MHBone_323"),
    ("eyeLf05EyelashJoint", "MHBone_323"),
    ("eyeLf06Joint", "MHBone_324"),
    ("eyeLf07Joint", "MHBone_325"),
    ("eyeLf08Joint", "MHBone_326"),
    
    ("faceRtIrisJoint", "MHBone_328"),
    ("faceRtHighlightJoint", "MHBone_328"),
    ("faceRtHighLightJointA", "MHBone_328"),
    ("faceRtHighlightJointB", "MHBone_328"),
    ("faceRtPupilJoint", "MHBone_328"),
    ("eyeRt01Joint", "MHBone_332"),
    ("eyeRt02Joint", "MHBone_333"),
    ("eyeRt03Joint", "MHBone_334"),
    ("eyeRt03IrissdJoint", "MHBone_334"),
    ("eyeRt04Joint", "MHBone_335"),
    ("eyeRt01EyelashJoint", "MHBone_332"),
    ("eyeRt02EyelashJoint", "MHBone_333"),
    ("eyeRt03EyelashJoint", "MHBone_334"),
    ("eyeRt04EyelashJoint", "MHBone_335"),
    ("eyeRt05Joint", "MHBone_336"),
    ("eyeRt05EyelashJoint", "MHBone_336"),
    ("eyeRt06Joint", "MHBone_337"),
    ("eyeRt07Joint", "MHBone_338"),
    ("eyeRt08Joint", "MHBone_339"),
    
    
    ## 鼻子
    ("NoseMd01Joint", "MHBone_344"),
    
    ## 嘴巴
    ("lineJoint", "MHBone_004"),
    ("faceMdToothUpJoint", "MHBone_004"),
    ("line_toothJoint", "MHBone_004"),
    ("faceMdToothDnJoint", "MHBone_372"),
    ("TongueMd04Joint", "MHBone_372"),
    ("TongueMd03Joint", "MHBone_372"),
    ("TongueMd02Joint", "MHBone_372"),
    ("TongueMd01Joint", "MHBone_373"),
    
    ("lipLdn1Joint", "MHBone_384"),
    ("lipLdn2Joint", "MHBone_386"),
    ("lipLdn3Joint", "MHBone_387"),
    ("lipLdn4Joint", "MHBone_387"),
    ("lipMdnJoint", "MHBone_388"),
    ("lipRdn1Joint", "MHBone_385"),
    ("lipRdn2Joint", "MHBone_390"),
    ("lipRdn3Joint", "MHBone_389"),
    ("lipRdn4Joint", "MHBone_389"),
    
    ("lipLup1Joint", "MHBone_384"),
    ("lipLup2Joint", "MHBone_383"),
    ("lipLup3Joint", "MHBone_382"),
    ("lipLup4Joint", "MHBone_382"),
    ("lipMupJoint", "MHBone_381"),
    ("lipRup1Joint", "MHBone_385"),
    ("lipRup2Joint", "MHBone_379"),
    ("lipRup3Joint", "MHBone_380"),
    ("lipRup4Joint", "MHBone_380"),
    
    ("faceMdJawDnJoint", "MHBone_407"),
    
    ## 其他面部细节
    ("faceLfCheekOtDnJoint", "MHBone_408"),
    ("faceLfCheekOtInJoint", "MHBone_409"),
    ("faceLfCheekOtJoint", "MHBone_396"),
    ("faceLfCheekOtUpJoint", "MHBone_410"),
    ("faceRtCheekOtDnJoint", "MHBone_406"),
    ("faceRtCheekOtInJoint", "MHBone_412"),
    ("faceRtCheekOtJoint", "MHBone_402"),
    ("faceRtCheekOtUpJoint", "MHBone_413"),
]

def _snap_bones_endfield(context):
    """执行 Endfield 骨骼吸附"""
    # 保存原始骨骼名称 (Target armature)
    original_bones = [b.name for b in context.active_object.data.bones]
    
    # 合并骨架 (Assumes active is Target/MHW, selected includes Source/Endfield)
    bpy.ops.object.join()
    
    armature = context.active_object.data
    armature_name = armature.name
    all_bone_names = [b.name for b in armature.bones]
    
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = bpy.data.armatures[armature_name].edit_bones
    
    # 记录已处理的 Target 骨骼，防止重复吸附
    processed_targets = set()

    for src_name, dst_name in _SNAP_MAP_ENDFIELD:
        if src_name not in all_bone_names:
            continue
        if dst_name not in edit_bones:
            continue
        
        # 如果该 Target 骨骼已经由列表前排的 Source 骨骼吸附过，则跳过
        # 例如: Spine 已将 001 吸附到位，后续 Spine1 -> 001 将被忽略
        if dst_name in processed_targets:
            continue

        # 执行吸附: 将 Target 骨骼吸附到 Source 骨骼位置
        edit_bones.active = edit_bones[src_name]
        context.object.data.use_mirror_x = False
        bpy.ops.armature.select_all(action='DESELECT')
        edit_bones[src_name].select = True
        edit_bones[dst_name].select = True
        
        original_area = context.area.type
        context.area.type = 'VIEW_3D'
        bpy.ops.view3d.snap_selected_to_active()
        context.area.type = original_area
        
        processed_targets.add(dst_name)
        
        bpy.ops.armature.select_all(action='DESELECT')
    
    # 显示所有骨骼层
    if hasattr(context.object.data, 'layers'):
        for i in range(32):
            context.object.data.layers[i] = True
    else:
        for coll in armature.collections:
            coll.is_visible = True
    
    # 删除非原始骨骼 (即删除所有 Endfield 骨骼，包括 Spine1 等未参与吸附的骨骼)
    for bone_name in all_bone_names:
        if bone_name not in original_bones:
            if bone_name in edit_bones:
                edit_bones.active = edit_bones[bone_name]
                bpy.ops.armature.delete()
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return True

class MHW_OT_SnapBonesEndfield(bpy.types.Operator):
    """Snap Endfield armature bones to MHWorld armature positions"""
    bl_idname = "mhw.snap_bones_endfield"
    bl_label = "Snap Endfield Armature"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
            any(obj.type == "ARMATURE" for obj in context.selected_objects)
            and context.mode == 'OBJECT'
        )

    def execute(self, context):
        if _snap_bones_endfield(context):
            self.report({'INFO'}, "Endfield Bone snap completed")
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Snap failed")
            return {'CANCELLED'}

classes = [
    MHW_OT_SnapBonesEndfield,
]