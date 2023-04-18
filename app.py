#SDK(Software Development Kit)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('4L/cjeK9Ls7NpTj2PucFd4MLm0DfHn1N5IYgSzWG56IDYa7sbvxRu7GgSGBw46X+BorCfsW+qXmn4y7dsYFr16XGvA+Lq5z8/XiXEIiHK2/QrAUA1Hed+K+PTvxfVtW27CHVvpAzWsWdpAT9bu0hgAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('00d3fade906a2828983468560e855f22')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()