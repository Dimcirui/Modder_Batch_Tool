import bpy
from .merge_bone import get_objects, get_armature

def set_active(obj, skip_sel=False):
    if not skip_sel:
        select(obj)
        bpy.context.view_layer.objects.active = obj

def select(obj, sel=True):
    if obj is not None:
        hide(obj, False)
        obj.select_set(sel)

def hide(obj, val=True):
    if hasattr(obj, 'hide_set'):
        obj.hide_set(val)
    elif hasattr(obj, 'hide'):
        obj.hide = val

def has_shapekeys(mesh):
    if not hasattr(mesh.data, 'shape_keys'):
        return False
    return hasattr(mesh.data.shape_keys, 'key_blocks')

def save_shapekey_order(mesh_name):
    mesh = get_objects()[mesh_name]
    armature = get_armature()

    if not armature:
        return

    # Get current custom data
    custom_data = armature.get('CUSTOM')
    if not custom_data:
        # print('NEW DATA!')
        custom_data = {}

    # Create shapekey order
    shape_key_order = []
    if has_shapekeys(mesh):
        for index, shapekey in enumerate(mesh.data.shape_keys.key_blocks):
            shape_key_order.append(shapekey.name)

    # Check if there is already a shapekey order
    if custom_data.get('shape_key_order'):
        # print('SHAPEKEY ORDER ALREADY EXISTS!')
        # print(custom_data['shape_key_order'])
        old_len = len(custom_data.get('shape_key_order'))

        if type(shape_key_order) is str:
            old_len = len(shape_key_order.split(',,,'))

        if len(shape_key_order) <= old_len:
            # print('ABORT')
            return

    # Save order to custom data
    # print('SAVE NEW ORDER')
    custom_data['shape_key_order'] = shape_key_order

    # Save custom data in armature
    armature['CUSTOM'] = custom_data

    # print(armature.get('CUSTOM').get('shape_key_order'))

def clean_material_names(mesh):
    for j, mat in enumerate(mesh.material_slots):
        if mat.name.endswith('.001'):
            mesh.active_material_index = j
            mesh.active_material.name = mat.name[:-4]
        if mat.name.endswith(('. 001', ' .001')):
            mesh.active_material_index = j
            mesh.active_material.name = mat.name[:-5]


def prepare_separation(mesh):
    # set_default_stage()
    # unselect_all()

    # # Remove Rigidbodies and joints
    # if bpy.context.scene.remove_rigidbodies_joints:
    #     for obj in get_objects():
    #         if 'rigidbodies' in obj.name or 'joints' in obj.name:
    #             delete_hierarchy(obj)

    save_shapekey_order(mesh.name)
    set_active(mesh)

    for mod in mesh.modifiers:
        if mod.type == 'DECIMATE':
            mesh.modifiers.remove(mod)
        else:
            mod.show_expanded = False

    clean_material_names(mesh)

def clean_shapekeys(mesh):
    # Remove empty shapekeys
    if has_shapekeys(mesh):
        for kb in mesh.data.shape_keys.key_blocks:
            if can_remove_shapekey(kb):
                mesh.shape_key_remove(kb)
        if len(mesh.data.shape_keys.key_blocks) == 1:
            mesh.shape_key_remove(mesh.data.shape_keys.key_blocks[0])

def can_remove_shapekey(key_block):
    if 'mmd_' in key_block.name:
        return True
    if key_block.relative_key == key_block:
        return False  # Basis
    for v0, v1 in zip(key_block.relative_key.data, key_block.data):
        if v0.co != v1.co:
            return False
    return True

