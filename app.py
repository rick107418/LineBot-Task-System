from flask import Flask, request, abort , send_file, make_response
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FlexSendMessage
# TextSendMessage,
import os, json , time, requests



app = Flask(__name__, static_folder='static')

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route('/static/images/Todo.jpg')
def serve_image():
    response = make_response(send_file("static/images/Todo.jpg"))
    response.headers['Content-Type'] = 'image/jpeg'
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
    with open('static/json/reply_message.json', 'r', encoding='utf-8') as f:
        flex_content = json.load(f)

    #reply_text = "你好，我是派工系統Bot，請問您需要什麼服務？"
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=reply_text)
        FlexSendMessage(
            alt_text='任務派送卡片',
            contents=flex_content
        )
    )
    
# def get_image_url(base_url):
#     version = int(time.time())  # 或你自己定義版本號，比如 build number
#     return f"{base_url}?v={version}"

# 使用範例
# base_url = "https://yourdomain.com/static/images/Todo.jpg"
# image_url_with_version = get_image_url(base_url)

if __name__ == "__main__":
    app.run()