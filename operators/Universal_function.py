import bpy
import bmesh

from .separate_mesh import prepare_separation, clean_shapekeys


def _Clean_Vertex_By_Weight():
    def check_each_vertex_group_max_weight(obj):
        gid_to_maxw = {}
        # 让统计字典内的顶点组的初始值为0
        for g in obj.vertex_groups:
            gid_to_maxw[g.index] = 0
        # 循环网格体的每一个顶点，统计每个顶点组的最大权重
        for v in obj.data.vertices:
            for g in v.groups:
                gid = g.group
                w = obj.vertex_groups[gid].weight(v.index)
                if (gid_to_maxw.get(gid) is None or w > gid_to_maxw[gid]):
                    gid_to_maxw[gid] = w
        return gid_to_maxw

    # 获得对象
    for obj in bpy.context.selected_objects:
        # 获得对象的 每个顶点组到最大权重的字典
        gid_to_maxw = check_each_vertex_group_max_weight(obj)
        # 让字典的值按大到小排序，这是为了从大到小逐个删除时，删除序号大的不会影响序号小。
        wait_to_del_gids = []
        for gid, maxw in gid_to_maxw.items():
            if maxw <= 0:
                wait_to_del_gids.append(gid)
        # 让顶点组编号从大到小排序，这先删除编号大的不会对编号小的造成影响
        wait_to_del_gids = sorted(wait_to_del_gids)[::-1]
        # print(f'Delete vertex group index list {wait_to_del_gids}')
        # 逐个删除空顶点组
        for gid in wait_to_del_gids:
            obj.vertex_groups.remove(obj.vertex_groups[gid])
    # print('Success')

class CleanZeroVG(bpy.types.Operator):
    bl_idname = "mbt.clean_zero_vg"
    bl_label = "clean zero weight vg"
    bl_description = "Clear all empty vertex groups of selected mesh objects"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        _Clean_Vertex_By_Weight()
        self.report({'INFO'}, 'clean completed')
        return {'FINISHED'}



class SeparateByMaterials(bpy.types.Operator):
    bl_idname = "mbt.separate_by_materials"
    bl_label = "separate by materials"
    bl_description = "Separate the selected mesh objects according to their materials." \
                     "\nThe separated meshes will be renamed according to the material name." \
                     "\nAt the same time, the shape keys will be also separated"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        active_obj = bpy.context.active_object

        for obj in bpy.context.selected_objects:
            prepare_separation(obj)

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.separate(type='MATERIAL')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mbt.clean_zero_vg()

        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                mat_name = obj.active_material.name if obj.active_material else obj.name
                obj.name = mat_name
                clean_shapekeys(obj)
                # print(mat_name)

        # 再次重命名以去除名称后缀
        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                mat_name = obj.active_material.name if obj.active_material else obj.name
                obj.name = mat_name

        bpy.context.view_layer.objects.active = active_obj

        self.report({'INFO'}, 'separate completed')
        return {'FINISHED'}


class RemoveShapeKeys(bpy.types.Operator):
    bl_idname = "mbt.remove_shapekeys"
    bl_label = "remove all shape keys"
    bl_description = "Delete all shape keys of the selected mesh objects"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        meshes_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])
        for n in meshes_sel_name:
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            obj = bpy.context.active_object
            if obj.data.shape_keys:
                bpy.ops.object.shape_key_remove(all=True)
        bpy.context.view_layer.objects.active = bpy.data.objects[meshes_sel_name[0]]
        self.report({'INFO'}, 'remove completed')
        return {'FINISHED'}


class UnifyUVs(bpy.types.Operator):
    bl_idname = "mbt.unify_uvs"
    bl_label = "unify UVs"
    bl_description = "Unify the UV channels of selected mesh objects.\nThis operation will delete excess UV channels and keep only the first UV channel."
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        meshes_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])

        for n in meshes_sel_name:
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            activemesh = bpy.context.active_object

            while len(activemesh.data.uv_layers) > 1:
                activemesh.data.uv_layers.remove(activemesh.data.uv_layers[-1])
            activemesh.data.uv_layers[0].name = "UVMap"

        bpy.context.view_layer.objects.active = bpy.data.objects[meshes_sel_name[0]]
        self.report({'INFO'}, 'unify completed')
        return {'FINISHED'}


