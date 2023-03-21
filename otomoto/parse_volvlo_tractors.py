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

    # get available trucks on otomoto.pl
    cookies = {
        'laquesis': 'cars-33522@b#cars-34184@a#cars-36794@b#cars-37743@b#cars-38418@b#cars-38824@b#cars-38834@a#cars-39185@b#cars-40275@a#cars-40386@b#cars-40725@b#cars-41189@a#cars-41196@a#cars-41420@b#cars-41538@b#cars-41542@a#cars-42079@a#euads-3587@a#mcta-682@a',
        'lqstatus': '1678208824',
        'dfp_user_id': 'e2124f00-bdda-4c39-a7c2-2a742c335d41-ver2',
        'OptanonAlertBoxClosed': '2023-03-07T16:44:08.441Z',
        'OTAdditionalConsentString': '1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931',
        'eupubconsent-v2': 'CPoSiJHPoSiJ1AcABBENC6CgAAAAAH_AAAYgJSNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-QSjAJMNW4gC7MscGbaMIoEQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkACAUATgRAhwBRgwCAAASAJCIgJAjwQCAAiAQAAgAVCIQAMbAILACwEAgAFANCxRigCECQgyICIpTAgKkSCgnsqEEoP9DTCEOssAKDR_xUICNZAxWBEJCwchwRICXiyQPMUb5ACMAKAUSoVqKT00BAAA.YAAAD_gAAAAA',
        'rtbhouse-split': '4',
        'xtvrn': '$remove$',
        'sceuidjs': 'af49f106-98e0-4482-98e6-8c586fa00036',
        'ldf': 'r8wDM1iA',
        '_ga': 'GA1.1.10838588.1678383399',
        '_ga_7SW5PHVD0K': 'GS1.1.1678383398.1.1.1678383419.0.0.0',
        'ock': 'jaA6tO0kvJoT03aSJQ4WsmNgbB_zZjW82LyLen0Yke4.',
        'PHPSESSID': '7bvo8vfomhuhiat2v0g13ks8nj',
        'mobile_default': 'desktop',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Mar+10+2023+02%3A36%3A37+GMT%2B0500+(Yekaterinburg+Standard+Time)&version=6.31.0&isIABGlobal=false&hosts=&genVendors=V4%3A0%2CV3%3A0%2CV9%3A0%2C&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2Cgad%3A0%2CSTACK42%3A0&geolocation=RU%3BUD&AwaitingReconsent=false',
    }
    headers = {
        'authority': 'www.otomoto.pl',
        'accept': 'application/graphql+json, application/json',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'dnt': '1',
        'referer': 'https://www.otomoto.pl/ciezarowe/uzytkowe/volvo/od-2010/q-fh?search%5Bfilter_enum_gearbox%5D=automatic&search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_float_price%3Ato%5D=150000&search%5Border%5D=created_at_first%3Adesc&page=2&search%5Badvanced_search_expanded%5D=true',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sitecode': 'otomotopl',
        'user-agent': ua.random,
    }
    params = {
        'operationName': 'listingScreen',
        'variables': '{"categoryId":"57","click2BuyExperimentId":"CARS-34184","click2BuyExperimentVariant":"a","experiments":[{"key":"MCTA-682","variant":"a"},{"key":"MCTA-685","variant":"a"}],"filters":[{"name":"filter_enum_make","value":"volvo"},{"name":"filter_enum_damaged","value":"0"},{"name":"q","value":"fh"},{"name":"subcategory_id","value":"81"},{"name":"order","value":"created_at_first:desc"},{"name":"category_id","value":"57"},{"name":"filter_float_year:from","value":"2010"},{"name":"filter_float_price:to","value":"150000"}],"includeClick2Buy":false,"includeFiltersCounters":false,"includePriceEvaluation":false,"includePromotedAds":false,"includeRatings":false,"includeSortOptions":false,"maxAge":60,"page":1,"parameters":["make","offer_type","year","mileage","engine_capacity","fuel_type"],"searchTerms":null,"sortBy":"created_at_first:desc"}',
        'extensions': '{"persistedQuery":{"sha256Hash":"73eb8ed8efd659872656208529da9f1b5eeaae1bf6cfc3ceb6aca04fccc0b198","version":1}}',
    }
    response = requests.get('https://www.otomoto.pl/graphql', params=params, cookies=cookies, headers=headers).json()

    edges = response['data']['advertSearch']['edges']
    for edge in edges:

        # continute if the vehicle has already been parsed
        vehicle_id = edge['node']['id']
        if db.vehicle_exists(site_name='otomoto', vehicle_id=vehicle_id):
            continue

        # continue if vehicle doesn't fit the description
        title = edge['node']['title']
        info = edge['node']['shortDescription']
        if not ('fh 460' in title.lower() or 'fh460' in title.lower() or 'fh500' in title.lower() or 'fh 500' in title.lower() or
                'fh 460' in info.lower() or 'fh460' in info.lower() or 'fh500' in info.lower() or 'fh 500' in info.lower() or
                '460' in title.lower() or '500' in title.lower() or '460' in info.lower() or '500' in info.lower()):
            continue

        # request for detailes photos
        cookies = {
            'laquesis': 'cars-33522@b#cars-34184@a#cars-36794@b#cars-37743@b#cars-38418@b#cars-38824@b#cars-38834@a#cars-39185@b#cars-40275@a#cars-40386@b#cars-40725@b#cars-41189@a#cars-41196@a#cars-41420@b#cars-41538@b#cars-41542@a#cars-42079@a#euads-3587@a#mcta-682@a',
            'lqstatus': '1678208824',
            'dfp_user_id': 'e2124f00-bdda-4c39-a7c2-2a742c335d41-ver2',
            'OptanonAlertBoxClosed': '2023-03-07T16:44:08.441Z',
            'OTAdditionalConsentString': '1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931',
            'eupubconsent-v2': 'CPoSiJHPoSiJ1AcABBENC6CgAAAAAH_AAAYgJSNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-QSjAJMNW4gC7MscGbaMIoEQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkACAUATgRAhwBRgwCAAASAJCIgJAjwQCAAiAQAAgAVCIQAMbAILACwEAgAFANCxRigCECQgyICIpTAgKkSCgnsqEEoP9DTCEOssAKDR_xUICNZAxWBEJCwchwRICXiyQPMUb5ACMAKAUSoVqKT00BAAA.YAAAD_gAAAAA',
            'rtbhouse-split': '4',
            'xtvrn': '$remove$',
            'sceuidjs': 'af49f106-98e0-4482-98e6-8c586fa00036',
            'ldf': 'r8wDM1iA',
            '_ga': 'GA1.1.10838588.1678383399',
            '_ga_7SW5PHVD0K': 'GS1.1.1678383398.1.1.1678383419.0.0.0',
            'ock': 'jaA6tO0kvJoT03aSJQ4WsmNgbB_zZjW82LyLen0Yke4.',
            'PHPSESSID': '7bvo8vfomhuhiat2v0g13ks8nj',
            'mobile_default': 'desktop',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Mar+10+2023+02%3A36%3A37+GMT%2B0500+(Yekaterinburg+Standard+Time)&version=6.31.0&isIABGlobal=false&hosts=&genVendors=V4%3A0%2CV3%3A0%2CV9%3A0%2C&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2Cgad%3A0%2CSTACK42%3A0&geolocation=RU%3BUD&AwaitingReconsent=false',
            'laquesis_result': 'cars-40386@b|t',
        }
        headers = {
            'authority': 'www.otomoto.pl',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'referer': 'https://www.otomoto.pl/ciezarowe/uzytkowe/volvo/od-2010/q-fh?search%5Bfilter_enum_gearbox%5D=automatic&search%5Bfilter_enum_damaged%5D=0&search%5Border%5D=created_at_first%3Adesc&search%5Bfilter_float_price%3Ato%5D=150000&search%5Badvanced_search_expanded%5D=true',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua.random
        }
        response = requests.get(f'https://www.otomoto.pl/{vehicle_id}', cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        photos = ';'.join(list(filter(str.strip, list(map(lambda pic: pic['data-lazy'].split(';')[0], soup.find_all('img', {'class': 'bigImage'})))[:5])))

        if len(photos.split(';')) == 0:
            continue

        photos = ';'.join(list(filter(str.strip, water_mark(site_name='otomoto', vehicle_id=vehicle_id, photos=photos))))

        year = get_year(soup)
        if try_parse_int(year) < 2010:
            continue

        link = edge['node']['url']
        if edge['node']['price']['amount']['currencyCode'] == 'EUR':
            price = int(int(edge['node']['price']['amount']['units']) * convert_from_eur) + 15000
        elif edge['node']['price']['amount']['currencyCode'] == 'PLN':
            price = int(int(edge['node']['price']['amount']['units']) * convert_from_pln) + 15000
        else:
            price = 0
        location = edge['node']['location']['region']['name'] + ' (' + edge['node']['location']['city']['name'] + ')'
        site_name = 'otomoto'
        automat = get_automat(soup)

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


def get_year(soup: BeautifulSoup) -> str:
    for item in soup.find_all('li', {'class': 'offer-params__item'}):
        if 'Rok produkcji' in item.text:
            return item.find('div').text.strip()

    return 'нет информации'


def get_automat(soup: BeautifulSoup) -> str:
    for item in soup.find_all('li', {'class': 'offer-params__item'}):
        if 'Skrzynia biegów' in item.text:
            if item.find('div').text.strip() == 'Manualna':
                return 'Механика'
            elif item.find('div').text.strip() == 'Automatyczna':
                return 'Автомат'

    return 'нет информации'


def try_parse_int(string):
    try:
        return int(string)
    except:
        return 0
