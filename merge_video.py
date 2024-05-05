import os
import cv2

def list_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
def natural_sort_key(s):
    # Key function for natural sorting
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def merge_mp4_files(directory, output_file):
    mp4_files = [f for f in list_files_in_directory(directory) if f.endswith('.mp4')]
    mp4_files = sorted(mp4_files, key=natural_sort_key)
    print(mp4_files)
    if not mp4_files:
        print("No MP4 files found in the directory.")
        return

    video_list = [cv2.VideoCapture(os.path.join(directory, f)) for f in mp4_files]

    # Get video properties from the first video
    width = int(video_list[0].get(3))
    height = int(video_list[0].get(4))
    fps = int(video_list[0].get(5))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use appropriate fourcc codec based on your system

    output_video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    try:
        for video in video_list:
            while True:
                ret, frame = video.read()
                if not ret:
                    break
                output_video.write(frame)
        print(f'Merged {len(mp4_files)} MP4 files successfully into {output_file}')
    except Exception as e:
        print(f'Error merging MP4 files: {e}')
    finally:
        for video in video_list:
            video.release()
        output_video.release()

if __name__ == "__main__":
    folder_path = "./cam_chuyendung/"
    output_filename = "cam_chuyendung.mp4"

    merge_mp4_files(folder_path, output_filename)
