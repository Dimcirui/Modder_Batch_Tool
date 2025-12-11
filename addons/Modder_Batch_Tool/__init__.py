import bpy
import os
from .legacy_games.MHWorld import auto_process
from . import legacy_games
from bpy.utils import previews
from bpy.props import StringProperty, BoolProperty, EnumProperty, CollectionProperty,PointerProperty

from .properties.mbt_properties import MBTToolPanelPG
from ... import addon_updater_ops, addon_updater
from .config import __addon_name__
from .i18n.dictionary import dictionary
from ...common.class_loader import auto_load
from ...common.class_loader.auto_load import add_properties, remove_properties
from ...common.i18n.dictionary import common_dictionary
from ...common.i18n.i18n import load_dictionary
from .panels.AddonPanels import ICONS_PATH, preview_collections

# Add-on info
bl_info = {
    "name": "Modder Batch Tool",
    "author": "诸葛不太亮, Dimcirui",
    "blender": (4, 2, 0),
    "version": (1, 4, 0),
    "description": "Utility tools to do a lot of repetitive operations automatically.",
    "warning": "",
    "wiki_url": "https://github.com/Dimcirui/Modder_Batch_Tool",
    "tracker_url": "https://github.com/Dimcirui/Modder_Batch_Tool/issues",
    "support": "COMMUNITY",
    # "location": "View3D > Tool Shelf > Modder's Batch Tool",
    "category": "3D View"
}

_addon_properties = {}


# You may declare properties like following, framework will automatically add and remove them.
# Do not define your own property group class in the __init__.py file. Define it in a separate file and import it here.
# 注意不要在__init__.py文件中自定义PropertyGroup类。请在单独的文件中定义它们并在此处导入。
# _addon_properties = {
#     bpy.types.Scene: {
#         "property_name": bpy.props.StringProperty(name="property_name"),
#     },
# }

updatemodules = [
                 addon_updater,
                 addon_updater_ops,
]

updateclasses = [
                 addon_updater_ops.AddonUpdaterUpdateTarget,
                 addon_updater_ops.AddonUpdaterCheckNow,
                 addon_updater_ops.AddonUpdaterEndBackground,
                 addon_updater_ops.AddonUpdaterInstallManually,
                 addon_updater_ops.AddonUpdaterUpdateNow,
                 addon_updater_ops.AddonUpdaterIgnore,
                 addon_updater_ops.AddonUpdaterRestoreBackup,
                 addon_updater_ops.AddonUpdaterUpdatedSuccessful,
                 addon_updater_ops.AddonUpdaterInstallPopup,
]



def register():
    # Register classes
    global preview_collections

    auto_load.init()
    for i in range(len(updatemodules)):
        if updatemodules[i] in auto_load.modules:
            auto_load.modules.remove(updatemodules[i])
    for i in range(len(updateclasses)):
        if updateclasses[i] in auto_load.ordered_classes:
            auto_load.ordered_classes.remove(updateclasses[i])
    addon_updater_ops.register(bl_info)

    auto_load.register()
    
    # 注册 legacy_games
    try:
        auto_process.register()
        legacy_games.register()  # 新增这行
    except Exception as e:
        print(f"Warning: legacy_games register failed: {e}")
        import traceback
        traceback.print_exc()

    icon_names = ["github", "korone", "bilibili", "qq", "caimogu"]
    pcoll = bpy.utils.previews.new()
    for icon_name in icon_names:
        pcoll.load(icon_name, os.path.join(ICONS_PATH, icon_name + ".png"), 'IMAGE')
    if preview_collections.get('icons'):
        bpy.utils.previews.remove(preview_collections['icons'])
    preview_collections['icons'] = pcoll

    add_properties(_addon_properties)

    # Internationalization
    load_dictionary(dictionary)
    bpy.app.translations.register(__addon_name__, common_dictionary)
    bpy.types.Scene.mbt_toolpanel = PointerProperty(type=MBTToolPanelPG)
    print("{} addon is installed.".format(__addon_name__))


def unregister():
    addon_updater_ops.unregister()
    global preview_collections
    # Internationalization
    bpy.app.translations.unregister(__addon_name__)
    # unRegister classes
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    
    # 手动注销 legacy_games
    try:
        legacy_games.unregister()
        auto_process.unregister()
    except:
        pass

    auto_load.unregister()
    remove_properties(_addon_properties)
    print("{} addon is uninstalled.".format(__addon_name__))
