import requests
from fake_useragent import UserAgent

from classes.export import Export


def get_data() -> list:
    vehicles = []
    ua = UserAgent()

    cookies = {
        'laquesis': 'cars-33522@b#cars-34184@a#cars-36794@b#cars-37743@b#cars-38418@b#cars-38824@b#cars-38834@a#cars-39185@b#cars-40275@a#cars-40386@b#cars-40725@b#cars-41189@a#cars-41196@a#cars-41420@b#cars-41538@b#cars-41542@a#cars-42079@a#euads-3587@a#mcta-682@a',
        'lqstatus': '1678208824',
        'dfp_user_id': 'e2124f00-bdda-4c39-a7c2-2a742c335d41-ver2',
        'OptanonAlertBoxClosed': '2023-03-07T16:44:08.441Z',
        'eupubconsent-v2': 'CPoSiJHPoSiJ1AcABBENC6CgAAAAAH_AAAYgJSNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-QSjAJMNW4gC7MscGbaMIoEQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkACAUATgRAhwBRgwCAAASAJCIgJAjwQCAAiAQAAgAVCIQAMbAILACwEAgAFANCxRigCECQgyICIpTAgKkSCgnsqEEoP9DTCEOssAKDR_xUICNZAxWBEJCwchwRICXiyQPMUb5ACMAKAUSoVqKT00BAAA.YAAAD_gAAAAA',
        'OTAdditionalConsentString': '1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931',
        'PHPSESSID': '5nlabsjdkbd6nksq8lscqq1u05',
        'mobile_default': 'desktop',
        'rtbhouse-split': '4',
        'xtvrn': '$remove$',
        'sceuidjs': 'af49f106-98e0-4482-98e6-8c586fa00036',
        'ock': '0vsW6TRRViMeXQjJCuTu6Gay17-TDFaGcYQs3PxjL_k.',
        'vinCounter': '0',
        'ldf': 'r8wDM1iA',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Mar+08+2023+15%3A57%3A57+GMT%2B0500+(Yekaterinburg+Standard+Time)&version=6.31.0&isIABGlobal=false&hosts=&genVendors=V4%3A0%2CV3%3A0%2CV9%3A0%2C&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2Cgad%3A0%2CSTACK42%3A0&geolocation=RU%3BUD&AwaitingReconsent=false',
    }
    headers = {
        'authority': 'www.otomoto.pl',
        'accept': 'application/graphql+json, application/json',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'dnt': '1',
        'referer': 'https://www.otomoto.pl/ciezarowe/uzytkowe/volvo/od-2010/q-Volvo-FH?search%5Bfilter_enum_gearbox%5D=automatic&search%5Bfilter_float_price%3Ato%5D=150000&search%5Bfilter_enum_damaged%5D=0&search%5Border%5D=created_at_first%3Adesc&search%5Badvanced_search_expanded%5D=true',
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
        'variables': '{"categoryId":"57","click2BuyExperimentId":"CARS-34184","click2BuyExperimentVariant":"a","experiments":[{"key":"MCTA-682","variant":"a"},{"key":"MCTA-685","variant":"a"}],"filters":[{"name":"filter_enum_make","value":"volvo"},{"name":"filter_enum_gearbox","value":"automatic"},{"name":"filter_enum_damaged","value":"0"},{"name":"q","value":"Volvo FH"},{"name":"subcategory_id","value":"81"},{"name":"order","value":"created_at_first:desc"},{"name":"category_id","value":"57"},{"name":"filter_float_year:from","value":"2010"},{"name":"filter_float_price:to","value":"150000"}],"includeClick2Buy":false,"includeFiltersCounters":false,"includePriceEvaluation":false,"includePromotedAds":false,"includeRatings":false,"includeSortOptions":false,"maxAge":60,"page":1,"parameters":["make","offer_type","year","mileage","engine_capacity","fuel_type"],"searchTerms":null,"sortBy":"created_at_first:desc"}',
        'extensions': '{"persistedQuery":{"sha256Hash":"73eb8ed8efd659872656208529da9f1b5eeaae1bf6cfc3ceb6aca04fccc0b198","version":1}}',
    }

    response = requests.get('https://www.otomoto.pl/graphql', params=params, cookies=cookies, headers=headers)

    # with open('data.json', 'r', encoding='utf-8') as file:
    #     response = json.load(file)

    edges = response.json()['data']['advertSearch']['edges']
    for edge in edges:
        vehicle_id = edge['node']['id']
        title = edge['node']['title']
        if edge['node']['thumbnail'] != 'null':
            picture = [edge['node']['thumbnail']['x1'].split(';')[0]]
        else:
            picture = ['https://excelautomationinc.com/wp-content/uploads/2021/07/No-Photo-Available.jpg']
        link = edge['node']['url']
        price = int(int(edge['node']['price']['amount']['units']) / 4.3987) + 15000
        info = edge['node']['shortDescription']
        location = edge['node']['location']['region']['name'] + ' (' + edge['node']['location']['city']['name'] + ')'

        if ('fh 460' in title.lower() or 'fh460' in title.lower() or 'fh500' in title.lower() or 'fh 500' in title.lower()) or \
                'fh 460' in info.lower() or 'fh460' in info.lower() or 'fh500' in info.lower() or 'fh 500' in info.lower():
            vehicles.append(Export(vehicle_id=vehicle_id,
                                   link=link,
                                   title=title,
                                   picture=picture,
                                   price=price,
                                   info=info,
                                   location=location))

    return vehicles
