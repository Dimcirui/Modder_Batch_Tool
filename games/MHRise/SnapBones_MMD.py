import bpy

# MMD 日文骨骼 -> MHRise (用于骨骼吸附)
_SNAP_MAP_UNFIXED = [
    # 躯干
    ("下半身", "Waist_00"),
    ("上半身", "Spine_00"),
    ("上半身2", "Spine_01"),
    ("首", "Neck_00"),
    ("首", "Neck_00_S"),
    ("頭", "Head_00"),
    
    # 左臂
    ("肩.L", "L_Arm_00"),
    ("腕.L", "L_Arm_01"),
    ("ひじ.L", "L_Arm_02"),
    ("手首.L", "L_Arm_03"),
    ("手首.L", "L_Weapon_00"),
    ("親指０.L", "L_Finger_00"),
    ("親指１.L", "L_Finger_01"),
    ("親指２.L", "L_Finger_02"),
    ("人指１.L", "L_Finger_03"),
    ("人指２.L", "L_Finger_04"),
    ("人指３.L", "L_Finger_05"),
    ("中指１.L", "L_Finger_06"),
    ("中指２.L", "L_Finger_07"),
    ("中指３.L", "L_Finger_08"),
    ("手首.L", "L_Finger_09"),
    ("薬指１.L", "L_Finger_10"),
    ("薬指２.L", "L_Finger_11"),
    ("薬指３.L", "L_Finger_12"),
    ("小指１.L", "L_Finger_13"),
    ("小指２.L", "L_Finger_14"),
    ("小指３.L", "L_Finger_15"),
    
    # 右臂
    ("肩.R", "R_Arm_00"),
    ("腕.R", "R_Arm_01"),
    ("ひじ.R", "R_Arm_02"),
    ("手首.R", "R_Arm_03"),
    ("手首.R", "R_Weapon_00"),
    ("親指０.R", "R_Finger_00"),
    ("親指１.R", "R_Finger_01"),
    ("親指２.R", "R_Finger_02"),
    ("人指１.R", "R_Finger_03"),
    ("人指２.R", "R_Finger_04"),
    ("人指３.R", "R_Finger_05"),
    ("中指１.R", "R_Finger_06"),
    ("中指２.R", "R_Finger_07"),
    ("中指３.R", "R_Finger_08"),
    ("手首.R", "R_Grip_00"),
    ("薬指１.R", "R_Finger_09"),
    ("薬指２.R", "R_Finger_10"),
    ("薬指３.R", "R_Finger_11"),
    ("小指１.R", "R_Finger_12"),
    ("小指２.R", "R_Finger_13"),
    ("小指３.R", "R_Finger_14"),
    
    # 腿部
    ("足D.L", "L_Leg_00"),
    ("ひざD.L", "L_Leg_01"),
    ("足首D.L", "L_Leg_02"),
    ("足先EX.L", "L_Leg_03"),
    ("足D.R", "R_Leg_00"),
    ("ひざD.R", "R_Leg_01"),
    ("足首D.R", "R_Leg_02"),
    ("足先EX.R", "R_Leg_03"),
    
    # 辅助骨骼
    ("腕.L", "L_Arm_00_W"),
    ("ひじ.L", "L_Arm_01_W"),
    ("腕.L", "L_Arm_01_T"),
    ("手捩.L", "L_Arm_02_T"),
    ("腕.R", "R_Arm_00_W"),
    ("ひじ.R", "R_Arm_01_W"),
    ("腕.R", "R_Arm_01_T"),
    ("手捩.R", "R_Arm_02_T"),
    ("足D.L", "L_Leg_00_W"),
    ("ひざD.L", "L_Leg_01_W"),
    ("足首D.L", "L_Leg_02_T"),
    ("足D.R", "R_Leg_00_W"),
    ("ひざD.R", "R_Leg_01_W"),
    ("足首D.R", "R_Leg_02_T"),
]

