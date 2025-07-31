import bpy

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common import clear_existing_objects, setup_camera, render_video
from s03_add_video_vse import add_audio_vse, add_video_vse


if __name__ == "__main__":
    clear_existing_objects()
    setup_camera()

    add_video_vse("../sample.mp4")
    add_audio_vse("../sample.mp4", channel=2)

    frame_start = 1
    text_strip = bpy.context.scene.sequence_editor.sequences.new_effect(
        name="MyText", type="TEXT", channel=1, frame_start=frame_start,
        frame_end=31,
    )
    text_strip.text = "This video rocks dude"
    text_strip.font_size = 96
    text_strip.color = (0.0, 0.0, 0.0, 1.0)
    text_strip.location.x = 0.5
    text_strip.location.y = 0.5

    render_video(frame_end=30, use_vse=True)
