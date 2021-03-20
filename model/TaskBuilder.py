import re

from model.PrivateHighlightTask import PrivateHighlightTask
from model.PublicHighlightTask import PublicHighlightTask
from model.arithmetic.Arithmetic import arithmetic_registry
from model.config.Config import config_registry
from model.json.Json import json_registry
from model.str.Str import str_registry

task_registry = {'/me': {'default': PrivateHighlightTask},
                 '/public': {'default': PublicHighlightTask},
                 '/str': str_registry,
                 '/json': json_registry,
                 '/arit': arithmetic_registry,
                 '/config': config_registry,
                 'default': PrivateHighlightTask,
                 }

p = re.compile('([^\s]+)')


class TaskBuilder:
  @staticmethod
  def build_task(event):
    return TaskBuilder.match_command(task_registry,
                                     event, event['message']['text'])

  @staticmethod
  def match_command(registry, event, cmd):
    match = p.search(cmd)
    if len(match.groups()) > 0 and match.groups()[0] in registry and type(
        registry[match.groups()[0]]) is dict:
      return TaskBuilder.match_command(registry[match.groups()[0]], event,
                                       cmd.replace(match.groups()[0] + ' ', ""))
    else:
      return registry[match.groups()[0]](event,
                                         TaskBuilder.strip_slash_command(
                                             registry, cmd)
                                         ) if match.groups()[0] in registry else \
        registry["default"](event,
                            TaskBuilder.strip_slash_command(registry, cmd)
                            )

  @staticmethod
  def strip_slash_command(registry, cmd):
    result = cmd
    for cur_slash_command in registry.keys():
      result = result.replace(cur_slash_command + ' ', '')
    return result
