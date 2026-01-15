import bpy
import os

class MHW_OT_AddEmptyMesh(bpy.types.Operator):
    """Import an empty mod3 mesh for merging purposes"""
    bl_idname = "mhw.add_empty_mesh"
    bl_label = "Add Empty Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 1. 获取自带的 emptymesh.mod3 文件路径
        # 假设该文件位于当前脚本同级目录下的 mesh 文件夹内
        addon_dir = os.path.dirname(os.path.abspath(__file__))
        mesh_path = os.path.join(addon_dir, "mesh", "emptymesh.mod3")
        
        if not os.path.exists(mesh_path):
            self.report({'ERROR'}, f"Empty mesh file not found at: {mesh_path}")
            return {'CANCELLED'}

        # 2. 记录当前场景的所有物体 (快照)
        # 这样我们就不用依赖 unreliable 的 selected_objects 了
        old_objects = set(context.scene.objects)

        # 3. 执行导入
        # MHW Mod3 Importer 的标准操作符通常是 import_mesh.mhw_mod3
        try:
            bpy.ops.import_mesh.mhw_mod3(filepath=mesh_path)
        except AttributeError:
            # 如果用户没装 Mod3 Importer 或者是其他版本的插件
            self.report({'ERROR'}, "Could not find 'import_mesh.mhw_mod3'. Please ensure the MHW Mod3 Importer addon is installed.")
            return {'CANCELLED'}
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {str(e)}")
            return {'CANCELLED'}

        # 4. 找出新增加的物体
        current_objects = set(context.scene.objects)
        new_objects = current_objects - old_objects
        
        if not new_objects:
            self.report({'WARNING'}, "Import operator ran but no new objects appeared in the scene.")
            return {'CANCELLED'}

        # 5. 分类新物体 (找出网格和骨架)
        target_mesh = None
        target_armature = None
        
        for obj in new_objects:
            if obj.type == 'MESH':
                target_mesh = obj
            elif obj.type == 'ARMATURE':
                target_armature = obj
        
        # 6. 设置活动物体
        if target_mesh:
            # 清除所有选择
            bpy.ops.object.select_all(action='DESELECT')
            
            # 选中并激活新网格
            target_mesh.select_set(True)
            context.view_layer.objects.active = target_mesh
            
            # 如果导入还附带了骨架，也顺便选中它(方便用户操作)，但保持网格为活动物体
            if target_armature:
                target_armature.select_set(True)
                
            self.report({'INFO'}, f"Added empty mesh: {target_mesh.name}")
        else:
            self.report({'WARNING'}, "Imported successfully but could not identify the mesh object.")

        return {'FINISHED'}

classes = [
    MHW_OT_AddEmptyMesh,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)