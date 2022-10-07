from bilibili_api import comment, sync
from bilibili_api.video import Video

"""
Class to store comment information
"""


class CommentDescriptor:
    def __init__(self, content, user_name, user_profile_url):
        self.content = content
        self.user_name = user_name
        self.user_profile_url = user_profile_url

    def __str__(self):
        return f"{self.user_name}:\n{self.content}\n \n{self.user_profile_url}"


async def get_video_comments(video: Video, log=True):
    oid = video.get_aid()

    comments = []
    page = 1
    count = 0
    while True:

        c = await comment.get_comments(oid, comment.ResourceType.VIDEO, page)

        replies = c["replies"]
        for reply in replies:

            new_comment = CommentDescriptor(reply["content"]["message"], reply["member"]["uname"],
                                            reply["member"]["avatar"])
            comments.append(new_comment)
            if log:
                print(new_comment)

            print(f"Comment num: {len(comments)}", end="\r")
        page += 1

        count += c['page']['size']

        if count >= c['page']['count']:
            break

    print(f"Total comments: {len(comments)} (NOT including replies)")
    return comments


if __name__ == "__main__":
    sync(get_video_comments(Video(bvid="BV1CB4y1b7NX")))
