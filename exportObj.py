import bpy, sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.ops.export_scene.obj(filepath = argv[0], use_selection = True, use_triangles = True, global_scale = float(argv[1]))
