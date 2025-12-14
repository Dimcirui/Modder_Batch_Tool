import bpy

# Endfield 骨骼名 -> MHWorld MhBone
# 使用列表以保持优先级顺序
_ENDFIELD_MAP_LIST = [
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

def _process_endfield_bones(obj):
    """
    处理 Endfield 骨骼组:
    1. 如果目标组不存在: 直接重命名源组。
    2. 如果目标组已存在: 将源组权重合并(Add)到目标组，然后删除源组。
    """
    vgroups = obj.vertex_groups
    processed = set()  # 记录已处理的目标名称
    
    for src_name, dst_name in _ENDFIELD_MAP_LIST:
        # 如果源顶点组不存在，跳过
        if src_name not in vgroups:
            continue
        
        # 如果这个目标名称已经被处理过（说明是重复映射）
        if dst_name in processed and dst_name in vgroups:
            # 合并权重
            src_vg = vgroups[src_name]
            dst_vg = vgroups[dst_name]
            
            for vert in obj.data.vertices:
                try:
                    src_weight = src_vg.weight(vert.index)
                    try:
                        dst_weight = dst_vg.weight(vert.index)
                        dst_vg.add([vert.index], src_weight + dst_weight, 'REPLACE')
                    except RuntimeError:
                        dst_vg.add([vert.index], src_weight, 'REPLACE')
                except RuntimeError:
                    pass
            
            # 删除源组
            vgroups.remove(src_vg)
        else:
            # 第一次遇到这个目标名称，直接重命名
            vgroups[src_name].name = dst_name
            processed.add(dst_name)
class MHW_OT_EndfieldToMHW(bpy.types.Operator):
    """Convert Endfield vertex groups to MHWorld format (Merge weights for duplicates)"""
    bl_idname = "mhw.endfield_to_mhw"
    bl_label = "Endfield to MHWorld"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.active_object is not None and 
                context.active_object.type == 'MESH')

    def execute(self, context):
        count = 0
        # 确保处于 Object 模式以应用修改器
        original_mode = context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for obj in context.selected_objects:
            if obj.type == "MESH":
                # 将当前物体设为激活，以便 modifier_apply 正常工作
                context.view_layer.objects.active = obj
                _process_endfield_bones(obj)
                count += 1
        
        # 恢复原始模式
        if original_mode != 'OBJECT':
            try:
                bpy.ops.object.mode_set(mode=original_mode)
            except:
                pass
            
        self.report({'INFO'}, f"Processed {count} Endfield mesh(es)")
        return {'FINISHED'}

classes = [
    MHW_OT_EndfieldToMHW,
]