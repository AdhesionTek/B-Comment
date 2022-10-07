import os
import sys
from typing import List

from bilibili_api import sync
from bilibili_api.video import Video

from FileDownloader import download_url_to
from GenVideoComments import CommentDescriptor, get_video_comments
from ImgGen import draw_comment_to_path
from SafePath import to_safe_path


async def generate_comment_pictures(output_path, comments: List[CommentDescriptor], log=True):
    temp_path = "temp"

    if not os.path.exists(output_path):
        os.mkdir(output_path)
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    for i in range(len(comments)):
        comment = comments[i]
        if log:
            print(
                f"[{get_progress_bar(i / len(comments))}] current comment ({i}/{len(comments)}) by {comment.user_name}", end="\r")
        # Download avatar
        avatar_path = download_url_to(temp_path, comment.user_profile_url)
        # Generate image
        img_path = os.path.join(output_path, f"{i + 1}_{to_safe_path(comment.content)[:100]}.png")
        draw_comment_to_path(path=img_path, comment_content=comment.content, name=comment.user_name,
                             profile_img_path=avatar_path)
        # Delete avatar
        os.remove(avatar_path)


def get_progress_bar(portion: float, length=20):
    s = ""

    t = int(portion * length)

    for i in range(length):
        if i < t:
            s += "="
        else:
            s += "-"
    return s


async def generate_video_comment_pictures(aid: int = None, bid: str = None, log=True):
    if aid is None and bid is None:
        raise ValueError("aid and bid cannot both be None")

    if aid is not None:
        video = Video(aid=aid)
    else:
        video = Video(bvid=bid)

    video_info = await video.get_info()
    video_title = video_info["title"]

    output_path = f"{to_safe_path(video_title)}_av{video.get_aid()}_comments"

    comments = await get_video_comments(video, log=False)
    await generate_comment_pictures(output_path, comments, log)


async def generate_dynamic_comment_pictures(dynamic_id, log=True):
    """
    TODO add support for dynamic comments
    """
    pass


usage = """
Usage: CommentPicGen.py -bv [bid] -av [aid]

bid: bvid of the video
aid: aid of the video


"""


async def async_main():
    print(sys.argv)
    if len(sys.argv) < 3:
        print(usage)
        return
    if sys.argv[1] == "-bv":
        await generate_video_comment_pictures(bid=sys.argv[2])
    elif sys.argv[1] == "-av":
        av = sys.argv[2]
        if av.isdigit():
            av = int(av)
        else:
            av = av[2:]
            if av.isdigit():
                av = int(av)
            else:
                print("Invalid aid")
                return
        await generate_video_comment_pictures(aid=av)
    else:
        print(usage)


if __name__ == "__main__":
    sync(async_main())
