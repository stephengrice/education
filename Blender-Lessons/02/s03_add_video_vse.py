import bpy

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common import clear_existing_objects, setup_camera, render_video

def add_video_vse(filename, channel=1):
    scene = bpy.context.scene
    sequence_editor = scene.sequence_editor

    # Create a new sequence if one doesn't exist
    if sequence_editor is None:
        sequence_editor = scene.sequence_editor_create()

    # Add the video file to the sequence editor as a video strip
    video_strip = sequence_editor.sequences.new_movie(
        frame_start=1,
        name="VideoStrip",
        filepath=filename,
        channel=channel
    )

    return video_strip

def add_audio_vse(filename, channel=1):
    scene = bpy.context.scene
    sequence_editor = scene.sequence_editor

    # Create a new sequence if one doesn't exist
    if sequence_editor is None:
        sequence_editor = scene.sequence_editor_create()

    # Add the audio file to the sequence editor as an audio strip
    audio_strip = sequence_editor.sequences.new_sound(
        frame_start=1,
        name="AudioStrip",
        filepath=filename,
        channel=channel
    )
    return audio_strip

if __name__ == "__main__":
    clear_existing_objects()
    setup_camera()

    add_video_vse('../sample.mp4')
    add_audio_vse('../sample.mp4', channel=2)

    render_video(frame_end=30, use_vse=True)
