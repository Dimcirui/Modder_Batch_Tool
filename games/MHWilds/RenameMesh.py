import bpy


#由NSACloud编写
class RenameMeshToREFormat(bpy.types.Operator):
    bl_label = "rename meshes"
    bl_idname = "mbt.rename_mesh_to_reformat"
    bl_description = "Change the mesh name to a format that conforms to the re engine, such as Group_0_Sub_0__xxx.\nIt will rename each mesh according to the first material name"
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
        groupIndexDict = dict()
        selection = context.selected_objects
        for selectedObj in selection:

            if "Group_" in selectedObj.name:
                try:
                    groupID = int(selectedObj.name.split("Group_")[1].split("_")[0])
                except:
                    pass
            else:
                print("Could not parse group ID in {selectedObj.name}, setting to 0")
                groupID = 0
            if groupID not in groupIndexDict:
                groupIndexDict[groupID] = 0
            if len(selectedObj.data.materials) > 0:
                materialName = selectedObj.data.materials[0].name.split(".", 1)[0].strip()
            else:
                materialName = "NO_MATERIAL"
            selectedObj.name = f"Group_{str(groupID)}_Sub_{str(groupIndexDict[groupID])}__{materialName}"
            groupIndexDict[groupID] += 1

        self.report({"INFO"}, "renamed completed")
        return {'FINISHED'}


classes = [RenameMeshToREFormat]
