import bpy
import copy
from ...operators.merge_bone import merge_weights


def Merge_MHWilds_Facial_Bones(ArmatureName):

    merge_bone_list = ['HeadAll_SCL', 'Ear_SCL', 'Head_SCL', 'C_ForeHead_LOD02', 'L_ForeHead_LOD01',
                       'R_ForeHead_LOD01', 'C_EyeBrow_LOD02', 'L_BetweenEyeBrow_LOD01', 'R_BetweenEyeBrow_LOD01',
                       'L_EyeBrow_LOD02', 'L_EyeBrow_A_LOD01', 'L_EyeBrow_B_LOD01', 'L_EyeBrow_C_LOD01',
                       'R_EyeBrow_LOD02', 'R_EyeBrow_A_LOD01', 'R_EyeBrow_B_LOD01', 'R_EyeBrow_C_LOD01',
                       'L_Eye_Master', 'L_EyeJ_LOD02', 'L_DoubleEyeLidJ_LOD02', 'L_DoubleEyeLid_LOD01',
                       'L_DoubleEyeLid_A_LOD00', 'L_DoubleEyeLid_B_LOD00', 'L_UpEyeLidJ_LOD02', 'L_UpEyeLid_LOD01',
                       'L_UpEyeLid_A_LOD00', 'L_UpEyeLid_B_LOD00', 'L_LoEyeLidJ_LOD02', 'L_LoEyeLid_LOD01',
                       'L_LoEyeLid_A_LOD00', 'L_LoEyeLid_B_LOD00', 'L_EyeBagJ_LOD02', 'L_EyeBagJ_LOD01',
                       'L_EyeBagJ_A_LOD00', 'L_EyeBagJ_B_LOD00', 'L_OuterEyeJ_LOD02', 'L_UpOuterEyeJ_LOD01',
                       'L_LoOuterEyeJ_LOD01', 'L_InnerEyeJ_LOD02', 'L_LoInnerEyeJ_LOD01', 'L_UpInnerEyeJ_LOD01',
                       'R_Eye_Master', 'R_EyeJ_LOD02', 'R_DoubleEyeLidJ_LOD02', 'R_DoubleEyeLid_LOD01',
                       'R_DoubleEyeLid_A_LOD00', 'R_DoubleEyeLid_B_LOD00', 'R_UpEyeLidJ_LOD02', 'R_UpEyeLid_LOD01',
                       'R_UpEyeLid_A_LOD00', 'R_UpEyeLid_B_LOD00', 'R_LoEyeLidJ_LOD02', 'R_LoEyeLid_LOD01',
                       'R_LoEyeLid_A_LOD00', 'R_LoEyeLid_B_LOD00', 'R_EyeBagJ_LOD02', 'R_EyeBagJ_LOD01',
                       'R_EyeBagJ_A_LOD00', 'R_EyeBagJ_B_LOD00', 'R_InnerEyeJ_LOD02', 'R_UpInnerEyeJ_LOD01',
                       'R_LoInnerEyeJ_LOD01', 'R_OuterEyeJ_LOD02', 'R_UpOuterEyeJ_LOD01', 'R_LoOuterEyeJ_LOD01',
                       'C_Nose_Master', 'C_Nose_LOD02', 'L_NoseNaso_LOD02', 'R_NoseNaso_LOD02',
                       'C_Nose_Master_LOD02', 'C_Nose_LOD01', 'L_Nose_LOD01', 'L_NoseUnder_LOD00', 'R_Nose_LOD01',
                       'R_NoseUnder_LOD00', 'L_Naso_LOD02', 'R_Naso_LOD02', 'L_CheekBone_LOD02',
                       'L_malarFat_A_LOD01', 'L_malarFat_B_LOD01', 'R_CheekBone_LOD02', 'R_malarFat_A_LOD01',
                       'R_malarFat_B_LOD01', 'L_NasoB_LOD02', 'R_NasoB_LOD02', 'L_Cheek_LOD02', 'L_Cheek_LOD01',
                       'C_Mouth_Master', 'C_upLip_LOD02', 'C_upLip_LOD01', 'C_upLip_T_LOD01', 'L_upLip_LOD02',
                       'L_upLip_LOD01', 'L_upLip_A_LOD01', 'L_upLip_A_LOD00', 'L_upLip_AT_LOD00', 'L_upLip_B_LOD01',
                       'L_upLip_B_LOD00', 'L_upLip_BT_LOD00', 'L_upLip_T_LOD01', 'R_upLip_LOD02', 'R_upLip_LOD01',
                       'R_upLip_A_LOD01', 'R_upLip_A_LOD00', 'R_upLip_AT_LOD00', 'R_upLip_B_LOD01',
                       'R_upLip_B_LOD00', 'R_upLip_BT_LOD00', 'R_upLip_T_LOD01', 'L_cornerLip_LOD02',
                       'L_cornerLip_A_LOD01', 'L_cornerLip_B_LOD01', 'L_cornerLipInner_LOD01', 'R_cornerLip_LOD02',
                       'R_cornerLip_A_LOD01', 'R_cornerLip_B_LOD01', 'R_cornerLipInner_LOD01', 'C_loLip_LOD02',
                       'C_loLip_LOD01', 'C_loLip_T_LOD01', 'L_loLip_LOD02', 'L_loLip_LOD01', 'L_loLip_A_LOD01',
                       'L_loLip_A_LOD00', 'L_loLip_AT_LOD00', 'L_loLip_B_LOD01', 'L_loLip_B_LOD00',
                       'L_loLip_BT_LOD00', 'L_loLip_T_LOD01', 'R_loLip_LOD02', 'R_loLip_LOD01', 'R_loLip_A_LOD01',
                       'R_loLip_A_LOD00', 'R_loLip_AT_LOD00', 'R_loLip_B_LOD01', 'R_loLip_B_LOD00',
                       'R_loLip_BT_LOD00', 'R_loLip_T_LOD01', 'C_Jaw_LOD02', 'C_Chin_LOD01', 'C_Chin_LOD00',
                       'L_JawLine_LOD01', 'L_JawLine_LOD00', 'R_JawLine_LOD01', 'R_JawLine_LOD00',
                       'C_TongueA_LOD01', 'C_TongueB_LOD01', 'R_TongueB_LOD00', 'C_TongueC_LOD01',
                       'L_TongueC_LOD00', 'R_TongueC_LOD00', 'L_TongueB_LOD00', 'LowerTeeth', 'C_UnderJaw_LOD02',
                       'L_UnderJaw_LOD02', 'R_UnderJaw_LOD02', 'L_Temporal_LOD01', 'R_Temporal_LOD01',
                       'L_Masseter_LOD01', 'R_Masseter_LOD01', 'R_Cheek_LOD02', 'R_Cheek_LOD01', 'HelmJoint_L_Hoho',
                       'HelmJoint_L_Era', 'HelmJoint_Mayu', 'HelmJoint_Ago', 'HelmJoint_R_Era', 'HelmJoint_R_Hoho',
                       'UpperTeeth', 'fcParam_000', 'fcParam_001', 'fcParam_002', 'fcParam_003', 'fcParam_004',
                       'fcParam_005', 'fcParam_006', 'fcParam_007', 'fcParam_008', 'fcParam_009', 'fcParam_010',
                       'fcParam_011', 'fcParam_012', 'fcParam_013', 'fcParam_014', 'fcParam_015', 'fcParam_016',
                       'fcParam_017', 'fcParam_018', 'fcParam_019', 'fcParam_020', 'fcParam_021', 'fcParam_022',
                       'fcParam_023', 'fcParam_024', 'fcParam_025', 'fcParam_026', 'fcParam_027', 'fcParam_028',
                       'fcParam_029', 'fcParam_030', 'fcParam_031', 'fcParam_032', 'fcParam_033', 'fcParam_034',
                       'fcParam_035', 'fcParam_036', 'fcParam_037', 'fcParam_038', 'fcParam_039', 'fcParam_040',
                       'fcParam_041', 'fcParam_042', 'fcParam_043', 'fcParam_044', 'fcParam_045', 'fcParam_046',
                       'fcParam_047', 'fcParam_048', 'fcParam_049', 'fcParam_050', 'fcParam_051', 'fcParam_052',
                       'fcParam_053', 'fcParam_054', 'fcParam_055', 'fcParam_056', 'fcParam_057', 'fcParam_058',
                       'fcParam_059', 'fcParam_060', 'fcParam_061', 'fcParam_062', 'fcParam_063', 'fcParam_064',
                       'fcParam_065', 'fcParam_066', 'fcParam_067', 'fcParam_068', 'fcParam_069', 'fcParam_070',
                       'fcParam_071', 'fcParam_072', 'fcParam_073', 'fcParam_074', 'fcParam_075', 'fcParam_076',
                       'fcParam_077', 'fcParam_078', 'fcParam_079', 'fcParam_080', 'fcParam_081', 'fcParam_082',
                       'fcParam_083', 'fcParam_084', 'fcParam_085', 'fcParam_086', 'fcParam_087', 'fcParam_088',
                       'fcParam_089', 'fcParam_090', 'fcParam_091', 'fcParam_092', 'fcParam_093', 'fcParam_094',
                       'fcParam_095', 'fcParam_096', 'fcParam_097', 'fcParam_098', 'fcParam_099', 'fcParam_100',
                       'fcParam_101', 'fcParam_102', 'fcParam_103', 'fcParam_104', 'fcParam_105', 'fcParam_106',
                       'fcParam_107', 'fcParam_108', 'fcParam_109', 'fcParam_110', 'fcParam_111', 'fcParam_112',
                       'fcParam_113', 'fcParam_114', 'fcParam_115', 'fcParam_116', 'fcParam_117', 'fcParam_118',
                       'fcParam_119', 'fcParam_120', 'fcParam_121', 'fcParam_122', 'fcParam_123', 'fcParam_124',
                       'fcParam_125', 'fcParam_126', 'fcParam_127', 'fcParam_128', 'fcParam_129', 'fcParam_130',
                       'fcParam_131', 'fcParam_132', 'fcParam_133', 'fcParam_134', 'fcParam_135', 'fcParam_136',
                       'fcParam_137', 'fcParam_138', 'fcParam_139', 'fcParam_140', 'fcParam_141', 'fcParam_142',
                       'fcParam_143', 'fcParam_144', 'fcParam_145', 'fcParam_146', 'fcParam_147', 'fcParam_148',
                       'fcParam_149', 'fcParam_150', 'fcParam_151', 'fcParam_152', 'fcParam_153', 'fcParam_154',
                       'fcParam_155', 'fcParam_156', 'fcParam_157', 'fcParam_158', 'fcParam_159', 'fcParam_160',
                       'fcParam_161', 'fcParam_162', 'fcParam_163', 'fcParam_164', 'fcParam_165', 'fcParam_166',
                       'fcParam_167', 'fcParam_168', 'fcParam_169', 'fcParam_170', 'fcParam_171', 'fcParam_172',
                       'fcParam_173', 'fcParam_174', 'fcParam_175', 'fcParam_176', 'fcParam_177', 'fcParam_178',
                       'fcParam_179', 'fcParam_180', 'fcParam_181', 'fcParam_182', 'fcParam_183', 'fcParam_184',
                       'fcParam_185', 'fcParam_186', 'fcParam_187', 'fcParam_188', 'fcParam_189', 'fcParam_190',
                       'fcParam_191', 'fcParam_192', 'fcParam_193', 'fcParam_194', 'fcParam_195', 'fcParam_196',
                       'fcParam_197', 'fcParam_198', 'fcParam_199', 'fcParam_200']

    bpy.ops.armature.select_all(action='DESELECT')
    for mergebone in merge_bone_list:
        bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[
            mergebone]
        bpy.ops.object.select_pattern(pattern=mergebone, case_sensitive=False, extend=True)

    armature = bpy.context.object

    # Find which bones to work on and put their name and their parent in a list
    parenting_list = {}
    for bone in bpy.context.selected_editable_bones:
        parent = bone.parent
        while parent and parent.parent and parent in bpy.context.selected_editable_bones:
            parent = parent.parent
        if not parent:
            continue
        parenting_list[bone.name] = parent.name

    # Merge all the bones in the parenting list
    merge_weights(armature, parenting_list)
    bpy.ops.armature.select_all(action='DESELECT')


