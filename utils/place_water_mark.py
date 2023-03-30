from io import BytesIO
import multiprocessing
from functools import partial

from PIL import Image, ImageDraw, ImageFont
import requests
from fake_useragent import UserAgent


def place_mark(site_name: str, vehicle_id: int, url: str) -> str:
    if url == '':
        return ''

    ua = UserAgent()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'if-modified-since': 'Tue, 21 Mar 2023 13:16:25 GMT',
        'if-none-match': '"dp0ar8ktx7ha-PL"',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.random
    }
    try:
        image = Image.open(BytesIO(requests.get(url, headers=headers).content)).convert('RGB')
    except Exception as ex:
        print(ex)
        return ''

    box = (0, image.size[1] - image.size[1] * 0.07, image.size[0], image.size[1])
    draw = ImageDraw.Draw(image)
    draw.rectangle(box, fill="#FFFFFF")

    text = "Напишите на WhatsApp +996 705 817 477"
    font_size = 80
    size = None
    font = ImageFont.truetype('fonts/Croogla4F.ttf', font_size)
    while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
        size = font.getsize_multiline(text)
        font_size -= 1
        font = ImageFont.truetype('fonts/Croogla4F.ttf', font_size)

    if font_size > 30:
        font_size = 28
        font = ImageFont.truetype('fonts/Croogla4F.ttf', font_size)

    draw.multiline_text((box[0], box[1]), text, "#000000", font)

    path = f'photos/{site_name}/{vehicle_id}@{url.split("/")[-2]}.jpg'

    image.save(path)

    return path


def water_mark(site_name: str, vehicle_id: int, photos: str) -> list:
    partial_func = partial(place_mark, site_name, vehicle_id)
    photos = [photo for photo in photos.split(';') if photo.strip()]

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        water_photos = pool.map(partial_func, photos)

    return water_photos
