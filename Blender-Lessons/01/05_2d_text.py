import bpy

# Delete the cube that comes with it
if 'Cube' in bpy.data.objects:
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.object.delete()

# Create a new camera object if one doesn't exist
if not bpy.data.objects.get('Camera'):
    bpy.ops.object.camera_add(location=(0, 0, 10))
    camera = bpy.context.object
else:
    # Use existing camera
    camera = bpy.data.objects['Camera']

# Set camera properties for a 2D-style setup
camera.data.type = 'ORTHO'
camera.data.ortho_scale = 5
camera.rotation_euler = (0, 0, 0)
camera.location = (0, 0, 10)

# Set the active camera for the scene
bpy.context.scene.camera = camera

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

# Animate cube
for frame in range(scene.frame_start+1, scene.frame_end + 1):
    scene.frame_set(frame)
    cube.location.x -= 0.5
    cube.keyframe_insert(data_path="location", index=-1)  # Insert a keyframe for the location

bpy.ops.object.text_add()
text_object = bpy.context.object
text_object.data.body = "PageKey"
text_object.location = (-1.5, 0, 0)
text_object.rotation_euler = (0, 0, 0)

bpy.ops.render.render(animation=True)
