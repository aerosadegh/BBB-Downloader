import os
import sys
import subprocess
import requests


def merge(
    input1: str = "webcams.mp4",
    input2: str = "deskshare.mp4",
    output: str = "presentation.mp4",
):
    # with open('test.log', 'wb') as fout:
    process = subprocess.Popen(
        f"ffmpeg -i {input1} -i {input2} -c copy {output} -y".split(),
        stdout=subprocess.PIPE,
    )
    return process.communicate()[0]


class Download:
    def __init__(self, base_url, sessionid, path, extension="mp4") -> None:
        self.base_url = base_url.rstrip("/") + "/"  # settings["dwpath_led"].rstrip("/") + "/"
        self.sessionid = sessionid  # settings["sessionid"]
        self.extension = extension  # settings["ext_cb"]
        self.path = path  # settings["dwpath_led"]
        if not os.path.exists(path):
            os.makedirs(path)

    def get_iter_videos(self):
        yield self._get_webcams()
        yield self._get_deskshare()

    @staticmethod
    def _to_download(
        file_path,
        link,
        resume_byte_pos=None,
    ):
        print(f"Downloading {file_path}")
        headers = {"Range": f"bytes={resume_byte_pos}-"} if resume_byte_pos is not None else None
        print("headers:", headers)
        response = requests.get(link, stream=True, headers=headers)
        total_length = response.headers.get("content-length")
        if total_length is None:  # no content length header
            print(response.content)
        else:
            total_length = int(total_length)
            download_flag = True
            if os.path.exists(file_path):
                print(os.path.getsize(file_path) == total_length)
                if os.path.getsize(file_path) == total_length:
                    download_flag = False
                    yield (total_length, total_length)

            if download_flag:
                with open(file_path, "ab") as fout:
                    if total_length is None:  # no content length header
                        fout.write(response.content)
                    else:
                        dld = 0 if resume_byte_pos is None else resume_byte_pos
                        total_length = int(total_length) if resume_byte_pos is None else int(total_length) + resume_byte_pos
                        print(total_length, f"{total_length//1024//1024}MB")
                        for data in response.iter_content(chunk_size=4096):
                            dld += len(data)
                            fout.write(data)
                            # done = int(100 * dld / total_length)
                            yield (dld, total_length)

    def _get_webcams(self):
        link = f"{self.base_url}{self.sessionid}/video/webcams.{self.extension}"
        print("link: ", link)
        filename = os.path.join(self.path, "webcams.mp4")
        resume_from = None
        if os.path.exists(filename):
            resume_from = os.path.getsize(filename)
        return Download._to_download(filename, link, resume_byte_pos=resume_from)

    def _get_deskshare(self):
        link = f"{self.base_url}{self.sessionid}/deskshare/deskshare.{self.extension}"
        print("link: ", link)
        filename = os.path.join(self.path, "deskshare.mp4")
        resume_from = None
        if os.path.exists(filename):
            resume_from = os.path.getsize(filename)
        return Download._to_download(filename, link, resume_byte_pos=resume_from)

    def do_merge(self):
        merge(
            os.path.join(self.path, "webcams.mp4"),
            os.path.join(self.path, "deskshare.mp4"),
            os.path.join(self.path, "presentation.mp4"),
        )


# link = "https://conf2.anisa.co.ir/presentation/" + "7c73890a6bb99b872fce98138ab61735d96e3ddb-1646888881275" + "/video/webcams.mp4"
# file_name = "download.data"
# with open(file_name, "wb") as f:
#     print("Downloading %s" % file_name)
#     response = requests.get(link, stream=True)
#     total_length = response.headers.get('content-length')

#     if total_length is None: # no content length header
#         f.write(response.content)
#     else:
#         dl = 0
#         total_length = int(total_length)
#         print(total_length, f"{total_length//1024//1024}MB")
#         for data in response.iter_content(chunk_size=4096):
#             dl += len(data)
#             f.write(data)
#             done = int(100 * dl / total_length)
#             sys.stdout.write(f"\r[{'=' * done}{' ' * (100-done)}] {done:.2f}%")
#             sys.stdout.flush()


if __name__ == "__main__":

    LINK = "https://conf2.anisa.co.ir/presentation/" + "7c73890a6bb99b872fce98138ab61735d96e3ddb-1646888881275" + "/video/webcams.mp4"
    BASEURL = "https://conf2.anisa.co.ir/presentation/"
    SESSION_ID = "7c73890a6bb99b872fce98138ab61735d96e3ddb-1646888881275"
    # path = 6
    dl = Download(BASEURL, SESSION_ID, ".")

    if input().strip() != "":
        for itr in dl.get_iter_videos():
            for (dnl, totallength) in itr:
                sys.stdout.write(
                    f"\r[{'=' * int(100 * dnl / totallength)}"
                    f"{' ' * (100-int(100 * dnl / totallength))}] {int(100 * dnl / totallength):.0f}%"
                )
                sys.stdout.flush()
