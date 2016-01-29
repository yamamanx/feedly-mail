#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime, timedelta
import time
import smtplib
from email.Utils import formatdate
from email.Header import Header
from email.MIMEText import MIMEText

ADDRESS = "SMTP Mail Address"
PASSWARD = "SMTP Password"
SMTP = "SMTP Server"
PORT = 587
to_addr = "TO MAIL ADDRESS"
to_ccs = ["CC MAIL ADDRESS1","CC MAIL ADDRESS2","CC MAIL ADDRESS3","CC MAIL ADDRESS4","CC MAIL ADDRESS5"]
WEATHERMAP_CITY = "CITY NAME"
WEATHERMAP_API_KEY = "API KEY"
FEEDLY_TOKEN = "TOKEN KEY" 
FEEDLY_USER_ID = "USER ID"

def create_message(from_addr, to_addr, subject, body, to_ccs, encoding):
    msg = MIMEText(body ,'plain', encoding)
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Cc"] = ",".join(to_ccs)
    msg["Date"] = formatdate()
    msg["Subject"] = Header(subject, encoding)
    return msg

def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP(SMTP, PORT)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(ADDRESS, PASSWARD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

def weather_string():
    response_weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + WEATHERMAP_CITY + "&appid=" + WEATHERMAP_API_KEY)
    weather_data = json.loads(response_weather.text)
    condition_code = weather_data["weather"][0]["id"]
    return condition_string(condition_code)

def condition_string(condition_code):
    return_str = "分かりません。"
    if condition_code == 200:
        return_str = "軽い雷雨です。"
    elif condition_code == 201:
        return_str = "雷雨です。"
    elif condition_code == 202:
        return_str = "激しい雷雨です。"
    elif condition_code == 211:
        return_str = "雷雨です。"
    elif condition_code == 212:
        return_str = "激しい雷です。"
    elif condition_code == 230:
        return_str = "超激しい雷です。"
    elif condition_code == 231:
        return_str = "霧雨と雷です。"
    elif condition_code == 232:
        return_str = "激しい霧雨と雷です。"
    elif condition_code == 300:
        return_str = "軽い霧雨です。"
    elif condition_code == 301:
        return_str = "霧雨です。"
    elif condition_code == 302:
        return_str = "激しい霧雨です。"
    elif condition_code == 310:
        return_str = "軽い霧と雨です。"
    elif condition_code == 311:
        return_str = "霧と雨です。"
    elif condition_code == 312:
        return_str = "激しい霧と雨です。"
    elif condition_code == 313:
        return_str = "霧雨と霧です。"
    elif condition_code == 314:
        return_str = "激しい霧雨と雨です。"
    elif condition_code == 321:
        return_str = "細かい霧雨です。"
    elif condition_code == 500:
        return_str = "軽い雨です。"
    elif condition_code == 501:
        return_str = "雨です。"
    elif condition_code == 502:
        return_str = "激しい雨です。"
    elif condition_code == 503:
        return_str = "超激しい雨です。"
    elif condition_code == 504:
        return_str = "ウルトラ激しい雨です。"
    elif condition_code == 511:
        return_str = "冷たい雨です。"
    elif condition_code == 520:
        return_str = "軽いシャワーのような雨です。"
    elif condition_code == 531:
        return_str = "超シャワーの雨です。"
    elif condition_code == 600:
        return_str = "軽い雪です。"
    elif condition_code == 601:
        return_str = "雪です。"
    elif condition_code == 602:
        return_str = "激しい雪です。"
    elif condition_code == 611:
        return_str = "みぞれです。"
    elif condition_code == 612:
        return_str = "細かいみぞれです。"
    elif condition_code == 615:
        return_str = "軽い雨と雪です。"
    elif condition_code == 616:
        return_str = "雨と雪です。"
    elif condition_code == 620:
        return_str = "軽く細かい雪です。"
    elif condition_code == 621:
        return_str = "細かい雪です。"
    elif condition_code == 622:
        return_str = "激しく細かい雪です。"
    elif condition_code == 701:
        return_str = "霧状です。"
    elif condition_code == 711:
        return_str = "煙っていますね。"
    elif condition_code == 721:
        return_str = "ヘイズです。"
    elif condition_code == 731:
        return_str = "砂埃です。"
    elif condition_code == 741:
        return_str = "濃霧です。"
    elif condition_code == 751:
        return_str = "砂です。"
    elif condition_code == 761:
        return_str = "埃です。"
    elif condition_code == 771:
        return_str = "スコールです。"
    elif condition_code == 781:
        return_str = "竜巻です。"
    elif condition_code == 800:
        return_str = "快晴です。"
    elif condition_code == 801:
        return_str = "晴れです。"
    elif condition_code == 802:
        return_str = "ところどころ曇りです。"
    elif condition_code == 803:
        return_str = "やや曇りです。"
    elif condition_code == 804:
        return_str = "曇りです。"
    elif condition_code == 900:
        return_str = "竜巻です。"
    elif condition_code == 901:
        return_str = "鮮やかな雲です。"
    elif condition_code == 902:
        return_str = "ハリケーンです。"
    elif condition_code == 903:
        return_str = "寒いです。"
    elif condition_code == 904:
        return_str = "暑いです。"
    elif condition_code == 905:
        return_str = "風がありますね。"
    elif condition_code == 906:
        return_str = "ひょうです。"
    elif condition_code == 951:
        return_str = "穏やかです。"
    elif condition_code == 952:
        return_str = "軽い風です。"
    elif condition_code == 953:
        return_str = "そよ風です。"
    elif condition_code == 954:
        return_str = "風です。"
    elif condition_code == 955:
        return_str = "さわやかな風です。"
    elif condition_code == 956:
        return_str = "強い風です。"
    elif condition_code == 956:
        return_str = "早い強風です。"
    elif condition_code == 958:
        return_str = "強風です。"
    elif condition_code == 959:
        return_str = "かなりの強風です。"
    elif condition_code == 960:
        return_str = "嵐です。"
    elif condition_code == 961:
        return_str = "バイオレンスな嵐です。"
    elif condition_code == 962:
        return_str = "ハリケーンです。"
    return "今の天気は" + return_str



def lambda_handler(event, context):
    try:
        now = datetime.now()
        subject = "ここ1週間の気になった記事です - " + now.strftime("%Y/%m/%d")
        body = "皆様\nおはようございます。xxです。\n\n" + weather_string() + "\n\n1週間以内の気になった記事を共有します。\n\n通勤中や寝る前などお暇な時にぜひどうぞ。\n新着記事から順に上に表示しています。\n\n"

        last_week_time=now-timedelta(7)
        unix_time = int(time.mktime(last_week_time.timetuple()))*1000

        headers = {'Authorization': FEEDLY_TOKEN}

        response_stream = requests.get('https://cloud.feedly.com/v3/streams/contents?streamId=user/' + FEEDLY_USER_ID + '/tag/global.saved&count=100&newerThan=' + str(unix_time), headers=headers)
        stream_data = json.loads(response_stream.text)

        stream_data_array=stream_data["items"]
        for stream in stream_data_array:
            tag_string=""
            tag_div=""
            for tag in stream["tags"]:
                if tag["label"] != "" and tag["label"] != "global.read":
                    tag_string = tag_string + tag_div + "[" + tag["label"] + "]"
                    tag_div = ","
            body = body + tag_string + "\n" + stream["title"] + "\n" + stream["alternate"][0]["href"] + "\n\n"

        msg = create_message(ADDRESS, to_addr, subject, body, to_ccs, 'utf-8')
        send(ADDRESS, [to_addr], msg)

    except Exception as e:
       print(e)
       raise e
