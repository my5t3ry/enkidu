#!/usr/bin/python3 -u
import logging
import uuid
from logging.config import dictConfig

from flask import Flask, request, json, send_from_directory, abort
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.img import JpgImageFormatter
from pygments.lexers import guess_lexer
from pygments.styles import get_all_styles, get_style_by_name

from model.PrivateHighlightTask import PrivateHighlightTask
from model.taskfactory import build_task

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
img_store = '/root/img/'
html_store = '/root/html/'
tmp_dode = '/root/tmp/tmp.code'
enkidu_url = 'https://enkidu.dgm-it.de'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
chat = build('chat', 'v1', credentials=credentials)


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


def resolve_target(event_data, cur_task, cur_spaces_ctx):
  if isinstance(cur_task, PrivateHighlightTask):
    return event_data['space']['name']
  else:
    for cur_space in cur_spaces_ctx:
      if cur_task.target_display_name.lower() in cur_space[
        'displayName'].lower():
        return cur_space['name']


@app.route('/', methods=['POST'])
def home_post():
  event_data = request.get_json()
  cur_spaces_ctx = chat.spaces().list().execute()['spaces']
  logging.info("Current bot spaces ['%s']", json.dumps(cur_spaces_ctx))
  cur_task = build_task(event_data)
  logging.info("received event ['%s']", event_data)
  target_space = resolve_target(event_data, cur_task, cur_spaces_ctx)
  logging.info("Resolved target space ['%s']", target_space)
  card = build_targets(cur_task)

  chat.spaces().messages().create(
      parent=target_space,
      body=card).execute()

  return json.jsonify({})


def generate_moc():
  return "", "", ""


def build_targets(cur_task):
  html_url, img_url, lexer = generate_targets(cur_task.code)
  return generate_card(html_url, img_url, lexer)


def generate_targets(code):
  cur_uuid = uuid.uuid4().hex
  jpg_file_name = cur_uuid + ".jpg"
  html_file_name = cur_uuid + ".html"
  img_file_path = img_store + "/" + jpg_file_name
  html_file_path = html_store + "/" + html_file_name
  img_url = enkidu_url + '/img/' + jpg_file_name
  html_url = enkidu_url + '/html/' + html_file_name
  jpg_formatter = JpgImageFormatter(style=get_style_by_name('solarized-light'))
  html_formatter = HtmlFormatter(style=get_style_by_name('solarized-light'))
  html_formatter.noclasses = True
  html_formatter.linenos = True
  lexer = guess_lexer(code.encode())
  jpg_result = highlight(code, lexer, jpg_formatter)
  html_result = highlight(code, lexer, html_formatter)
  open(img_file_path, 'wb').write(jpg_result)
  with open(html_file_path, "w") as f:
    f.write(html_result)
  return html_url, img_url, lexer


def generate_card(html_url, img_url, lexer):
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


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
