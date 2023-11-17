import requests
import os
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
from moviepy.editor import VideoFileClip
import re

def create_folder(folder_name):
    """创建文件夹"""
    os.makedirs(folder_name, exist_ok=True)

def download_file(url, save_path, headers=None):
    """下载文件，并显示下载进度"""
    with requests.get(url, headers=headers, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        tqdm_kwargs = dict(total=total_size, unit='iB', unit_scale=True)
        with open(save_path, 'wb') as file, tqdm(
                desc=save_path,
                **tqdm_kwargs
        ) as bar:
            for data in response.iter_content(block_size):
                bar.update(len(data))
                file.write(data)

def download_video(url, title, headers):
    """下载视频并返回视频文件路径"""
    ready_video_url = extract_ready_video_url(url, headers)
    if ready_video_url:
        video_file_path = f'./视频/{title}.mp4'
        download_file(ready_video_url, video_file_path, headers)
        return video_file_path

def extract_ready_video_url(url, headers):
    """从网页中提取readyVideoUrl"""
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    javascript_scripts = soup.find_all('script', {'type': 'text/javascript'})
    for script_tag in javascript_scripts:
        script_text = script_tag.text
        match = re.search(r'\"readyVideoUrl\"\s*:\s*\"(.*?)\"', script_text)
        if match:
            return match.group(1)
    return None

def extract_audio_from_video(video_path, title):
    """从视频中提取音频并保存为MP3文件"""
    audio_file_path = f'./音频/{title}.mp3'
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file_path)
        print(f"成功提取音频到{audio_file_path}")
    except Exception as e:
        print(f"提取音频失败: {str(e)}")

def batch_download_video(url_list, headers):
    """批量下载视频"""
    for url in url_list:
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text

        video_path = download_video(url, title, headers)
        if video_path:
            extract_audio_from_video(video_path, title)

def main():
    bilibili_url = "https://m.bilibili.com/video/BV1NM4y1d7aC?p="
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36 Edg/92.0.902.55'
    }

    create_folder('视频')
    create_folder('音频')

    # 要修改的地方，修改批量下载的链接列表
    url_list = [bilibili_url + str(i) for i in range(63, 71)]
    batch_download_video(url_list, headers)


if __name__ == "__main__":
    main()
