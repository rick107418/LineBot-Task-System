from flask import Flask, request, abort , send_file, make_response
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, FlexMessage, FlexContainer
# TextSendMessage,
import os, json , time, requests



app = Flask(__name__, static_folder='static')

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route('/static/images/Todo.jpg')
def serve_image():
    response = make_response(send_file("static/images/Todo.jpg"))
    response.headers['Content-Type'] = 'image/jpg'
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#     with open('static/json/reply_message.json', 'r', encoding='utf-8') as f:
#         flex_content = json.load(f)

    # reply_text = "你好，我是派工系統Bot，請問您需要什麼服務？"
    line_flex_json={
                        "type": "flex",
                        "altText": "任務派送卡片",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://linebot-task-system.onrender.com/static/images/Todo.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [{
                                    "type": "text",
                                    "text": "請協助設定IP",
                                    "weight": "bold",
                                    "size": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "margin": "md",
                                    "contents": [{
                                        "type": "icon",
                                        "size": "sm",
                                        "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                    },
                                    {
                                        "type": "icon",
                                        "size": "sm",
                                        "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                    },
                                    {
                                        "type": "icon",
                                        "size": "sm",
                                        "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                    },
                                    {
                                        "type": "icon",
                                        "size": "sm",
                                        "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                                    },
                                    {
                                        "type": "icon",
                                        "size": "sm",
                                        "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
                                    },
                                    {
                                        "type": "text",
                                        "text": "緊急程度",
                                        "size": "sm",
                                        "color": "#999999",
                                        "margin": "md",
                                        "flex": 0
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "時間",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 4
                                        },
                                        {
                                            "type": "text",
                                            "text": "10:00 - 10:30",
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 13
                                        }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "地點",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 4
                                        },
                                        {
                                            "type": "text",
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 13,
                                            "text": "第一辦公大樓1樓行政收發室"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "詳細資訊",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 4
                                        },
                                        {
                                            "type": "text",
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "text": "請協助黃祥銘先生設定上網資訊，分機 2686",
                                            "margin": "md",
                                            "flex": 14
                                        }
                                        ]
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [{
                                    "type": "button",
                                    "style": "primary",
                                    "height": "sm",
                                    "action": {
                                    "type": "postback",
                                    "label": "接受",
                                    "data": "Accept"
                                    },
                                    "margin": "none",
                                    "position": "relative",
                                    "scaling": True,
                                    "flex": 5
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                    "type": "postback",
                                    "label": "拒絕",
                                    "data": "Not Accept"
                                    },
                                    "margin": "md",
                                    "position": "relative",
                                    "scaling": True,
                                    "flex": 5
                                }],
                                "flex": 0,
                                "margin": "sm",
                                "cornerRadius": "none"
                            }
                            }
                    }
    line_flex_str= json.dumps(line_flex_json)
    line_bot_api.reply_message(
        #TextSendMessage(text=reply_text)
        event.reply_token,
        message=[FlexMessage(alt_text='任務派送卡片',contents=FlexContainer.from_json(line_flex_str))]
        #flex_content
    )
    
# def get_image_url(base_url):
#     version = int(time.time())  # 或你自己定義版本號，比如 build number
#     return f"{base_url}?v={version}"

# 使用範例
# base_url = "https://yourdomain.com/static/images/Todo.jpg"
# image_url_with_version = get_image_url(base_url)

if __name__ == "__main__":
    app.run()