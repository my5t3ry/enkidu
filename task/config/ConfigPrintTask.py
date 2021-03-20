import json

from task.PrivatTask import PrivatTask


class ConfigPrintTask(PrivatTask):
  user_config = None

  def __init__(self, event, payload):
    super(ConfigPrintTask, self).__init__(event, payload)
    self.user_config = event['user_config']

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": json.dumps(self.user_config)}
