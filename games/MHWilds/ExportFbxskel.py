import json
import bpy
import os
import copy
import logging
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy_extras.io_utils import ExportHelper

from .fbxskel.fbxskel_loader import load_fbxskel
from .fbxskel.fbxskel_writer import export_fbxskel, write_fbxskel
from ...operators.general_function import showErrorMessageBox

logger = logging.getLogger("mhwilds_fbxskel")

FemaleFbxskelMesh = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "ch03_000_9000.fbxskel.7")


def copy_bone_matrices(armature_a_name, armature_b_name):
    # 获取骨架对象
    armature_a = bpy.data.objects[armature_a_name]
    armature_b = bpy.data.objects[armature_b_name]

    # 切换到姿态模式
    bpy.context.view_layer.objects.active = armature_a
    bpy.ops.object.mode_set(mode='POSE')

    # 创建一个字典来存储骨骼名称和矩阵
    bone_matrices = {}

    # 遍历骨架 A 的所有姿态骨骼
    for bone in armature_a.pose.bones:
        # 获取骨骼的矩阵
        bone_matrix = copy.deepcopy(bone.matrix)
        bone_matrices[bone.name] = bone_matrix

    bpy.ops.object.mode_set(mode='OBJECT')

    # 切换到骨架 B
    bpy.context.view_layer.objects.active = armature_b
    bpy.ops.object.mode_set(mode='POSE')

    # 遍历骨架 B 的所有姿态骨骼
    for bone in armature_b.pose.bones:
        if bone.name in bone_matrices:
            # 如果骨骼名称匹配，则将矩阵赋值给该骨骼
            bone.matrix = bone_matrices[bone.name]
            bpy.context.view_layer.update()

    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.armature_apply(selected=False)
    bpy.ops.pose.select_all(action='DESELECT')

    # 切换回对象模式
    bpy.ops.object.mode_set(mode='OBJECT')


class Generatefbxskel(bpy.types.Operator):
    bl_idname = "mbt.generate_fbxskel"
    bl_label = "generate fbxskel"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.selected_objects is not None and len(bpy.context.selected_objects) == 1:
            for obj in bpy.context.selected_objects:
                return obj.type == "ARMATURE"

    def execute(self, context):
        fixed_location_list = [
            ['L_Hand', 'L_Wep_Sub'],
            ['L_Hand', 'L_Wep'],
            ['R_Hand', 'R_Wep_Sub'],
            ['R_Hand', 'R_Wep'],
            ['R_Forearm', 'R_Shield'],
            ['L_UpperArm', 'L_UpperArm_HJ_00'],
            ['R_UpperArm', 'R_UpperArm_HJ_00'],
            ['L_UpperArm', 'L_UpperArmTwist_HJ_00'],
            ['R_UpperArm', 'R_UpperArmTwist_HJ_00'],
            ['L_UpperArm', 'L_UpperArmDouble_HJ_00'],
            ['R_UpperArm', 'R_UpperArmDouble_HJ_00'],
            ['L_Forearm', 'L_ForearmDouble_HJ_00'],
            ['R_Forearm', 'R_ForearmDouble_HJ_00'],
            ['L_Forearm', 'L_Forearm_HJ_00'],
            ['R_Forearm', 'R_Forearm_HJ_00'],
            ['L_Knee', 'L_KneeDouble_HJ_00'],
            ['R_Knee', 'R_KneeDouble_HJ_00'],
        ]
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.context.active_object
        ArmatureName0 = obj.name

        bpy.ops.object.select_all(action='DESELECT')

        ArmatureObj = load_fbxskel(FemaleFbxskelMesh, collection=None, fix_rotation=True)
        ArmatureObj.select_set(True)
        ArmatureName1 = ArmatureObj.name
        ArmatureName = ArmatureObj.data.name
        bpy.ops.object.mode_set(mode='EDIT')
        for bone in ArmatureObj.data.edit_bones:
            bone.length = 0.1
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        copy_bone_matrices(ArmatureName0, ArmatureName1)

        ArmatureName = bpy.context.active_object.data.name
        obj = bpy.context.active_object.data.bones
        bpy.ops.object.mode_set(mode='EDIT')

        for n in fixed_location_list:
            bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[0]]
            bpy.context.object.data.use_mirror_x = False
            bpy.ops.armature.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=n[0], case_sensitive=False, extend=True)
            bpy.ops.object.select_pattern(pattern=n[1], case_sensitive=False, extend=True)
            bpy.context.area.type = 'VIEW_3D'
            bpy.ops.view3d.snap_selected_to_active()
            bpy.ops.armature.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}


class Exportfbxskel(bpy.types.Operator, ExportHelper):
    bl_idname = "mbt.export_fbxskel"
    bl_label = 'export fbxskel'
    bl_description = ""
    bl_options = {'PRESET', "REGISTER", "UNDO"}
    filename_ext = ".7"

    @classmethod
    def poll(cls, context):
        if bpy.context.selected_objects is not None and len(bpy.context.selected_objects) == 1:
            for obj in bpy.context.selected_objects:
                return obj.type == "ARMATURE"

    def invoke(self, context, event):
        fbxskel_armature = bpy.context.active_object
        if ".fbxskel" in fbxskel_armature.name:
            self.filepath = fbxskel_armature.name.split(".fbxskel")[0] + ".fbxskel.7"
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        beware = False
        try:
            bone_infos, beware_export = export_fbxskel(selected_objects)
            data, beware_write = write_fbxskel(bone_infos)
            with open(self.filepath, "wb") as file_out:
                file_out.write(data)
            beware = beware_export or beware_write
        except Exception as e:
            self.report({"ERROR"}, "Could not export fbxskel, reason = " + str(e))
            import traceback
            traceback.print_exc()
            return {"CANCELLED"}
        if beware:
            logger.warning("Export to " + self.filepath + " done, but warning were generated: make sure everything went correctly by checking the system console, found in Window->Toggle System Console")
            self.report({"WARNING"}, "Export done, but warning were generated: make sure everything went correctly by checking the system console, found in Window->Toggle System Console")
        else:
            logger.info("Export to " + self.filepath + " completed! ")
            self.report({"INFO"}, "export completed")
        return {"FINISHED"}


