import bpy

def clear_existing_objects():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_camera():
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

def render_video(frame_start=1, frame_end=10, use_vse=False):
    scene = bpy.context.scene
    scene.render.filepath = "output"
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.frame_start = frame_start
    scene.frame_end = frame_end
    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.ffmpeg.format = 'MPEG4'
    scene.render.ffmpeg.audio_codec = 'MP3'

    if use_vse:
        # Set rendering to use the VSE sequence
        scene.sequence_editor_create()  # Ensure sequence editor exists
        scene.render.use_sequencer = True

    bpy.ops.render.render(animation=True)
