import moviepy
import os


def concatenate(video_clip_paths, output_path, output_width, output_height):
    """Extension (mp4, etc.) must be added to `output_path"""
    resized = []
    for clip in [moviepy.VideoFileClip(c) for c in video_clip_paths]:
        width, height = clip.size
        scale = max(width / output_width, height / output_height)
        resized.append(clip.resized(new_size=(width / scale, height / scale)))
    moviepy.concatenate_videoclips(resized, method="compose").write_videofile(output_path)


main_path = 'C://Users/gubar/OneDrive/Документы/Походы/Большие/2026 Ловозеро/Медиа/Видео/to_merge'
output = 'merged.mp4'
result_width = 1920
result_height = 1080

paths = []
for video in os.listdir(main_path):
    paths.append(os.path.join(main_path, video))

concatenate(paths, os.path.join(main_path, output), result_width, result_height)