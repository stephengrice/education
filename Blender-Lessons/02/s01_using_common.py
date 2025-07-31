import bpy

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common import clear_existing_objects, setup_camera, render_video


if __name__ == "__main__":
    clear_existing_objects()
    setup_camera()

    bpy.ops.mesh.primitive_cube_add(size=2)
    cube = bpy.context.object
    cube.location = (3, 0, 1)
    scene = bpy.context.scene
    # Animate cube
    for frame in range(scene.frame_start+1, scene.frame_end + 1):
        scene.frame_set(frame)
        cube.location.x -= 0.5
        cube.keyframe_insert(data_path="location", index=-1)  # Insert a keyframe for the location

    render_video()
