import logging
import uuid
from flask import Flask, request, json, send_from_directory, abort
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.img import JpgImageFormatter
from pygments.lexers import guess_lexer



from logging.config import dictConfig

dictConfig({
  'version': 1,
  'formatters': {'default': {
    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
  }},
  'handlers': {'wsgi': {
    'class': 'logging.StreamHandler',
    'stream': 'ext://sys.stdout',
    'formatter': 'default'
  }},
  'root': {
    'level': 'INFO',
    'handlers': ['wsgi']
  }
})



app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/chat.bot']
SERVICE_ACCOUNT_FILE = 'cred.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
chat = build('chat', 'v1', credentials=credentials)

img_store = '/root/img/'
html_store = '/root/html/'
tmp_dode = '/root/tmp/tmp.code'
enkidu_url = 'https://enkidu.dgm-it.de'


@app.route('/img/<path:filename>')
def image(filename):
  try:
    return send_from_directory('/root/img/', filename)
  except IOError:
    abort(404)


@app.route('/html/<path:filename>')
def html(filename):
  try:
    return send_from_directory('/root/html/', filename)
  except IOError:
    abort(404)


@app.route('/', methods=['POST'])
def home_post():
  event_data = request.get_json()
  logging.info("received event ['{}']".format(event_data))
  if event_data['type'] == 'REMOVED_FROM_SPACE':
    logging.info('Bot removed from  %s', event_data['space']['name'])
    return json.jsonify({})

  if event_data['type'] == 'MESSAGE':
    code = event_data['message']['text']
    send_async_response(code)

  # Return empty jsom respomse simce message already sent via REST API
  return json.jsonify({})


# [START async-response]


def send_async_response(code):
  html_url, img_url, lexer = generate_targets(code)
  spaces_list = chat.spaces().list().execute()
  chat.spaces().messages().create(
      parent=spaces_list['spaces'][0]['name'],
      body=build_card(html_url, img_url, lexer)).execute()


def generate_targets(code):
  cur_uuid = uuid.uuid4().hex
  jpg_file_name = cur_uuid + ".jpg"
  html_file_name = cur_uuid + ".html"
  img_file_path = img_store + "/" + jpg_file_name
  html_file_path = html_store + "/" + html_file_name
  img_url = enkidu_url + '/img/' + jpg_file_name
  html_url = enkidu_url + '/html/' + html_file_name
  jpg_formatter = JpgImageFormatter()
  html_formatter = HtmlFormatter()
  html_formatter.noclasses = True
  html_formatter.linenos = True
  lexer = guess_lexer(code)
  jpg_result = highlight(code, lexer, jpg_formatter)
  html_result = highlight(code, lexer, html_formatter)
  open(img_file_path, 'wb').write(jpg_result)
  with open(html_file_path, "w") as f:
    f.write(html_result)
  return html_url, img_url, lexer


def build_card(html_url, img_url, lexer):
  return {
    "cards": [
      {
        "header": {
          "title": "enkidu has some " + lexer.name.lower() + " for you",
          "imageUrl": "https://www.gstatic.com/images/icons/material/system/1x/face_black_24dp.png",
        },
        "sections": [
          {
            "widgets": [
              {
                "image": {
                  "imageUrl": img_url,
                  "onClick": {
                    "openLink": {
                      "url": html_url
                    }
                  }
                }
              }
            ]
          }
        ]
      }
    ]
  }


def format_response(event):
  event_type = event['type']

  text = ""
  sender_name = event['user']['displayName']

  if event_type == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
    text = 'Thanks for adding me to {}!'.format(event['space']['displayName'])

  elif event_type == 'ADDED_TO_SPACE' and event['space']['type'] == 'DM':
    text = 'Thanks for adding me to a DM, {}!'.format(sender_name)

  elif event_type == 'MESSAGE':
    text = 'Your message, {}: "{}"'.format(sender_name,
                                           event['message']['text'])

  response = {'text': text}

  if event_type == 'MESSAGE' and event['message']['thread'] is not None:
    thread_id = event['message']['thread']
    response['thread'] = thread_id

  return response


if __name__ == '__main__':
  app.run(host='10.29.85.74', port=80, debug=True)
