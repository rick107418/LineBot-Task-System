from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import json

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

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

    reply_text = "你好，我是派工系統Bot，請問您需要什麼服務？"
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=reply_text)
        FlexSendMessage(
            alt_text='任務派送卡片',
            contents=flex_content
        )
    )
    


if __name__ == "__main__":
    app.run()