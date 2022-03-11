
import sys
import os
import requests

def merge(input1: str = "webcams.mp4", input2: str="deskshare.mp4", output: str="presentation.mp4"):
    os.popen(f"ffmpeg -i {input1} -i {input2} -c copy {output}").read()



class Download:
    def __init__(self, settings: dict) -> None:
        self.base_url = settings["dwpath_led"]
        self.sessionid = settings["sessionid"]
        self.sessionno = settings["dwpath_led"]
    

link = "https://conf2.anisa.co.ir/presentation/" + "7c73890a6bb99b872fce98138ab61735d96e3ddb-1646888881275" + "/video/webcams.mp4"
file_name = "download.data"
with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        print(total_length, f"{total_length//1024//1024}MB")
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(100 * dl / total_length)
            sys.stdout.write(f"\r[{'=' * done}{' ' * (100-done)}] {done:.2f}%")    
            sys.stdout.flush()