class SplitSeamEdge(bpy.types.Operator):
    bl_idname = 'mbt.split_seam_edge'
    bl_label = "split seam edge"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        meshes_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])

        for n in meshes_sel_name:
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            obj = bpy.context.active_object

            # 分离缝合边
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.seams_from_islands(mark_seams=True)
            bpy.context.tool_settings.mesh_select_mode = (False, True, False)
            bpy.ops.mesh.select_all(action='DESELECT')

            bpy.ops.object.mode_set(mode='OBJECT')
            for edge in obj.data.edges:
                if edge.use_seam:
                    edge.select = True
                    # bpy.ops.object.mode_set(mode='EDIT')
                    # bpy.ops.mesh.edge_split(type='EDGE')
                    # bpy.ops.object.mode_set(mode='OBJECT')

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.edge_split(type='EDGE')

            # bpy.ops.mesh.select_all(action='SELECT')
            # bpy.ops.mesh.delete_loose()
            # bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            # 分离重叠点
            uv_layers = obj.data.uv_layers.active
            uv_coords = {}
            for poly in obj.data.polygons:
                loop_start = poly.loop_start
                loop_end = loop_start + poly.loop_total
                i = 0
                for loop_index in range(loop_start, loop_end):
                    uv_co = uv_layers.data[loop_index].uv
                    if poly.vertices[i] in uv_coords and uv_coords[poly.vertices[i]] != uv_co:
                        obj.data.vertices[poly.vertices[i]].select = True
                    else:
                        uv_coords[poly.vertices[i]] = uv_co
                    i += 1

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.edge_split(type='VERT')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            # 分离锐边
            bpy.ops.object.mode_set(mode='EDIT')
            bm = bmesh.from_edit_mesh(obj.data)
            for e in bm.edges:
                if not e.smooth:
                    e.select = True
            bpy.ops.mesh.edge_split(type='EDGE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bmesh.update_edit_mesh(obj.data)

            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete_loose()
            bpy.ops.mesh.select_all(action='DESELECT')

            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.context.view_layer.objects.active = bpy.data.objects[meshes_sel_name[0]]
        self.report({'INFO'}, 'split completed')
        return {'FINISHED'}

def Normalize_Limit_Weight(weight_limit):
    meshes_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])
    # print(meshes_sel_name)

    bpy.ops.mbt.clean_zero_vg()
    for n in meshes_sel_name:
        bpy.context.view_layer.objects.active = bpy.data.objects[n]
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        bpy.ops.object.vertex_group_lock(action='UNLOCK', mask='ALL')
        bpy.ops.object.vertex_group_normalize_all(lock_active=False)
        bpy.ops.object.vertex_group_clean(group_select_mode='ALL', limit=0.001)
        bpy.ops.object.vertex_group_limit_total(limit=weight_limit)
        bpy.ops.object.mode_set(mode='OBJECT')

    bpy.context.view_layer.objects.active = bpy.data.objects[meshes_sel_name[0]]



class NormalizeLimit8wtVG(bpy.types.Operator):
    bl_idname = "mbt.normalize_limit_8wt_vg"
    bl_label = "normalize and limit to 8wt"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        Normalize_Limit_Weight(weight_limit=8)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}

class NormalizeLimit6wtVG(bpy.types.Operator):
    bl_idname = "mbt.normalize_limit_6wt_vg"
    bl_label = "normalize and limit to 6wt"
    bl_description = "MHWilds currently supports a weighted total limit of up to 6wt, which may be extended to 12wt in the future"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        Normalize_Limit_Weight(weight_limit=6)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}

class NormalizeLimit4wtVG(bpy.types.Operator):
    bl_idname = "mbt.normalize_limit_4wt_vg"
    bl_label = "normalize and limit to 4wt"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):
        Normalize_Limit_Weight(weight_limit=4)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}


