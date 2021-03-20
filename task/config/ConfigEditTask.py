import json

from components.settings_repository.SettingsRepository import SettingsRepository
from task.PrivatTask import PrivatTask


class ConfigEditTask(PrivatTask):
  parseError = None
  user_name = None
  new_user_config = None

  def __init__(self, event, payload):
    super(ConfigEditTask, self).__init__(event, payload)
    self.user_name = event['user']['name']

    try:
      self.new_user_config = json.loads(payload)
    except Exception as e:
      self.parseError = {
        "save failed": "could not parse json [{}] exception [{}]".format(
            payload, e)}

  def run(self):
    if self.parseError == None:
      settings_reposiory = SettingsRepository()
      settings_reposiory.set_settings(self.user_name, self.new_user_config)
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    response = {
      "save success": self.new_user_config} if self.parseError == None else self.parseError
    return {
      "text": json.dumps(response)}
