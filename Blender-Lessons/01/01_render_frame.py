# Render a frame - simplest possible script
import bpy

# Delete the cube that comes with it
if 'Cube' in bpy.data.objects:
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add(size=2)
cube = bpy.context.object
cube.location = (3, 0, 1)

scene = bpy.context.scene
scene.render.filepath = "output.png"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.frame_set(1)

bpy.ops.render.render(write_still=True)
