import bpy
import importlib

_submodule_names = {
    "MHRise": [
        "ImportMesh",
        "MHWtoMHR",
        "MMDtoMHR",
        "SnapBones_MMD",
        "UMAtoMHR",
        "XPStoMHR",
    ],
    "MHWorld": [
        "ImportMesh",
        "MHRtoMHW",
        "MMDtoMHW",
        "SnapBones_MMD",
        "UMAtoMHW",
        "VRCHATtoMHW",
        "addemptymesh",
        "SnapBones_Endfield",
        "EndfieldtoMHW",
        # "auto_process",
    ],
}

_modules = []
_classes = []


def register():
    global _modules, _classes
    _modules = []
    _classes = []
    
    print("--- Legacy Games: Registering ---")
    
    for folder, module_names in _submodule_names.items():
        for mod_name in module_names:
            full_name = f"{__package__}.{folder}.{mod_name}"
            try:
                mod = importlib.import_module(full_name)
                _modules.append(mod)
                
                if hasattr(mod, "register"):
                    mod.register()
                elif hasattr(mod, "classes"):
                    for cls in mod.classes:
                        bpy.utils.register_class(cls)
                        _classes.append(cls)
                        
            except Exception as e:
                print(f"  [!] Failed to load {full_name}: {e}")
    
    print(f"--- Legacy Games: Done ({len(_modules)} modules) ---")


def unregister():
    for cls in reversed(_classes):
        try:
            bpy.utils.unregister_class(cls)
        except:
            pass
    _classes.clear()
    
    for mod in reversed(_modules):
        if hasattr(mod, "unregister"):
            try:
                mod.unregister()
            except:
                pass
    _modules.clear()