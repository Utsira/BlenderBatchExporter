import bpy, os

from bpy.app.handlers import persistent

@persistent
def load_handler(dummy):
    print("Load Handler:", bpy.data.filepath)

bpy.app.handlers.load_post.append(load_handler)

# for file in os.listdir()
# bpy.ops.wm.open_mainfile(filepath="file_path")