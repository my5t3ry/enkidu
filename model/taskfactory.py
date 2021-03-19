from model.PrivateHighlightTask import PrivateHighlightTask
from model.PublicHighlightTask import PublicHighlightTask

slash_commands = ['/me ', '/public ']


def build_task(event):
  if "slashCommand" in event['message']:
    return PrivateHighlightTask(strip_slash_command(event)) if \
      event['message']['annotations'][0]['slashCommand'][
        'commandName'] == '/me' else PublicHighlightTask(
        strip_slash_command(event))
  else:
    return PrivateHighlightTask(
        strip_slash_command(event))


def strip_slash_command(event):
  result = event['message']['text']
  for cur_slash_command in slash_commands:
    result = result.replace(cur_slash_command, '')
  return result
