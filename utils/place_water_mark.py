from io import BytesIO
import multiprocessing
from functools import partial

from PIL import Image, ImageDraw, ImageFont
import requests


def place_mark(site_name: str, vehicle_id: int, url: str) -> str:
    if url == '':
        return ''

    image = Image.open(BytesIO(requests.get(url).content))
    box = (0, image.size[1] - image.size[1] * 0.07, image.size[0], image.size[1])
    draw = ImageDraw.Draw(image)
    draw.rectangle(box, fill="#FFFFFF")

    text = "Напишите на WhatsApp +996 705 817 477"
    font_size = 80
    size = None
    font = ImageFont.truetype(r'C:\Users\wasd\AppData\Local\Microsoft\Windows\Fonts\Croogla4F.ttf', font_size)
    while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
        size = font.getsize_multiline(text)
        font_size -= 1
        font = ImageFont.truetype(r'C:\Users\wasd\AppData\Local\Microsoft\Windows\Fonts\Croogla4F.ttf', font_size)

    if font_size > 30:
        font_size = 28
        font = ImageFont.truetype(r'C:\Users\wasd\AppData\Local\Microsoft\Windows\Fonts\Croogla4F.ttf', font_size)

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
