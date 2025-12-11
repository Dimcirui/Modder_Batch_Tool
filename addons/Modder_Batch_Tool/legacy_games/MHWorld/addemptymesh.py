import bpy
import pathlib

_mesh_dir = pathlib.Path(__file__).parent / "mesh"
_empty_mesh_file = str(_mesh_dir / "emptymesh.mod3")


class MHW_OT_AddEmptyMesh(bpy.types.Operator):
    """Add empty meshes to selected armatures"""
    bl_idname = "mhw.add_empty_mesh"
    bl_label = "Add Empty Meshes"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == "ARMATURE" for obj in context.selected_objects)

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        armature_names = sorted(
            obj.name for obj in context.selected_objects if obj.type == "ARMATURE"
        )
        
        for arm_name in armature_names:
            # 导入空网格
            bpy.ops.custom_import.import_mhw_mod3(filepath=_empty_mesh_file)
            
            # 获取导入的对象
            mesh_names = sorted(
                obj.name for obj in context.selected_objects if obj.type == "MESH"
            )
            armature_import_names = sorted(
                obj.name for obj in context.selected_objects if obj.type == "ARMATURE"
            )
            
            # 设置父级
            context.view_layer.objects.active = bpy.data.objects[arm_name]
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
            
            # 处理空网格
            context.view_layer.objects.active = bpy.data.objects[mesh_names[0]]
            empty_obj = context.active_object
            empty_obj.data["blockLabel"] = ""
            context.view_layer.update()
            
            # 移除 modifier 并重新绑定
            bpy.ops.object.modifier_remove()
            modifier = empty_obj.modifiers[0]
            modifier.object = bpy.data.objects[arm_name]
            
            # 清空顶点
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')
            
            # 移除顶点组
            empty_obj.vertex_groups.remove(empty_obj.vertex_groups[0])
            
            # 删除导入的骨架
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[armature_import_names[0]].select_set(True)
            bpy.ops.object.delete(use_global=False)

        # 恢复选择
        context.view_layer.objects.active = bpy.data.objects[armature_names[0]]
        for name in armature_names:
            bpy.data.objects[name].select_set(True)
            
        self.report({'INFO'}, "Add completed")
        return {'FINISHED'}


classes = [
    MHW_OT_AddEmptyMesh,
]