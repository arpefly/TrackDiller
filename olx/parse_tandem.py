import re

import requests
from bs4 import BeautifulSoup
import lxml

from classes import Export


def get_data_tandems():
    vehicles = []

    import requests

    cookies = {
        'PHPSESSID': 'o98rqdi86anlnc139romrl6mlo',
        'mobile_default': 'desktop',
        'fingerprint': 'MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTsxOzA7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MTsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzEzMDE3NjU0OTk7MjsyOzI7MjsyOzI7NTsyODQ4MDA2NDE4OzEzNTcwNDE3Mzg7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MTswOzQxMDAyMTk5OzM0NjkzMDY1NTE7NjQyMzAyMDI2Ozc4NTI0NzAyOTsxMDA1MzAxMjAzOzE5MjA7MTA4MDsyNDsyNDszNjA7MzAwOzM2MDszMDA7MzYwOzMwMDszNjA7MzAwOzM2MDszNjA7MzYwOzM2MDszNjA7MzYwOzM2MDszMDA7MzAwOzMwMDszMDA7MzAwOzA7MDsw',
        'dfp_user_id': 'e6bbe5ce-df27-4870-8ab4-836627ac9be4-ver2',
        'laquesis': 'cars-33613@b#erm-1001@a#erm-1031@c#euads-3574@b#f8nrp-1502@b#jobs-4644@a#jobs-4672@b#jobs-4750@b#jobs-4757@a#jobs-4982@b#jobs-4989@b#jobs-5077@b#jobs-5103@b#jobs-5187@a#jobs-5188@a#oesx-2534@c#oesx-2597@b#olxeu-40264@a#olxeu-40383@b',
        'laquesisff': 'a2b-000#aut-388#buy-2279#buy-2489#dat-2874#decision-256#do-2963#do-3418#euit-2250#euonb-114#euweb-1372#euweb-451#grw-124#kuna-307#kuna-554#kuna-603#mou-1052#oesx-1437#oesx-1643#oesx-645#oesx-867#olxeu-0000#psm-308#psm-402#psm-457#psm-574#sd-570#ser-87#srt-1289#srt-1346#srt-1434#srt-1593#srt-1758#srt-683#uacc-529',
        'laquesissu': '297@ad_page|1#297@reply_phone_1step|1',
        '_hjFirstSeen': '1',
        '_hjSession_1685071': 'eyJpZCI6ImIzM2JmOTk4LWQ3NGMtNDhiMy04YmFjLWFhZjdkNmZmOGI0MyIsImNyZWF0ZWQiOjE2NzgyNjU4MDE3MTQsImluU2FtcGxlIjpmYWxzZX0=',
        'from_detail': '0',
        'observed_aui': 'd9eb320e54cf435f8e31c4de80e722f8',
        '_ga': 'GA1.1.435354839.1678265802',
        'OptanonAlertBoxClosed': '2023-03-08T08:56:44.539Z',
        'eupubconsent-v2': 'CPoUwncPoUwncAcABBENC6CgAAAAAH_AAAYgJSNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-QSbAJMNW4gC7EscCbaMIoEQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkACAUARgRAhwBRgwCAAACAJCIgJAjwQCAAiAQAAgAVCIQAEbAIKACwEAgAFANCxRigCECQgyICIpTAgIkSCgnsqEEoP9DTCEOssAKDR_xUICJQAhWBEJCwchwRICXiyQLMUb5ACMAKAUSoVqCT00AAAA.YAAAD_gAAAAA',
        'OTAdditionalConsentString': '1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931',
        'deviceGUID': '75af6303-19a3-490a-a326-14232f5fe2fe',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2023-03-08%2013%3A56%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fdostawcze%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.pl%2F',
        'sbjs_first_add': 'fd%3D2023-03-08%2013%3A56%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fdostawcze%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.pl%2F',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.0.0%20Safari%2F537.36',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'newrelic_cdn_name': 'CF',
        'a_access_token': '2fad9a8fe838b9009d8f37eda1db1df2fd226e87',
        'a_refresh_token': 'c8c84e50a180cd74ca6ea25b995e658f29745a60',
        'a_grant_type': 'device',
        'dfp_segment': '%5B%5D',
        'user_id': '1477967603',
        'user_business_status': 'private',
        'lqstatus': '1678267182|186c06fd946x2803cc00|euads-3574||',
        'lister_lifecycle': '1678265944',
        '_hjSessionUser_1685071': 'eyJpZCI6IjhhZGFkZDRkLTdmY2QtNTA5Ny1hMWFmLWU1ZWE1N2QxYzU1ZSIsImNyZWF0ZWQiOjE2NzgyNjU4MDExOTEsImV4aXN0aW5nIjp0cnVlfQ==',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Mar+08+2023+14%3A07%3A24+GMT%2B0500+(Yekaterinburg+Standard+Time)&version=6.19.0&isIABGlobal=false&hosts=&genVendors=V9%3A0%2C&consentId=856ff7e0-4429-44a0-b9a3-593eb514ee50&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2Cgad%3A0%2CSTACK42%3A0&geolocation=RU%3BUD&AwaitingReconsent=false',
        '_ga_V1KE40XCLR': 'GS1.1.1678265802.1.1.1678266444.58.0.0',
        'sbjs_session': 'pgs%3D38%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fciezarowe%2Fplandeka-firana%2F%3Fsearch%255Border%255D%3Dcreated_at%3Adesc%26search%255Bfilter_enum_mark%255D%255B0%255D%3Dvolvo%26search%255Bfilter_enum_mark%255D%255B1%255D%3Ddaf%26search%255Bfilter_float_axes%3Afrom%255D%3D4%26search%255Bfilter_float_price%3Ato%255D%3D150000%26search%255Bfilter_float_year%3Afrom%255D%3D2010',
        'session_start_date': '1678268369127',
        'onap': '186c06fd946x2803cc00-1-186c06fd946x2803cc00-137-1678268369',
    }
    headers = {
        'authority': 'www.olx.pl',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=o98rqdi86anlnc139romrl6mlo; mobile_default=desktop; fingerprint=MTI1NzY4MzI5MTs4OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTsxOzA7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MTsxOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MTswOzA7MDsxOzA7MDsxOzE7MDsxOzE7MTsxOzA7MTswOzEzMDE3NjU0OTk7MjsyOzI7MjsyOzI7NTsyODQ4MDA2NDE4OzEzNTcwNDE3Mzg7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MTswOzQxMDAyMTk5OzM0NjkzMDY1NTE7NjQyMzAyMDI2Ozc4NTI0NzAyOTsxMDA1MzAxMjAzOzE5MjA7MTA4MDsyNDsyNDszNjA7MzAwOzM2MDszMDA7MzYwOzMwMDszNjA7MzAwOzM2MDszNjA7MzYwOzM2MDszNjA7MzYwOzM2MDszMDA7MzAwOzMwMDszMDA7MzAwOzA7MDsw; dfp_user_id=e6bbe5ce-df27-4870-8ab4-836627ac9be4-ver2; laquesis=cars-33613@b#erm-1001@a#erm-1031@c#euads-3574@b#f8nrp-1502@b#jobs-4644@a#jobs-4672@b#jobs-4750@b#jobs-4757@a#jobs-4982@b#jobs-4989@b#jobs-5077@b#jobs-5103@b#jobs-5187@a#jobs-5188@a#oesx-2534@c#oesx-2597@b#olxeu-40264@a#olxeu-40383@b; laquesisff=a2b-000#aut-388#buy-2279#buy-2489#dat-2874#decision-256#do-2963#do-3418#euit-2250#euonb-114#euweb-1372#euweb-451#grw-124#kuna-307#kuna-554#kuna-603#mou-1052#oesx-1437#oesx-1643#oesx-645#oesx-867#olxeu-0000#psm-308#psm-402#psm-457#psm-574#sd-570#ser-87#srt-1289#srt-1346#srt-1434#srt-1593#srt-1758#srt-683#uacc-529; laquesissu=297@ad_page|1#297@reply_phone_1step|1; _hjFirstSeen=1; _hjSession_1685071=eyJpZCI6ImIzM2JmOTk4LWQ3NGMtNDhiMy04YmFjLWFhZjdkNmZmOGI0MyIsImNyZWF0ZWQiOjE2NzgyNjU4MDE3MTQsImluU2FtcGxlIjpmYWxzZX0=; from_detail=0; observed_aui=d9eb320e54cf435f8e31c4de80e722f8; _ga=GA1.1.435354839.1678265802; OptanonAlertBoxClosed=2023-03-08T08:56:44.539Z; eupubconsent-v2=CPoUwncPoUwncAcABBENC6CgAAAAAH_AAAYgJSNf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PEmnMbO2dYGH9_n1_z-ZKY7___f_7z_v-v________7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79_7_H9-QSbAJMNW4gC7EscCbaMIoEQIwrCQqgUAFFAMLRAYQOrgp2VwE-sIkACAUARgRAhwBRgwCAAACAJCIgJAjwQCAAiAQAAgAVCIQAEbAIKACwEAgAFANCxRigCECQgyICIpTAgIkSCgnsqEEoP9DTCEOssAKDR_xUICJQAhWBEJCwchwRICXiyQLMUb5ACMAKAUSoVqCT00AAAA.YAAAD_gAAAAA; OTAdditionalConsentString=1~89.2008.2072.2135.2322.2465.2501.2958.2999.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3300.3306.3307.3308.3314.3315.3316.3318.3324.3327.3328.3330.3531.3831.3931; deviceGUID=75af6303-19a3-490a-a326-14232f5fe2fe; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2023-03-08%2013%3A56%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fdostawcze%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.pl%2F; sbjs_first_add=fd%3D2023-03-08%2013%3A56%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fdostawcze%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.pl%2F; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.0.0%20Safari%2F537.36; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; newrelic_cdn_name=CF; a_access_token=2fad9a8fe838b9009d8f37eda1db1df2fd226e87; a_refresh_token=c8c84e50a180cd74ca6ea25b995e658f29745a60; a_grant_type=device; dfp_segment=%5B%5D; user_id=1477967603; user_business_status=private; lqstatus=1678267182|186c06fd946x2803cc00|euads-3574||; lister_lifecycle=1678265944; _hjSessionUser_1685071=eyJpZCI6IjhhZGFkZDRkLTdmY2QtNTA5Ny1hMWFmLWU1ZWE1N2QxYzU1ZSIsImNyZWF0ZWQiOjE2NzgyNjU4MDExOTEsImV4aXN0aW5nIjp0cnVlfQ==; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Mar+08+2023+14%3A07%3A24+GMT%2B0500+(Yekaterinburg+Standard+Time)&version=6.19.0&isIABGlobal=false&hosts=&genVendors=V9%3A0%2C&consentId=856ff7e0-4429-44a0-b9a3-593eb514ee50&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2Cgad%3A0%2CSTACK42%3A0&geolocation=RU%3BUD&AwaitingReconsent=false; _ga_V1KE40XCLR=GS1.1.1678265802.1.1.1678266444.58.0.0; sbjs_session=pgs%3D38%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.olx.pl%2Fmotoryzacja%2Fciezarowe%2Fplandeka-firana%2F%3Fsearch%255Border%255D%3Dcreated_at%3Adesc%26search%255Bfilter_enum_mark%255D%255B0%255D%3Dvolvo%26search%255Bfilter_enum_mark%255D%255B1%255D%3Ddaf%26search%255Bfilter_float_axes%3Afrom%255D%3D4%26search%255Bfilter_float_price%3Ato%255D%3D150000%26search%255Bfilter_float_year%3Afrom%255D%3D2010; session_start_date=1678268369127; onap=186c06fd946x2803cc00-1-186c06fd946x2803cc00-137-1678268369',
        'dnt': '1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.olx.pl/motoryzacja/ciezarowe/plandeka-firana/?search%5Border%5D=created_at:desc&search%5Bfilter_enum_mark%5D%5B0%5D=volvo&search%5Bfilter_enum_mark%5D%5B1%5D=daf&search%5Bfilter_float_axes:from%5D=4&search%5Bfilter_float_price:to%5D=150000&search%5Bfilter_float_year:from%5D=2010',
        cookies=cookies,
        headers=headers,
    )

    # with open('src.html', 'r', encoding='utf-8') as file:
    #     response = file.read()

    soup = BeautifulSoup(response.text, 'lxml')

    total_count = int(soup.find('div', {'data-testid': 'total-count'}).text.split(' ')[2])
    if total_count == 0:
        return []

    for card in soup.find_all('div', {'data-cy': 'l-card'}):
        if 'otomoto' not in card.find('a')['href']:
            link = 'https://www.olx.pl' + card.find('a')['href']
        else:
            link = card.find('a')['href']

        picture = card.find('img')['src'].split(';')[0]
        title = card.find('h6', {'class': 'css-16v5mdi'}).text
        price = card.find('p', {'class': 'css-10b0gli'}).contents[0]
        location = card.find('p', {'data-testid': 'location-date'}).text.split(' - ')[0]
        info = re.sub(' +', ' ', card.find('div', {'class': 'css-efx9z5'}).text)

        vehicles.append(Export(1, picture, link, title, price, info, location))

    return vehicles
