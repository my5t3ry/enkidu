from model.PrivateHighlightTask import PrivateHighlightTask
from model.PublicHighlightTask import PublicHighlightTask


def build_task(event):
  if "slashCommand" in event['message']:
    return PrivateHighlightTask(strip_slash_command(event)) if \
      event['message']['annotations'][0]['slashCommand'][
        'commandName'] == '/me' else PublicHighlightTask(
        strip_slash_command(event))
  else:
    return PrivateHighlightTask(
        event['message'])


def strip_slash_command(event):
  return event['message']['text'].replace(
      event['message']['annotations'][0]['slashCommand'][
        'commandName'] + ' ', '')
