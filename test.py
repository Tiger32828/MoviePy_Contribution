from moviepy.moviepy.editor import VideoFileClip
import os
import cv2
tmp_path = "video.mp4"


if not os.path.exists(tmp_path):
    print("No such path")
video_reader = VideoFileClip(filename = tmp_path)

# video_reader.resize()
output_size = (960, 540)

for idx, frame in enumerate(video_reader.iter_frames(output_size=output_size)):
    print(frame.shape)
    cv2.imwrite(str(idx) + ".png", frame)

    if idx == 10:
        break
