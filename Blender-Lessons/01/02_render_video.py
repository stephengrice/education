import bpy

# Delete the cube that comes with it
if 'Cube' in bpy.data.objects:
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add(size=2)
cube = bpy.context.object
cube.location = (3, 0, 1)

scene = bpy.context.scene
scene.render.filepath = "output"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.frame_start = 1
scene.frame_end = 10
scene.render.image_settings.file_format = 'FFMPEG'
scene.render.ffmpeg.format = 'MPEG4'

bpy.ops.render.render(animation=True)
