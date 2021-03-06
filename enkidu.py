#!/usr/bin/python3 -u
import asyncio
import logging
from logging.config import dictConfig

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, json, send_from_directory, abort
from google.oauth2 import service_account
from googleapiclient.discovery import build

from components.constant_service.ConsstantsService import ConstantsService
from components.settings_repository.SettingsRepository import SettingsRepository
from task.TaskBuilder import TaskBuilder

settings_repository = SettingsRepository()

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

credentials = service_account.Credentials.from_service_account_file(
    ConstantsService.get_value('credentials'),
    scopes=ConstantsService.get_value('scopes'))
chat = build('chat', 'v1', credentials=credentials)

async_task_stack = []


def checkAsyncTasks():
  for cur_task in async_task_stack:
    if cur_task.is_finished():
      chat.spaces().messages().create(
          parent=cur_task.get_target_space_name(),
          body=cur_task.get_message()).execute()
      async_task_stack.remove(cur_task)


# sched = BackgroundScheduler(daemon=True)
# sched.add_job(checkAsyncTasks, 'interval', seconds=10)
# sched.start()

@app.route('/dist/<path:filename>')
def dist(filename):
  global constants_service
  try:
    return send_from_directory(ConstantsService.get_value('dist_store'),
                               filename)
  except IOError:
    abort(404)


@app.route('/', methods=['POST'])
def home_post():
  event_data = request.get_json()
  logging.info("current event ['%s']", json.dumps(event_data))

  cur_spaces_ctx = chat.spaces().list().execute()['spaces']
  event_data['spaces_ctx'] = cur_spaces_ctx
  event_data['user_config'] = settings_repository.get_settings_and_init(
      event_data['user']['name'], event_data['user']['displayName'])
  logging.info("Current bot spaces ['%s']", json.dumps(cur_spaces_ctx))
  cur_task = TaskBuilder.build_task(event_data)
  # logging.debug("current event ['%s']", json.dumps(cur_task))
  # if cur_task.is_async_task:
  #   task = asyncio.run(cur_task.run())
  #   async_task_stack.append(cur_task)
  #   chat.spaces().messages().create(
  #       parent=cur_task.get_target_space_name(),
  #       body=cur_task.get_message()).execute()
  #   return json.jsonify({})
  # else:
  cur_task.run()
  try:
    message = cur_task.get_message()
  except Exception as e:
    message = {"text": "```\n" + "Command failed -> [{}]".format(e) + "\n```"}

  result = chat.spaces().messages().create(
      parent=cur_task.get_target_space_name(),
      body=message).execute()

  logging.info("message result ['%s']", json.dumps(result))

  return json.jsonify({})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4343, debug=True)
