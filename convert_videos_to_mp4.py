
import os
import subprocess
from tqdm import tqdm

SUPPORTED_FORMATS = ['.avi', '.mov', '.mkv', '.flv', '.webm', '.wmv', '.ts']

def convert_to_mp4(input_path, output_path):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '23',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-y',
        output_path
    ]
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception as e:
        print(f"❌ Lỗi khi chuyển file {input_path}: {e}")
        return False

def convert_all_videos_in_folder(folder_path):
    files = os.listdir(folder_path)
    video_files = [f for f in files if os.path.splitext(f)[1].lower() in SUPPORTED_FORMATS]

    if not video_files:
        print("❗ Không có file video nào cần chuyển đổi.")
        return

    print(f"\n🔄 Đang chuyển đổi {len(video_files)} video sang định dạng .mp4...\n")
    for file in tqdm(video_files):
        input_file = os.path.join(folder_path, file)
        output_file = os.path.splitext(input_file)[0] + '.mp4'
        if convert_to_mp4(input_file, output_file):
            print(f"✅ Đã chuyển: {file} → {os.path.basename(output_file)}")
        else:
            print(f"❌ Lỗi chuyển file: {file}")

if __name__ == "__main__":
    current_folder = os.path.dirname(os.path.abspath(__file__))
    print(f"📁 Đang kiểm tra thư mục: {current_folder}")
    convert_all_videos_in_folder(current_folder)
