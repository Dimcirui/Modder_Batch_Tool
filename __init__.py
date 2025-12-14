from .addons.Modder_Batch_Tool import register as addon_register, unregister as addon_unregister

bl_info = {
    "name": 'Modder Batch Tool',
    "author": '诸葛不太亮, Dimcirui',
    "blender": (4, 2, 0),
    "version": (1, 4, 1),
    "description": 'Utility tools to do a lot of repetitive operations automatically.',
    "warning": '',
    "wiki_url": 'https://github.com/Dimcirui/Modder_Batch_Tool',
    "tracker_url": 'https://github.com/Dimcirui/Modder_Batch_Tool/issues',
    "support": 'COMMUNITY',
    "category": '3D View'
}

def register():
    addon_register()

def unregister():
    addon_unregister()

    
