import textwrap

from PIL import Image, ImageDraw, ImageFont


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY100 = (25, 25, 25)
    GRAY200 = (50, 50, 50)
    GRAY300 = (75, 75, 75)
    GRAY400 = (100, 100, 100)
    GRAY500 = (125, 125, 125)
    GRAY600 = (150, 150, 150)
    GRAY700 = (175, 175, 175)
    GRAY800 = (200, 200, 200)
    GRAY900 = (225, 225, 225)
    RED100 = (255, 0, 0)
    RED200 = (255, 25, 25)
    RED300 = (255, 50, 50)
    RED400 = (255, 75, 75)
    RED500 = (255, 100, 100)
    RED600 = (255, 125, 125)
    RED700 = (255, 150, 150)
    RED800 = (255, 175, 175)
    RED900 = (255, 200, 200)
    GREEN100 = (0, 255, 0)
    GREEN200 = (25, 255, 25)
    GREEN300 = (50, 255, 50)
    GREEN400 = (75, 255, 75)
    GREEN500 = (100, 255, 100)
    GREEN600 = (125, 255, 125)
    GREEN700 = (150, 255, 150)
    GREEN800 = (175, 255, 175)
    GREEN900 = (200, 255, 200)
    BLUE100 = (0, 0, 255)
    BLUE200 = (25, 25, 255)
    BLUE300 = (50, 50, 255)
    BLUE400 = (75, 75, 255)
    BLUE500 = (100, 100, 255)
    BLUE600 = (125, 125, 255)

    BLUE_GREY300 = (75, 75, 75)
    BLUE_GREY400 = (100, 110, 120)
    BLUE_GREY500 = (102, 153, 204)
    BLUE_GREY600 = (102, 153, 204)
    BLUE_GREY700 = (102, 153, 204)
    BLUE_GREY800 = (102, 153, 204)
    BLUE_GREY900 = (102, 153, 204)


def draw_comment_to_path(path: str, comment_content: str, profile_img_path: str, name, time="", like=0):
    resize_factor = 4

    warp_width = 20
    content_font_size = 32 * resize_factor
    name_font_size = 30 * resize_factor
    profile_img_size = 128 * resize_factor

    edge_padding = 40 * resize_factor
    content_x_padding = 20 * resize_factor
    content_y_padding = 10 * resize_factor

    profile_img = Image.open(profile_img_path)
    profile_img = profile_img.resize((profile_img_size, profile_img_size))

    content_font = ImageFont.truetype("TaipeiSansTCBeta-Regular.ttf", content_font_size)
    name_font = ImageFont.truetype("TaipeiSansTCBeta-Bold.ttf", name_font_size)

    raw_lines = comment_content.split("\n")

    lines = []

    for raw_line in raw_lines:
        lines.extend(textwrap.wrap(raw_line, warp_width))

    max_comment_width = max([content_font.getsize(line)[0] for line in lines])
    user_name_width = name_font.getsize(name)[0]
    total_comment_height = sum([content_font.getsize(line)[1] for line in lines])

    base_width = edge_padding * 2 + content_x_padding + profile_img_size

    image_width = max(max_comment_width + base_width, user_name_width + base_width)

    base_height = edge_padding * 2
    image_height = max(
        total_comment_height + base_height + name_font_size + content_y_padding,
        profile_img_size + base_height
    )

    img = Image.new("RGB", (image_width, image_height), Colors.WHITE)
    img_draw = ImageDraw.Draw(img)

    # Draw profile Pic
    img.paste(profile_img, (edge_padding, edge_padding))

    # Draw name
    name_x_offset = edge_padding + profile_img_size + content_x_padding
    name_y_offset = edge_padding
    img_draw.text(
        (name_x_offset, name_y_offset),
        name,
        Colors.BLUE_GREY400,
        font=name_font
    )

    # Draw content
    comment_x_offset = name_x_offset
    comment_y_offset = edge_padding + name_font_size + content_y_padding

    y = 0
    for line in lines:
        # print(f"Drawing line: {line}")
        img_draw.text((comment_x_offset, y + comment_y_offset), line, Colors.BLACK, font=content_font)
        y += content_font.getsize(line)[1]
    img.save(path)


def main():
    draw_comment_to_path(
        "test.png",
        "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
        "profilePic.png", "犬飼ゆいdfdsfddfs")


if __name__ == '__main__':
    main()
