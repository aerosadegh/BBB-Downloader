
import os

def merge(input1: str = "webcams.mp4", input2: str="deskshare.mp4", output: str="presentation.mp4"):
    os.popen(f"ffmpeg -i {input1} -i {input2} -c copy {output}").read()

