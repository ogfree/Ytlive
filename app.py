import subprocess
import os

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
            pass
    except KeyboardInterrupt:
        process.terminate()
        print("Livestream process terminated.")

if __name__ == "__main__":
    video_url = "https://rr1---sn-p5qddn76.googlevideo.com/videoplayback?expire=1706109186&ei=otSwZeLyDOD7zLUP_-ineA&ip=35.245.111.34&id=o-AKGozhCeQvMvCRFxarmj4OUYj_UygJFpTQWCjLY_0rV1&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=T8&mm=31%2C26&mn=sn-p5qddn76%2Csn-ab5sznzz&ms=au%2Conr&mv=u&mvi=1&pl=20&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=532.387&lmt=1582612547973840&mt=1706087202&fvip=3&fexp=24007246&c=ANDROID_MUSIC&txp=6316222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRAIgQkpClIX3NRtghDGDU12ItjdOPaaKKe9jRm1X0e1KVjoCIBwavN6Q9ajEO8ZNUGa6dm-H4jMISn_-aMXOpIVdlZ1C&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AAO5W4owRAIgTd8ILV0U5q3TSXJ2YGjFtp0Z5monrRPIbuecjtzUmlACIEm9ygL61fTSbi-vacfglAQZykVfvLHmsuCFN-o13HwL"
    stream_key = "ymfp-azxz-0mw0-rv6x-9jxg"
    
    start_livestream(video_url, stream_key)