class MergeMeshesWithSameTexture(bpy.types.Operator):
    bl_idname = "mbt.merge_meshes_with_same_texture"
    bl_label = "merge meshes with same texture"
    bl_description = "Merge the selected mesh objects according to their corresponding textures." \
                     "\nOnly mesh objects with base color texture in material node will be merged." \
                     "\nThe merged mesh name will be changed to the format of texture name + resolution"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # 检查是否有选中的对象
        if context.selected_objects:
            # 遍历所有选中的对象
            for obj in context.selected_objects:
                # 如果发现任何一个对象不是网格类型，返回 False
                if obj.type != "MESH":
                    return False
            # 如果所有选中的对象都是网格类型，返回 True
            return True
        # 如果没有选中的对象，返回 False
        return False

    def execute(self, context):

        bpy.ops.mbt.separate_by_materials()

        # 用于存储图像纹理信息的字典
        texture_info = {}

        # 遍历所有选中的对象
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                # 获取对象的材质
                for mat_slot in obj.material_slots:
                    mat = mat_slot.material
                    if mat and mat.use_nodes:
                        # 检查材质节点
                        found_shader = False
                        for node in mat.node_tree.nodes:
                            if node.name in ["原理化 BSDF", "原理化BSDF", "Principled BSDF", "mmd_shader"]:
                                found_shader = True
                                if node.name == "mmd_shader":
                                    # 检查基础色是否连接了图像纹理
                                    base_color_input = node.inputs.get("Base Tex")
                                    if base_color_input.is_linked:
                                        # 获取连接的节点
                                        image_texture_node = base_color_input.links[0].from_node
                                        if image_texture_node.type == 'TEX_IMAGE':
                                            # 获取图像文件名和分辨率
                                            image = image_texture_node.image
                                            if image:
                                                texture_name = image.name
                                                texture_size = (image.size[0], image.size[1])
                                                # 保存到字典
                                                if texture_name not in texture_info:
                                                    texture_info[texture_name] = {
                                                        'resolution': texture_size,
                                                        'objects': []
                                                    }
                                                texture_info[texture_name]['objects'].append(obj.name)
                                    else:
                                        print(
                                            f"对象 '{obj.name}' 的 '{mat.name}' 材质中的 '{node.name}' 着色器没有连接图像纹理。")
                                else:
                                    # 检查基础色是否连接了图像纹理
                                    base_color_input = node.inputs.get("Base Color")
                                    if base_color_input.is_linked:
                                        # 获取连接的节点
                                        image_texture_node = base_color_input.links[0].from_node
                                        if image_texture_node.type == 'TEX_IMAGE':
                                            # 获取图像文件名和分辨率
                                            image = image_texture_node.image
                                            if image:
                                                texture_name = image.name
                                                texture_size = (image.size[0], image.size[1])
                                                # 保存到字典
                                                if texture_name not in texture_info:
                                                    texture_info[texture_name] = {
                                                        'resolution': texture_size,
                                                        'objects': []
                                                    }
                                                texture_info[texture_name]['objects'].append(obj.name)
                                    else:
                                        print(
                                            f"对象 '{obj.name}' 的 '{mat.name}' 材质中的 '{node.name}' 着色器没有连接图像纹理。")
                        if not found_shader:
                            print(f"对象 '{obj.name}' 没有原理化着色器或 MMD Shader 着色器。")

        merged_objects = []
        # 合并具有相同图像纹理的网格对象
        for texture_name, info in texture_info.items():
            if info['objects']:
                # 选择要合并的对象
                objs_to_merge = [bpy.data.objects[obj_name] for obj_name in info['objects']]

                # 取消选择所有对象
                bpy.ops.object.select_all(action='DESELECT')

                # 选择要合并的对象
                for obj in objs_to_merge:
                    obj.select_set(True)

                # 将第一个对象设为活动对象
                bpy.context.view_layer.objects.active = objs_to_merge[0]

                if len(objs_to_merge) > 1:
                    # 合并对象
                    bpy.ops.object.join()

                # 修改合并后的网格名称
                merged_object = bpy.context.active_object
                merged_objects.append(merged_object)
                merged_object.name = f"{texture_name}_{info['resolution'][0]}x{info['resolution'][1]}"
                merged_object.name = f"{texture_name}_{info['resolution'][0]}x{info['resolution'][1]}"

                # 取消选择所有对象
                bpy.ops.object.select_all(action='DESELECT')

        for obj in merged_objects:
            obj.select_set(True)

        print("检查和合并完成。")

        self.report({'INFO'}, 'merge completed')
        return {'FINISHED'}