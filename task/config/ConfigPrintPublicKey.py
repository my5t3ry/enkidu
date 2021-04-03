from components.constant_service.ConsstantsService import ConstantsService
from task.PrivatTask import PrivatTask


class ConfigPrintPublicKeyTask(PrivatTask):
  parseError = None
  user_name = None
  new_user_config = None

  def __init__(self, event, payload):
    super(ConfigPrintPublicKeyTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_message(self):
    with open(ConstantsService.get_value('public_key_file')) as public_key_file:
      return {
        "text": public_key_file.read()}
