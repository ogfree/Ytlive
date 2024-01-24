import subprocess
import os
import speedtest
import time

def get_upload_speed():
    st = speedtest.Speedtest()
    upload_speed = st.upload() / 10**6
    return upload_speed

def read_config():
    with open("config.txt", "r") as file:
        config = {}
        for line in file:
            key, value = line.strip().split(": ")
            config[key] = value
        return config

def start_livestream(video_url, stream_key):
    command = (
        f"ffmpeg -re -i '{video_url}' "
        f"-c:v libx264 -b:v 800k -c:a aac -strict experimental "
        f"-b:a 128k -bufsize 1024k -maxrate 1024k -r 30 -g 60 "
        f"-f flv rtmp://x.rtmp.youtube.com/live2/{stream_key}"
    )

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        while True:
            upload_speed = get_upload_speed()
            print(f"Upload Speed: {upload_speed:.2f} Mbps", end='\r')
            time.sleep(1)
            os.system('clear')
    except KeyboardInterrupt:
        process.terminate()
        print("\nLivestream process terminated.")

if __name__ == "__main__":
    config = read_config()
    video_url = config.get("VideoURL", "")
    stream_key = config.get("StreamKey", "")
    
    if video_url and stream_key:
        start_livestream(video_url, stream_key)
    else:
        print("Please provide a valid VideoURL and StreamKey in the config.txt file.")
