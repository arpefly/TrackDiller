import functools
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from classes.export import Export
from create_bot import db
from utils import water_mark


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} {func.__name__} took {runtime:.4f} secs")
        return result

    return _wrapper


@timer
def get_data(convert_from_pln: int, convert_from_eur: int) -> list[Export]:
    vehicles = []
    ua = UserAgent()

    # get available trailer trucks on olx.pl
    cookies = {
        'dfp_user_id': 'e6bbe5ce-df27-4870-8ab4-836627ac9be4-ver2',
        'laquesisff': 'a2b-000#aut-388#buy-2279#buy-2489#dat-2874#decision-256#do-2963#do-3418#euit-2250#euonb-114#euweb-1372#euweb-451#grw-124#kuna-307#kuna-554#kuna-603#mou-1052#oesx-1437#oesx-1643#oesx-645#oesx-867#olxeu-0000#psm-308#psm-402#psm-457#psm-574#sd-570#ser-87#srt-1289#srt-1346#srt-1434#srt-1593#srt-1758#srt-683#uacc-529',
        'laquesissu': '297@ad_page|1#297@reply_phone_1step|1',
        'observed_aui': 'd9eb320e54cf435f8e31c4de80e722f8',
        '_ga': 'GA1.1.435354839.1678265802',
        'OptanonAlertBoxClosed': '2023-03-08T08:56:44.539Z',
        'OTAdditionalConsentString': '1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931',
        'deviceGUID': '75af6303-19a3-490a-a326-14232f5fe2fe',
        'a_refresh_token': 'c8c84e50a180cd74ca6ea25b995e658f29745a60',
        'a_grant_type': 'device',
        'user_business_status': 'private',
        'user_id': '1477967603',
        'lister_lifecycle': '1678265944',
        '_hjSessionUser_1685071': 'eyJpZCI6IjhhZGFkZDRkLTdmY2QtNTA5Ny1hMWFmLWU1ZWE1N2QxYzU1ZSIsImNyZWF0ZWQiOjE2NzgyNjU4MDExOTEsImV4aXN0aW5nIjp0cnVlfQ==',
        'PHPSESSID': '65vlo44c7dmfilm1r2hvm6bd0o',
        'mobile_default': 'desktop',
        'fingerprint': 'MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTsxOzA7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MTsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzEzMDE3NjU0OTk7MjsyOzI7MjsyOzI7NTsyODQ4MDA2NDE4OzEzNTcwNDE3Mzg7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MTswOzQxMDAyMTk5OzM0NjkzMDY1NTE7NjQyMzAyMDI2Ozc4NTI0NzAyOTsxMDA1MzAxMjAzOzE5MjA7MTA4MDsyNDsyNDszNjA7MzAwOzM2MDszMDA7MzYwOzMwMDszNjA7MzAwOzM2MDszNjA7MzYwOzM2MDszNjA7MzYwOzM2MDszMDA7MzAwOzMwMDszMDA7MzAwOzA7MDsw',
        'laquesis': 'cars-33613@b#er-2114@a#erm-1031@b#euads-3502@b#f8nrp-1502@b#jobs-4644@a#jobs-4750@b#jobs-4757@a#jobs-4982@b#jobs-4989@b#jobs-5077@b#jobs-5103@b#jobs-5169@a#jobs-5187@a#jobs-5188@a#jobs-5229@b#oesx-2534@c#olxeu-40264@a',
        'from_detail': '0',
        'eupubconsent-v2': 'CPoUwncPoUwncAcABBENC7CgAAAAAH_AAAYgJSNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-QSbAJMNW4gC7EscCbaMIoEQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkACAUARgRAhwBRgwCAAACAJCIgJAjwQCAAiAQAAgAVCIQAEbAIKACwEAgAFANCxRigCECQgyICIpTAgIkSCgnsqEEoP9DTCEOssAKDR_xUICJQAhWBEJCwchwRICXiyQLMUb5ACMAKAUSoVqCT00AAAA.YAAAD_gAAAAA',
        '_hjSession_1685071': 'eyJpZCI6ImE2YWVmYTUwLTE0ZjItNGJlNy05YmQzLWJkODMzN2VkNTA3ZCIsImNyZWF0ZWQiOjE2Nzg2MDMxNjQwMjEsImluU2FtcGxlIjpmYWxzZX0=',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2023-03-12%2011%3A40%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fdostawcze%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.pl%2F',
        'sbjs_first_add': 'fd%3D2023-03-12%2011%3A40%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fdostawcze%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.pl%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.0.0%20Safari%2F537.36',
        'newrelic_cdn_name': 'CF',
        'dfp_segment': '%5B%5D',
        'a_access_token': '3326ada28e9c39090a70fec362e9d2a77886d240',
        'lqstatus': '1678604480|186d48b88b5xc26c016|euads-3502#er-2114||',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Mar+12+2023+11%3A48%3A24+GMT%2B0500+(Yekaterinburg+Standard+Time)&version=6.19.0&isIABGlobal=false&hosts=&genVendors=V9%3A0%2C&consentId=856ff7e0-4429-44a0-b9a3-593eb514ee50&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2Cgad%3A0%2CSTACK42%3A0&geolocation=RU%3BUD&AwaitingReconsent=false',
        '_ga_V1KE40XCLR': 'GS1.1.1678603163.2.1.1678603749.17.0.0',
        'session_start_date': '1678605813545',
        'onap': '186c06fd946x2803cc00-2-186d48b88b5xc26c016-67-1678605814',
        'sbjs_session': 'pgs%3D33%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fciezarowe%2Fplandeka-firana%2F%3Fsearch%255Border%255D%3Dcreated_at%3Adesc%26search%255Bfilter_enum_mark%255D%255B0%255D%3Dvolvo%26search%255Bfilter_enum_mark%255D%255B1%255D%3Ddaf%26search%255Bfilter_enum_mark%255D%255B2%255D%3Dscania%26search%255Bfilter_enum_mark%255D%255B3%255D%3Dmercedes-benz%26search%255Bfilter_float_axes%3Afrom%255D%3D3%26search%255Bfilter_float_price%3Afrom%255D%3D10000%26search%255Bfilter_float_price%3Ato%255D%3D150000%26search%255Bfilter_float_year%3Afrom%255D%3D2010',
    }
    headers = {
        'authority': 'www.olx.pl',
        'accept': '*/*',
        'accept-language': 'pl',
        'authorization': 'Bearer 3326ada28e9c39090a70fec362e9d2a77886d240',
        'dnt': '1',
        'referer': 'https://www.olx.pl/motoryzacja/ciezarowe/plandeka-firana/?search%5Border%5D=created_at:desc&search%5Bfilter_enum_mark%5D%5B0%5D=volvo&search%5Bfilter_enum_mark%5D%5B1%5D=daf&search%5Bfilter_enum_mark%5D%5B2%5D=scania&search%5Bfilter_enum_mark%5D%5B3%5D=mercedes-benz&search%5Bfilter_float_axes:from%5D=3&search%5Bfilter_float_price:from%5D=10000&search%5Bfilter_float_price:to%5D=150000&search%5Bfilter_float_year:from%5D=2010',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': ua.random,
        'x-client': 'DESKTOP',
        'x-device-id': '75af6303-19a3-490a-a326-14232f5fe2fe',
        'x-platform-type': 'mobile-html5',
    }
    params = {
        'offset': '0',
        'limit': '40',
        'category_id': '3585',
        'sort_by': 'created_at:desc',
        'filter_enum_mark[0]': 'volvo',
        'filter_enum_mark[1]': 'daf',
        'filter_enum_mark[2]': 'scania',
        'filter_enum_mark[3]': 'mercedes-benz',
        'filter_float_axes:from': '3',
        'filter_float_price:from': '30000',
        'filter_float_price:to': '150000',
        'filter_float_year:from': '2010',
        'filter_refiners': 'spell_checker',
        'facets': '[{"field":"region","fetchLabel":true,"fetchUrl":true,"limit":30},{"field":"category_without_exclusions","fetchLabel":true,"fetchUrl":true,"limit":10}]',
        'sl': '186c06fd946x2803cc00',
    }

    response = requests.get('https://www.olx.pl/api/v1/offers/', params=params, cookies=cookies, headers=headers).json()

    data = response['data']
    for item in data:

        # continute if the vehicle has already been parsed
        vehicle_id = item['id']
        if db.vehicle_exists(site_name='olx', vehicle_id=vehicle_id):
            continue

        year = get_year(item['params'])
        if try_parse_int(year) < 2010:
            continue

        photos = ';'.join(list(filter(str.strip, [photo['link'].split(';')[0] for photo in item['photos']])))
        if len(photos.split(';')) == 0:
            continue

        photos = ';'.join(list(filter(str.strip, water_mark(site_name='olx', vehicle_id=vehicle_id, photos=photos))))

        link = item['url']
        title = item['title']
        info = BeautifulSoup(item['description'], 'lxml').text or item['description']
        price = get_price(item['params'], convert_from_pln, convert_from_eur)
        location = item['location']['region']['name'] + ' (' + item['location']['city']['name'] + ')'
        site_name = 'olx'
        automat = get_automat(item['params'])

        vehicles.append(Export(vehicle_id=vehicle_id,
                               link=link,
                               title=title,
                               photos=photos,
                               price=price,
                               info=info,
                               location=location,
                               site_name=site_name,
                               year=year,
                               transmission=automat))

    return vehicles


def get_price(params: dict, convert_from_PLN: int, convert_from_EUR: int) -> int:
    for item in params[:5]:
        if 'price' in item['key']:
            if item['value']['currency'] == 'PLN':
                return int(item['value']['value'] * convert_from_PLN) + 15000
            elif item['value']['currency'] == 'EUR':
                return int(item['value']['value'] * convert_from_EUR) + 15000

    return 0


def get_year(params: dict) -> str:
    for item in params:
        if 'year' in item['key']:
            return item['value']['label'].strip()

    return 'нет информации'


def get_automat(params: dict) -> str:
    for item in params:
        if 'transmission' in item['key']:
            transmission_type = item['value']['key']
            if transmission_type == 'automatic':
                return 'Автомат'
            elif transmission_type == 'manual':
                return 'Механика'
            else:
                return 'нет информации'

    return 'нет информации'


def try_parse_int(string):
    try:
        return int(string)
    except:
        return 0
