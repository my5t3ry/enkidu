import json

from pygments.styles import get_all_styles

from task.PrivatTask import PrivatTask


class ConfigListStyles(PrivatTask):

  def __init__(self, event, payload):
    super(ConfigListStyles, self).__init__(event, payload)

  def run(self):
    pass

  def get_message(self):
    return {
      "text": json.dumps(list(get_all_styles())).join(", ")}
