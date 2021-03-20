import re

from model.ConfigTask import ConfigTask
from model.PrivateHighlightTask import PrivateHighlightTask
from model.PublicHighlightTask import PublicHighlightTask

task_registry = {'/me': PrivateHighlightTask,
                 '/public': PublicHighlightTask,
                 '/config': ConfigTask,
                 }

p = re.compile('([^\s]+)')


class TaskBuilder:

  @staticmethod
  def build_task(event):
    match = p.search(event['message']['text'])[0]
    event['message']['text'] = TaskBuilder.strip_slash_command(event)
    return task_registry[match](
        event) if match in task_registry else PrivateHighlightTask(
        event)

  @staticmethod
  def strip_slash_command(event):
    result = event['message']['text']
    for cur_slash_command in task_registry.keys():
      result = result.replace(cur_slash_command, '')
    return result
