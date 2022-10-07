import time

import requests

from SafePath import to_safe_path


def download_url_to(path: str, url: str):
    filename_without_extension = to_safe_path(get_url_filename_without_extension(url))
    # extension = get_url_extension(url)
    download_path = f"{path}/{filename_without_extension}_{int(time.time())}.{get_url_extension(url)}"
    try:
        with open(download_path, "wb") as f:
            f.write(requests.get(url).content)
    except Exception as e:
        print(f"Unable to download {url}")
        print(e)

    return download_path


def get_url_extension(url: str) -> str:
    return url[url.rfind("."):]


def get_url_filename(url: str) -> str:
    return url[url.rfind("/") + 1:]


def get_url_filename_without_extension(url: str) -> str:
    return url[url.rfind("/") + 1:url.rfind(".")]