# MMD 英文骨骼映射
_SNAP_MAP_FIXED = [
    # 躯干
    ("Hips", "Waist_00"),
    ("Spine", "Spine_00"),
    ("Chest", "Spine_01"),
    ("Neck", "Neck_00"),
    ("Neck", "Neck_00_S"),
    ("Head", "Head_00"),
    
    # 左臂
    ("Left shoulder", "L_Arm_00"),
    ("Left arm", "L_Arm_01"),
    ("Left elbow", "L_Arm_02"),
    ("Left wrist", "L_Arm_03"),
    ("Left wrist", "L_Weapon_00"),
    ("Thumb0_L", "L_Finger_00"),
    ("Thumb1_L", "L_Finger_01"),
    ("Thumb2_L", "L_Finger_02"),
    ("IndexFinger1_L", "L_Finger_03"),
    ("IndexFinger2_L", "L_Finger_04"),
    ("IndexFinger3_L", "L_Finger_05"),
    ("MiddleFinger1_L", "L_Finger_06"),
    ("MiddleFinger2_L", "L_Finger_07"),
    ("MiddleFinger3_L", "L_Finger_08"),
    ("Left wrist", "L_Finger_09"),
    ("RingFinger1_L", "L_Finger_10"),
    ("RingFinger2_L", "L_Finger_11"),
    ("RingFinger3_L", "L_Finger_12"),
    ("LittleFinger1_L", "L_Finger_13"),
    ("LittleFinger2_L", "L_Finger_14"),
    ("LittleFinger3_L", "L_Finger_15"),
    
    # 右臂
    ("Right shoulder", "R_Arm_00"),
    ("Right arm", "R_Arm_01"),
    ("Right elbow", "R_Arm_02"),
    ("Right wrist", "R_Arm_03"),
    ("Right wrist", "R_Weapon_00"),
    ("Thumb0_R", "R_Finger_00"),
    ("Thumb1_R", "R_Finger_01"),
    ("Thumb2_R", "R_Finger_02"),
    ("IndexFinger1_R", "R_Finger_03"),
    ("IndexFinger2_R", "R_Finger_04"),
    ("IndexFinger3_R", "R_Finger_05"),
    ("MiddleFinger1_R", "R_Finger_06"),
    ("MiddleFinger2_R", "R_Finger_07"),
    ("MiddleFinger3_R", "R_Finger_08"),
    ("Right wrist", "R_Grip_00"),
    ("RingFinger1_R", "R_Finger_09"),
    ("RingFinger2_R", "R_Finger_10"),
    ("RingFinger3_R", "R_Finger_11"),
    ("LittleFinger1_R", "R_Finger_12"),
    ("LittleFinger2_R", "R_Finger_13"),
    ("LittleFinger3_R", "R_Finger_14"),
    
    # 腿部
    ("Left leg", "L_Leg_00"),
    ("Left knee", "L_Leg_01"),
    ("Left ankle", "L_Leg_02"),
    ("Left toe", "L_Leg_03"),
    ("Right leg", "R_Leg_00"),
    ("Right knee", "R_Leg_01"),
    ("Right ankle", "R_Leg_02"),
    ("Right toe", "R_Leg_03"),
    
    # 辅助骨骼
    ("Left arm", "L_Arm_00_W"),
    ("Left elbow", "L_Arm_01_W"),
    ("Left arm", "L_Arm_01_T"),
    ("zHandTwist_L", "L_Arm_02_T"),
    ("Right arm", "R_Arm_00_W"),
    ("Right elbow", "R_Arm_01_W"),
    ("Right arm", "R_Arm_01_T"),
    ("zHandTwist_R", "R_Arm_02_T"),
    ("Left leg", "L_Leg_00_W"),
    ("Left knee", "L_Leg_01_W"),
    ("Left ankle", "L_Leg_02_T"),
    ("Right leg", "R_Leg_00_W"),
    ("Right knee", "R_Leg_01_W"),
    ("Right ankle", "R_Leg_02_T"),
]


def _snap_bones(context):
    """执行骨骼吸附"""
    original_bones = [b.name for b in context.active_object.data.bones]
    
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
        
        edit_bones.active = edit_bones[src_name]
        context.object.data.use_mirror_x = False
        bpy.ops.armature.select_all(action='DESELECT')
        edit_bones[src_name].select = True
        edit_bones[dst_name].select = True
        
        original_area = context.area.type
        context.area.type = 'VIEW_3D'
        bpy.ops.view3d.snap_selected_to_active()
        context.area.type = original_area
        
        # 特殊处理：脚趾骨骼 Y 轴位置修正
        if dst_name in ("L_Leg_03", "R_Leg_03"):
            edit_bones.active = edit_bones[dst_name]
            context.active_bone.head[1] = -104.611
            context.active_bone.tail[1] = -89.8527
        
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


class MHR_OT_SnapBonesMMD(bpy.types.Operator):
    """Snap MMD armature bones to MHRise armature positions"""
    bl_idname = "mhr.snap_bones_mmd"
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
    MHR_OT_SnapBonesMMD,
]