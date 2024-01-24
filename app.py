import subprocess
import os
import speedtest
import time  # Import the time module for sleep

def get_upload_speed():
    st = speedtest.Speedtest()
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    return upload_speed

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
            time.sleep(1)  # Sleep for 1 second to avoid excessive updates
            os.system('clear')  # Clear the terminal screen
    except KeyboardInterrupt:
        process.terminate()
        print("\nLivestream process terminated.")

if __name__ == "__main__":
    video_url = "https://your_video_url_here"
    stream_key = "your_stream_key_here"
    
    start_livestream(video_url, stream_key)
