import bpy
import importlib
import os
from ...operators.general_function import showErrorMessageBox


class MHWildsOpenDictionaryFolder(bpy.types.Operator):
    bl_label = "open dictionary folder"
    bl_description = "Open the dictionary folder in file explorer"
    bl_idname = "mbt.mhwilds_open_dictionary_folder"

    def execute(self, context):
        presetsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bonenamelist")
        os.startfile(presetsPath)
        return {'FINISHED'}


class MHWildssnapbone(bpy.types.Operator):
    bl_idname = "mbt.mhwilds_snapbone"
    bl_label = "absorb bones"
    bl_description = "Absorb each bone in the game skeleton to the corresponding bone position in the external model skeleton." \
                     "\nSome bones will undergo additional position corrections after adsorption." \
                     "\nThe physical bones will also be merged into the parent"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.selected_objects:
            return False
        for obj in context.selected_objects:
            if obj.type != "ARMATURE":
                return False
        return True

    def execute(self, context):
        enumValue = bpy.context.scene.mbt_toolpanel.MHWildsBoneList
        file_name, file_extension = os.path.splitext(os.path.basename(enumValue))

        preset_module = importlib.import_module(f".bonenamelist.{file_name}", package=__name__)

        if "preset_module" in locals():
            importlib.reload(preset_module)

        fixed_name_list = preset_module.snap_bone_fixed_name_list
        rename_name_list = preset_module.rename_vg_fixed_name_list


        # 需要修正位置的骨骼
        fix_neck_bone = ['Neck_1', 'HeadRX_HJ_01', 'Neck_1_HJ_00']
        fix_spine0_bone = ['Spine_0', 'Spine_0_HJ_00']
        fix_spine2_bone = ['Spine_2', 'Spine_2_HJ_00']
        fix_shin_bone = ['L_Shin', 'R_Shin']
        fix_instep_bone = ['L_Instep', 'R_Instep']

        #若选中的骨架多于两个，则报错
        if len(context.selected_objects) > 2:
            showErrorMessageBox(
                "There are too many skeletons selected. Please select only two skeletons.")
        else:
            #吸附骨骼
            bpy.ops.object.mode_set(mode='OBJECT')

            #区分选中的两个骨架中哪个是外部骨架，哪个是MHWilds骨架
            armature_mhwilds = None
            armature_other = None
            for obj in bpy.context.selected_objects:
                if obj.type == 'ARMATURE' and obj.get("MBT_Armature_Type") == "MHWilds":
                    armature_mhwilds = obj
                else:
                    if armature_other is None:
                        armature_other = obj
            #判定选中的两个骨架中，是否同时存在外部骨架和游戏骨架
            both_exist = armature_mhwilds is not None and armature_other is not None
            #若不同时存在，则报错
            if not both_exist:
                showErrorMessageBox(
                    "The selected skeletons doesn't contain both the external skeleton and MHWilds skeleton.")
            else:
                #获取并保存复制骨架中所有骨骼的名称
                name_other = [bone.name for bone in armature_other.data.bones]
                #用字典中的几个骨骼名来判定选择的字典是否匹配当前选中的外部骨架
                if rename_name_list[0][0] in name_other and rename_name_list[1][0] in name_other and rename_name_list[2][0] in name_other and rename_name_list[4][0] in name_other and rename_name_list[6][0] in name_other:
                    for name_pair in rename_name_list:
                        if name_pair[0] in name_other:
                            name_other.remove(name_pair[0])

                    #复制一个外部骨架对象出来用于吸附
                    armature_other_copy = armature_other.copy()
                    armature_other_copy.data = armature_other.data.copy()
                    armature_other_copy.name = f"{armature_other.name}_copy"
                    bpy.context.collection.objects.link(armature_other_copy)

                    #激活并选中MHWilds骨架，然后与复制的外部骨架合并在一起
                    bpy.context.view_layer.objects.active = armature_mhwilds
                    bones = bpy.context.active_object.data.bones
                    name_ori = [bone.name for bone in bones]
                    bpy.ops.object.select_all(action='DESELECT')
                    armature_other_copy.select_set(True)
                    armature_mhwilds.select_set(True)
                    bpy.ops.object.join()

                    #获取并保存合并后骨架中所有骨骼的名称
                    ArmatureName = bpy.context.active_object.data.name
                    bones = bpy.context.active_object.data.bones
                    name_in = [bone.name for bone in bones]

                    bpy.ops.object.mode_set(mode='EDIT')

                    for bone_name in rename_name_list:
                        bone1_name, bone2_name = bone_name
                        if bone1_name in name_in and bone2_name in name_in:
                            bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[
                                bone2_name]
                            bpy.context.object.data.use_mirror_x = False
                            bpy.ops.armature.select_all(action='DESELECT')
                            bpy.ops.object.select_pattern(pattern=bone2_name, case_sensitive=False, extend=True)
                            bpy.ops.object.select_pattern(pattern=bone1_name, case_sensitive=False, extend=True)
                            bpy.ops.armature.parent_set(type='OFFSET')
                            bpy.ops.armature.select_all(action='DESELECT')

                    for bone_name in fixed_name_list:
                        bone1_name, bone2_name = bone_name
                        #仅当字典中的两列骨骼名都存在于合并后的骨架中时才进行吸附操作
                        if bone1_name in name_in and bone2_name in name_in:
                            bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[
                                bone1_name]
                            bpy.context.object.data.use_mirror_x = False
                            bpy.ops.armature.select_all(action='DESELECT')
                            bpy.ops.object.select_pattern(pattern=bone1_name, case_sensitive=False, extend=True)
                            bpy.ops.object.select_pattern(pattern=bone2_name, case_sensitive=False, extend=True)
                            bpy.context.area.type = 'VIEW_3D'
                            bpy.ops.view3d.snap_selected_to_active()
                            bpy.ops.armature.select_all(action='DESELECT')

                    # 修正骨骼，Neck_1应当位于Head与Neck_0的中点
                    if 'Head' in name_in and 'Neck_0' in name_in:
                        bone1 = bpy.data.armatures[ArmatureName].edit_bones['Head']
                        bone2 = bpy.data.armatures[ArmatureName].edit_bones['Neck_0']

                        center_x = (bone1.head.x + bone2.head.x) / 2
                        center_y = (bone1.head.y + bone2.head.y) / 2
                        center_z = (bone1.head.z + bone2.head.z) / 2

                        center_point = (center_x, center_y, center_z)

                        for fnb in fix_neck_bone:
                            bone = bpy.data.armatures[ArmatureName].edit_bones[fnb]
                            original_length = (bone.tail - bone.head).length
                            direction = (bone.tail - bone.head).normalized()
                            bone.head = center_point
                            bone.tail = bone.head + direction * original_length

                    # 修正骨骼，若mmd模型骨架没有Upper Chest骨骼，则Spine_2移动到Spine_1与Neck_0的中点
                    if 'Upper Chest' not in name_in:
                        bone1 = bpy.data.armatures[ArmatureName].edit_bones['Spine_1']
                        bone2 = bpy.data.armatures[ArmatureName].edit_bones['Neck_0']

                        if bone1 and bone2:
                            center_x = (bone1.head.x + bone2.head.x) / 2
                            center_y = (bone1.head.y + bone2.head.y) / 2
                            center_z = (bone1.head.z + bone2.head.z) / 2

                            center_point = (center_x, center_y, center_z)

                        for fs2b in fix_spine2_bone:
                            bone = bpy.data.armatures[ArmatureName].edit_bones[fs2b]
                            original_length = (bone.tail - bone.head).length
                            direction = (bone.tail - bone.head).normalized()
                            bone.head = center_point
                            bone.tail = bone.head + direction * original_length

                    # 修正骨骼，Instep应位于Foot与Toe的中点，额外修正Z轴坐标与Toe平齐，即在脚底
                    if 'L_Foot' in name_in and 'L_Toe' in name_in:
                        bone1 = bpy.data.armatures[ArmatureName].edit_bones['L_Foot']
                        bone2 = bpy.data.armatures[ArmatureName].edit_bones['L_Toe']

                        bone2_length = (bone2.tail - bone2.head).length
                        bone2.head.z = 0.019999
                        direction = (bone2.tail - bone2.head).normalized()
                        bone2.tail = bone2.head + direction * bone2_length

                        center_x = (bone1.head.x + bone2.head.x) / 2
                        center_y = (bone1.head.y + bone2.head.y) / 2
                        center_z = bone2.head.z

                        center_point = (center_x, center_y, center_z)

                        bone = bpy.data.armatures[ArmatureName].edit_bones[fix_instep_bone[0]]
                        original_length = (bone.tail - bone.head).length
                        direction = (bone.tail - bone.head).normalized()
                        bone.head = center_point
                        bone.tail = bone.head + direction * original_length

                    if 'R_Foot' in name_in and 'R_Toe' in name_in:
                        bone1 = bpy.data.armatures[ArmatureName].edit_bones['R_Foot']
                        bone2 = bpy.data.armatures[ArmatureName].edit_bones['R_Toe']

                        bone2_length = (bone2.tail - bone2.head).length
                        bone2.head.z = 0.019999
                        direction = (bone2.tail - bone2.head).normalized()
                        bone2.tail = bone2.head + direction * bone2_length

                        center_x = (bone1.head.x + bone2.head.x) / 2
                        center_y = (bone1.head.y + bone2.head.y) / 2
                        center_z = bone2.head.z

                        center_point = (center_x, center_y, center_z)

                        bone = bpy.data.armatures[ArmatureName].edit_bones[fix_instep_bone[1]]
                        original_length = (bone.tail - bone.head).length
                        direction = (bone.tail - bone.head).normalized()
                        bone.head = center_point
                        bone.tail = bone.head + direction * original_length

                    # 修正骨骼，Shin应当位于Knee的正下方距离0.01的位置
                    for fshb in fix_shin_bone:
                        if fshb in name_in:
                            bone = bpy.data.armatures[ArmatureName].edit_bones[fshb]
                            bone.head.z = bone.head.z - 0.01
                            bone.tail.z = bone.tail.z - 0.01

                    if 'Hip' in name_in:
                        hip_bone = bpy.data.armatures[ArmatureName].edit_bones['Hip']
                        center_point = (hip_bone.head.x, hip_bone.head.y, hip_bone.head.z)

                        # 修正骨骼，Spine_0和Spine_0_HJ_00应该与Hip在相同的位置，否则骑乘鹭鹰龙时屁股会顶起来
                        for fs0b in fix_spine0_bone:
                            if fs0b in name_in:
                                bone = bpy.data.armatures[ArmatureName].edit_bones[fs0b]
                                original_length = (bone.tail - bone.head).length
                                direction = (bone.tail - bone.head).normalized()
                                bone.head = center_point
                                bone.tail = bone.head + direction * original_length

                    for bone_name in name_in:
                        if bone_name not in name_ori and bone_name not in name_other:
                            bone_to_delete = bpy.data.armatures[ArmatureName].edit_bones[bone_name]
                            bpy.data.armatures[ArmatureName].edit_bones.remove(bone_to_delete)

                    bpy.ops.object.mode_set(mode='OBJECT')
                #若选择的字典不匹配当前选中的外部骨架，则报错
                else:
                    showErrorMessageBox(
                        "The selected dictionary may not match the currently selected external skeleton. Please select the correct dictionary.")

        self.report({'INFO'}, 'adsorption completed')
        return {'FINISHED'}


classes = [MHWildsOpenDictionaryFolder, MHWildssnapbone]
