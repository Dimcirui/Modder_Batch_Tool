from ..common.i18n.dictionary import preprocess_dictionary

dictionary = {

    "zh_CN": {
        # Preferences
        ("*", "View3D > Tool Shelf > Modder's Batch Tool"): "3D视图 > 侧栏 > Modder's Batch Tool面板",
        ("*", "Utility tools to do a lot of repetitive operations automatically"): "可以自动做大量重复工作的实用工具",

        # Show Panel Settings
        ("*", "Show Panel Settings"): "展示面板设置",
        ("*", "Show MHWilds panel"): "显示MHWilds面板",

        # Universal Function
        ("*", "Universal Function"): "通用功能",
        ("Operator", "separate by materials"): "按材质分离",
        ("*", "Separate the selected mesh objects according to their materials." \
              "\nThe separated meshes will be renamed according to the material name." \
              "\nAt the same time, the shape keys will be also separated"): "将选中的网格对象按照材质进行分离."
                                                                            "\n分离出来的网格会按照各自的材质名重新命名."
                                                                            "\n形态键也会同时被分离出来",
        ("Operator", "clean zero weight vg"): "清除空顶点组",
        ("*", "Clear all empty vertex groups of selected mesh objects"): "将选中的网格对象的所有空顶点组全部清除",

        # Universal translation
        ("*",
         "There are too many skeletons selected. Please select only two skeletons."): "选中的骨架过多，请只选中两个骨架。",
        ("*",
         "The selected dictionary may not match the currently selected external skeleton. Please select the correct dictionary."): "选择的字典可能不匹配当前选中的外部骨架，请选择正确的字典。",
        ("*", "batch rename vertax groups"): "批量更改顶点组名",
        ("*", "Batch absorb bones (only support t-pose)"): "批量吸附骨骼位置（仅支持t-pose）",
        ("*", "merge facial bones"): "合并面部表情骨骼",

        ("*", "Dictionary for adsorbing bones and renaming vertex groups"): "用于吸附骨骼和重命名顶点组的字典",
        ("Operator", "open dictionary folder"): "打开字典文件夹",
        ("*", "Open the dictionary folder in file explorer"): "在文件资源管理器中打开字典文件夹",
        ("Operator", "absorb bones"): "吸附骨骼",
        ("Operator", "rename vertex group"): "重命名顶点组",
        ("*", "Change the vertex group name of the external model to the corresponding game model vertex group name"): "将外部模型的顶点组名称修改为对应的游戏模型顶点组名称",
        ("*", "Batch normalize and limit weight to 8wt"): "批量规格化权重并设置总限值为8",
        ("*", "Batch normalize and limit weight to 6wt"): "批量规格化权重并设置总限值为6",
        ("*", "Batch normalize and limit weight to 4wt"): "批量规格化权重并设置总限值为4",
        ("Operator", "normalize and limit to 8wt"): "规格化权重并设置总限值为8",
        ("Operator", "normalize and limit to 6wt"): "规格化权重并设置总限值为6",
        ("*", "MHWilds currently supports a weighted total limit of up to 6wt, which may be extended to 12wt in the future"): "目前MHWilds支持最高6wt的权重总限值, 未来可能会扩展到12wt",
        ("Operator", "normalize and limit to 4wt"): "规格化权重并设置总限值为4",

        ("*", "Batch rename meshes to re format"): "批量重命名网格名为RE格式",
        ("Operator", "rename meshes"): "重命名网格名",
        ("*", "Change the mesh name to a format that conforms to the re engine, such as Group_0_Sub_0__xxx.\n"
              "It will rename each mesh according to the first material name"): "将网格名称修改为符合RE引擎的格式, 如Group_0_Sub_0__xxx."
                                                                                "\n它会按照每个网格的第一个材质来重新命名",

        ("*", "Batch split seam edge"): "批量分离缝合边",
        ("Operator", "split seam edge"): "分离缝合边",
        ("*", "Batch delete unnecessary UVs and unify UV names"): "批量删除多余的UV通道并统一UV名称",
        ("Operator", "unify UVs"): "统一UV通道",
        ("*", "Unify the UV channels of selected mesh objects."
              "\nThis operation will delete excess UV channels and keep only the first UV channel."): "将选中的网格对象的UV通道进行统一.\n该操作会删除多余的UV通道, 只保留第一个UV通道",
        ("Operator", "remove all shape keys"): "删除全部形态键",
        ("*", "Delete all shape keys of the selected mesh objects"): "将选中的网格对象的所有形态键全部删除",

        ("*", "convert to t-pose"): "转换为t-pose",
        ("Operator", "convert to t-pose"): "转换为t-pose",
        ("*", "Convert to t-pose"): "转换为t-pose（仅支持MHWilds骨架）",

        ("Operator", "merge meshes with same texture"): "合并具有相同贴图的网格",
        ("*", "Merge the selected mesh objects according to their corresponding textures." \
              "\nOnly mesh objects with base color texture in material node will be merged." \
              "\nThe merged mesh name will be changed to the format of texture name + resolution"): "将选中的网格对象按照各自对应的贴图进行合并."
                                                                                                    "\n只有材质节点中存在基础色贴图的网格对象才会被合并."
                                                                                                    "\n合并后的网格名称会修改为贴图名+分辨率的格式",
        ("*", "Set mod directory"): "设定mod文件路径",


        # Image Combiner
        ("*", "Image Combiner"): "贴图合并",
        ("*",
         "This modified combiner doesn't combine materials, so you can still seperate by materials"): "此魔改版插件并不合并材质，所以你仍可以按材质分离",
        ("*",
         "Please don't merge all textures into one texture with a very large resolution"): "请不要将所有贴图全部合并为一张分辨率非常大的贴图",
        ("*", "materials to combine:"): "要参与合并的材质",
        ("Operator", "Update Material List"): "更新材质列表",
        ("Operator", "Generate Material List"): "生成材质列表",
        ("*", "Properties:"): "特性",
        ("*", "Combined image size"): "合并贴图尺寸",
        ("*", "Power of 2"): "2的整数幂",
        ("Operator", "Save Combined Image"): "保存合并贴图",
        ("*", "Combine Images"): "合并贴图",

        # Credits
        ("*", "Credits"): "贡献者名单",
        ("*", "Korone"): "诸葛不太亮",
        ("Operator", "QQGroup"): "QQ群",
        ("Operator", "Caimogu"): "踩蘑菇mod论坛",

        # MHRise
        ("*", "import MHRise shadow mesh"): "导入MHRise通用骨架模型",

        # MHWorld
        ("*",
         "make sure you have installed <Easier MHW MOD3 Import_Export> plugin"): "请确保您已经安装《更方便的MOD3导入导出插件》",
        ("*", "import MHWorld basic armature"): "导入MHWorld基本骨架",
        ("Operator", "female armature"): "女性骨架",
        ("Operator", "male armature"): "男性骨架",
        ("*", "batch add empty mod3 meshes with properties"): "批量添加带自定义属性的mod3空模型网格",
        ("Operator", "add empty meshes"): "添加空模型网格",
        ("*", "batch emptied blocklabel"): "批量清空自定义属性的blocklabel",
        ("Operator", "emptied blocklabel"): "清空blocklabel",
        ("*",
         "Note: this function will automatically do all export pre-processing!"): "注意：该功能将自动为mod3模型网格做所有的导出前预处理!",
        ("Operator", "auto export process"): "自动导出预处理",

        # MHWilds
        ("*", "Current MHWilds Armature:"): "当前MHWilds骨架:",
        ("*", "Import MHWilds basic mesh"): "导入MHWilds基本模型",
        ("Operator", "female mesh"): "女性模型",
        ("*", "Import MHWilds full-body nude model of female."
              "\nThe imported model will be placed in a new collection."
              "\nYou can click the wrench icon on the right to adjust the import settings"): "导入MHWilds自带的女性全身裸体模型."
                                                                                             "\n导入的模型会被放置在一个新的集合中."
                                                                                             "\n你可以点击右侧的扳手按钮来调整导入设置项",
        ("Operator", "import settings"): "导入设置",
        ("*", "Settings for importing model"): "导入模型的设置项",
        ("*", "Whether the imported model armature is converted to t-pose."
              "\nNote that some bones will not be completely zeroed like thumbs, which takes into account the whole posture"): "是否要将导入的模型骨架转换为t-pose.\n注意某些骨骼不会完全归零, 比如大拇指, 这是考虑了整体姿态后的结果",
        ("*", "Whether to merge the facial bones.\nIf you need to make facial animations, don't check it"): "是否合并掉面部的表情骨骼.\n如果你需要制作表情动画, 则不要勾选它",

        ("*", "Convert MHWilds character armature to t-pose.\nConsidering some common bone names, this can also be applied to npcs"): "将MHWilds的人物骨架转换为t-pose.\n考虑到部分通用的骨骼名, 也可以应用在npc身上",

        ("*",
         "Please select both the external skeleton and MHWilds skeleton, and then press absorb bones"): "请同时选中外部骨架与MHWilds骨架, 然后点击吸附骨骼",
        ("*",
         "Absorb each bone in the game skeleton to the corresponding bone position in the external model skeleton."
         "\nSome bones will undergo additional position corrections after adsorption."
         "\nThe physical bones will also be merged into the parent"): "将游戏骨架中的各个骨骼吸附到外部模型骨架中的对应骨骼位置."
                                                                                        "\n部分骨骼会在吸附后进行额外的位置修正."
                                                                                        "\n吸附之后物理骨骼也会一同并入对应的父级",
        ("*", "The selected skeletons doesn't contain both the external skeleton and MHWilds skeleton."): "选中的骨架中未同时包含外部骨架与MHWilds骨架。",
        ("Operator", "male armature"): "男性骨架",

        ("*", "Generate or export fbxskel"): "生成或导出骨架对应的fbxskel",
        ("Operator", "generate fbxskel"): "生成fbxskel",
        ("*", "Please select the MHWilds skeleton generated by batch tool to generate fbxskel."): "请选择由批量插件生成的MHWilds骨架来生成fbxskel。",
        ("Operator", "export fbxskel"): "导出fbxskel",

        ("*",
         "Export fbxskel"): "导出fbxskel",

        ("*", "Please perform the operations in order"): "请按照顺序执行操作",

        ("*", "1.Download and install Bone System"): "1.下载并安装Bone System",
        ("Operator", "Download Bone System"): "下载Bone System",
        ("*", "By clicking, you will jump to the Bone System post page on caimogu"): "点击后会跳转到踩蘑菇的Bone System发布页面",

        ("*", "2.Set the mod file path"): "2.设定Mod文件路径",
        ("*", "Please select a path at the same level as the natives folder"): "请选择到与natives文件夹同级的路径",
        ("*", "3.Set file name"): "3.设定导出文件名",
        ("*", "The file name should be consistent with the GameObject name in the pfb file for the body part"): "文件名应与body部位的pfb文件中的GameObject名称保持一致",

        ("*", "4.Export fbxskel and json"): "4.导出fbxskel和json",
        ("Operator", "export fbxskel and json"): "导出fbxskel和json",
        ("*", "Export both fbxskel and json files."
              "\nPlease select the MHWilds character armature before exporting."
              "\nYou can click the wrench icon on the right to adjust the export settings"): "同时导出fbxskel和json文件."
                                                                                             "\n导出前请选中MHWilds人物骨架."
                                                                                             "\n你可以点击右侧的扳手按钮来调整导出设置项",

        ("Operator", "export settings"): "导出设置",
        ("*", "Settings for exporting json"): "导出json的设置项",
        ("*", "hide options:"): "隐藏选项:",
        ("*", "bind options:"): "绑定选项:",

        ("*", "hide face"): "隐藏头模",
        ("*", "hide hair"): "隐藏头发",
        ("*", "hide slinger"): "隐藏投射器",
        ("*", "bind facial"): "绑定表情",
        ("*", "bind part:"): "绑定部位:",


        ("*", "The mod file path is not set yet."): "Mod文件路径还未设定.",
        ("*", "The file name is not set yet."): "导出文件名还未设定.",


        # GranblueFantasyRelink
        # ("*", "convert gbfr model to tpose"): "将gbfr模型转换为tpose",
        # ("Operator", "convert to tpose"): "转换为tpose",


        # Props
        ("Operator", "Process Settings"): "功能设置",
        ("*", "convert quads to tris"): "面三角化",
        ("*", "split seam edge"): "分离缝合边",
        ("*", "unify UVs"): "统一UV通道",
        ("*", "separate by materials"): "按材质分离",
        ("*", "clean zero weight vg"): "清除空顶点组",
        ("*", "emptied blocklabel"): "清空blocklabel",


    }
}

dictionary = preprocess_dictionary(dictionary)

dictionary["zh_HANS"] = dictionary["zh_CN"]