class MHWildstpose(bpy.types.Operator):
    bl_idname = "mbt.mhwilds_tpose"
    bl_label = "convert to t-pose"
    bl_description = "Convert MHWilds character armature to t-pose.\nConsidering some common bone names, this can also be applied to npcs"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.selected_objects is not None:
            for obj in bpy.context.selected_objects:
                return obj.type == "ARMATURE"

    def execute(self, context):
        bone_list = ['L_UpperArm', 'L_Forearm', 'L_Hand', 'L_HandRZ_HJ_00', 'L_IndexF1', 'L_IndexF2', 'L_IndexF3',
                     'L_IndexF_HJ_03', 'L_IndexF_HJ_02', 'L_IndexF_HJ_00', 'L_IndexF_HJ_01', 'L_IndexF_HJ_04',
                     'L_MiddleF1', 'L_MiddleF2', 'L_MiddleF3', 'L_MiddleF_HJ_03', 'L_MiddleF_HJ_02', 'L_MiddleF_HJ_00',
                     'L_MiddleF_HJ_01', 'L_MiddleF_HJ_04', 'L_Palm', 'L_RingF1', 'L_RingF2', 'L_RingF3',
                     'L_RingF_HJ_03', 'L_RingF_HJ_02', 'L_RingF_HJ_00', 'L_RingF_HJ_01', 'L_RingF_HJ_04', 'L_PinkyF1',
                     'L_PinkyF2', 'L_PinkyF3', 'L_PinkyF_HJ_03', 'L_PinkyF_HJ_02', 'L_PinkyF_HJ_00', 'L_PinkyF_HJ_01',
                     'L_PinkyF_HJ_04', 'L_Hand_HJ_01', 'L_Hand_HJ_00', 'L_ForearmTwist_HJ_02', 'L_ForearmRY_HJ_00',
                     'L_ForearmRY_HJ_01', 'L_ForearmTwist_HJ_01', 'L_ForearmTwist_HJ_00', 'L_Elbow_HJ_00',
                     'L_UpperArmTwist_HJ_01', 'L_Triceps_HJ_00', 'L_Biceps_HJ_00', 'L_Biceps_HJ_01',
                     'L_UpperArmTwist_HJ_02', 'L_Deltoid_HJ_00', 'L_Deltoid_HJ_01', 'L_Deltoid_HJ_02', 'R_UpperArm',
                     'R_Forearm', 'R_Hand', 'R_HandRZ_HJ_00', 'R_IndexF1', 'R_IndexF2', 'R_IndexF3', 'R_IndexF_HJ_03',
                     'R_IndexF_HJ_02', 'R_IndexF_HJ_00', 'R_IndexF_HJ_01', 'R_IndexF_HJ_04', 'R_MiddleF1', 'R_MiddleF2',
                     'R_MiddleF3', 'R_MiddleF_HJ_03', 'R_MiddleF_HJ_02', 'R_MiddleF_HJ_00', 'R_MiddleF_HJ_01',
                     'R_MiddleF_HJ_04', 'R_Palm', 'R_RingF1', 'R_RingF2', 'R_RingF3', 'R_RingF_HJ_03', 'R_RingF_HJ_02',
                     'R_RingF_HJ_00', 'R_RingF_HJ_01', 'R_RingF_HJ_04', 'R_PinkyF1', 'R_PinkyF2', 'R_PinkyF3',
                     'R_PinkyF_HJ_03', 'R_PinkyF_HJ_02', 'R_PinkyF_HJ_00', 'R_PinkyF_HJ_01', 'R_PinkyF_HJ_04',
                     'R_Hand_HJ_01', 'R_Hand_HJ_00', 'R_ForearmTwist_HJ_02', 'R_ForearmRY_HJ_00', 'R_ForearmRY_HJ_01',
                     'R_ForearmTwist_HJ_01', 'R_ForearmTwist_HJ_00', 'R_Elbow_HJ_00', 'R_UpperArmTwist_HJ_01',
                     'R_Triceps_HJ_00', 'R_Biceps_HJ_00', 'R_Biceps_HJ_01', 'R_UpperArmTwist_HJ_02', 'R_Deltoid_HJ_00',
                     'R_Deltoid_HJ_01', 'R_Deltoid_HJ_02', 'L_Thigh', 'L_Knee', 'L_Shin', 'L_Foot', 'L_Instep', 'L_Toe',
                     'L_Foot_HJ_00', 'L_Calf_HJ_00', 'L_Shin_HJ_00', 'L_Shin_HJ_01', 'L_Knee_HJ_00', 'L_KneeRX_HJ_00','L_ThighTwist_HJ_00',
                     'L_Foot_HJ_00', 'L_Calf_HJ_00', 'L_Shin_HJ_00', 'L_Shin_HJ_01', 'L_Knee_HJ_00', 'L_KneeRX_HJ_00',
                     'L_ThighTwist_HJ_01', 'L_ThighTwist_HJ_02', 'R_Thigh', 'R_Knee', 'R_Shin', 'R_Foot', 'R_Instep',
                     'R_Toe', 'R_Foot_HJ_00', 'R_Calf_HJ_00', 'R_Shin_HJ_00', 'R_Shin_HJ_01', 'R_KneeRX_HJ_00',
                     'R_Knee_HJ_00', 'R_ThighTwist_HJ_00', 'R_ThighTwist_HJ_01', 'R_ThighTwist_HJ_02', 'L_ThighRZ_HJ_00', 'L_ThighRZ_HJ_01',
                     'R_ThighRZ_HJ_00', 'R_ThighRZ_HJ_01', 'L_Hip_HJ_00', 'L_Hip_HJ_01', 'R_Hip_HJ_00', 'R_Hip_HJ_01',
                     'L_ThighRX_HJ_00', 'L_ThighRX_HJ_01', 'R_ThighRX_HJ_00', 'R_ThighRX_HJ_01']

        ArmatureObj = bpy.context.active_object
        ArmatureName = ArmatureObj.data.name

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='DESELECT')

        for bone in bone_list:
            bpy.ops.object.select_pattern(pattern=bone, case_sensitive=False, extend=True)

        for i in range(len(bpy.context.selected_pose_bones)):
            zero = copy.deepcopy(bpy.context.selected_pose_bones[i].matrix)

            zero[0][0] = 1.0
            zero[0][1] = 0.0
            zero[0][2] = 0.0
            zero[1][0] = 0.0
            zero[1][1] = 0.0
            zero[1][2] = -1.0
            zero[2][0] = 0.0
            zero[2][1] = 1.0
            zero[2][2] = 0.0
            zero[3][0] = 0.0
            zero[3][1] = 0.0
            zero[3][2] = 0.0
            zero[3][3] = 1.0

            bpy.context.selected_pose_bones[i].matrix = zero
            bpy.context.view_layer.update()

        bpy.ops.object.mode_set(mode='OBJECT')
        if ArmatureObj.children:
            #若有某些子级网格对象在当前视图层为隐藏状态，则强制将其设为显示状态
            for child in ArmatureObj.children:
                child.hide_set(False)
            bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE', extend=True)
            bpy.ops.object.convert(target='MESH')

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.pose.armature_apply(selected=True)
        bpy.ops.pose.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')

        if ArmatureObj.children:
            bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
            modifier = bpy.context.active_object.modifiers.new(name="", type='ARMATURE')
            modifier.object = ArmatureObj
            bpy.ops.object.make_links_data(type='MODIFIERS')
            bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)

        bpy.ops.object.select_hierarchy(direction='CHILD', extend=True)
        bpy.context.view_layer.objects.active = ArmatureObj

        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}


classes = [MHWildstpose]
