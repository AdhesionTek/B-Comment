import re


def to_safe_path(s: str):
    output = s
    output = output.replace("[", "【")
    output = output.replace("]", "】")
    output = output.replace(":", "：")
    output = output.replace("/", "／")
    output = output.replace("\\", "＼")
    output = output.replace("?", "？")
    output = output.replace("*", "＊")
    output = output.replace("<", "＜")
    output = output.replace(">", "＞")
    # output = output.replace(".", "。")
    output = output.replace("|", "｜")
    output = output.replace('\n', " ")
    output = output.replace('\r', " ")
    output = output.replace('\t', " ")
    output = output.replace('\f', " ")
    output = output.replace('\v', " ")
    output = output.replace('\a', " ")
    output = output.replace('\b', " ")
    output = output.replace('"', "”")
    # output = re.sub(r'[\\/:*?"<>|\[\]]', "_", output)

    return output
