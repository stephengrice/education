import bpy

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common import clear_existing_objects, setup_camera, render_video

def add_video_as_plane(filename):
    # Check if the add-on is enabled
    addon_name = 'io_import_images_as_planes'
    addon_enabled = addon_name in bpy.context.preferences.addons

    # Enable the add-on if it's not already enabled
    if not addon_enabled:
        bpy.ops.preferences.addon_enable(module=addon_name)

    # Use the add-on to import the image or video as a plane
    bpy.ops.import_image.to_plane(files=[{"name": filename}], shader='EMISSION')

    # Get the active object (the imported plane)
    plane = bpy.context.object
    plane.scale = (2.85, 2.85, 2.85)
    return plane

if __name__ == "__main__":
    clear_existing_objects()
    setup_camera()

    add_video_as_plane('../sample.mp4')

    render_video(frame_end=30)