class Exportfbxskeljson(bpy.types.Operator):
    bl_idname = "mbt.export_fbxskel_json"
    bl_label = 'export fbxskel and json'
    bl_description = "Export both fbxskel and json files.\nPlease select the MHWilds character armature before exporting.\nYou can click the wrench icon on the right to adjust the export settings"
    bl_options = {'PRESET'}

    @classmethod
    def poll(cls, context):
        if bpy.context.selected_objects is not None and len(bpy.context.selected_objects) == 1:
            for obj in bpy.context.selected_objects:
                return obj.type == "ARMATURE"

    def execute(self, context):
        ori_armature = bpy.context.active_object

        bpy.ops.mbt.generate_fbxskel()

        armature = bpy.context.active_object

        scene = context.scene
        mbt_toolpanel = context.scene.mbt_toolpanel

        if mbt_toolpanel.MHWildsModDirectory != "":
            fbxskel_path = os.path.join(mbt_toolpanel.MHWildsModDirectory, 'natives\stm\BoneSystem')
            json_path = os.path.join(mbt_toolpanel.MHWildsModDirectory, 'reframework\data\BoneSystem')

            if not os.path.exists(fbxskel_path):
                os.makedirs(fbxskel_path)
                print(f"File path {fbxskel_path} has been created.")
            else:
                print(f"File path {fbxskel_path} already exists.")

            if mbt_toolpanel.MHWildsFbxskelName != "":

                file_path = os.path.join(fbxskel_path, mbt_toolpanel.MHWildsFbxskelName + ".fbxskel.7")

                selected_objects = bpy.context.selected_objects
                beware = False
                try:
                    bone_infos, beware_export = export_fbxskel(selected_objects)
                    data, beware_write = write_fbxskel(bone_infos)
                    with open(file_path, "wb") as file_out:
                        file_out.write(data)
                    beware = beware_export or beware_write
                except Exception as e:
                    self.report({"ERROR"}, "Could not export fbxskel, reason = " + str(e))
                    import traceback
                    traceback.print_exc()
                    return {"CANCELLED"}
                if beware:
                    logger.warning(
                        "Export to " + file_path + " done, but warning were generated: make sure everything went correctly by checking the system console, found in Window->Toggle System Console")
                    self.report({"WARNING"},
                                "Export done, but warning were generated: make sure everything went correctly by checking the system console, found in Window->Toggle System Console")
                else:
                    logger.info("Export to " + file_path + " completed!")

                if not os.path.exists(json_path):
                    os.makedirs(json_path)
                    print(f"File path {json_path} has been created.")
                else:
                    print(f"File path {json_path} already exists.")

                file_path = os.path.join(json_path, mbt_toolpanel.MHWildsFbxskelName + ".json")

                settings_infos = {
                    "HideFace": mbt_toolpanel.mhwilds_json_hide_face,
                    "HideHair": mbt_toolpanel.mhwilds_json_hide_hair,
                    "HideSlinger": mbt_toolpanel.mhwilds_json_hide_slinger,
                    "BindFace": mbt_toolpanel.mhwilds_json_bind_facial,
                    "BindPart": int(mbt_toolpanel.mhwilds_json_bind_part),
                    "FbxPath": mbt_toolpanel.MHWildsFbxskelName
                }

                with open(file_path, "w") as json_file:
                    json.dump(settings_infos, json_file, indent=4)

                logger.info("Export to " + file_path + " completed!")

                bpy.data.objects.remove(armature)
                bpy.context.view_layer.objects.active = ori_armature
                ori_armature.select_set(True)
                self.report({"INFO"}, "export completed")
            else:
                showErrorMessageBox("The file name is not set yet.")

        else:
            showErrorMessageBox("The mod file path is not set yet.")

        return {"FINISHED"}


class Exportfbxskeljson_Settings(bpy.types.Operator):
    bl_idname = "mbt.export_fbxskel_json_settings"
    bl_label = "export settings"
    bl_description = "Settings for exporting json"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def check(self, context):
        # Important for changing options
        return True

    def draw(self, context):
        mbt_toolpanel = context.scene.mbt_toolpanel
        layout = self.layout

        row = layout.row()
        col_left = row.column()
        col_right = row.column()

        col_left.label(text="hide options:")
        col_left.prop(mbt_toolpanel, "mhwilds_json_hide_face")
        col_left.prop(mbt_toolpanel, "mhwilds_json_hide_hair")
        col_left.prop(mbt_toolpanel, "mhwilds_json_hide_slinger")

        col_right.label(text="bind options:")
        col_right.prop(mbt_toolpanel, "mhwilds_json_bind_facial")
        if mbt_toolpanel.mhwilds_json_bind_facial == True:
            col_right.label(text="bind part:")
            col_right.prop(mbt_toolpanel, "mhwilds_json_bind_part", text="")


classes = [Generatefbxskel, Exportfbxskel, Exportfbxskeljson, Exportfbxskeljson_Settings]
