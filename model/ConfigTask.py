import json

from model.PrivatTask import PrivatTask


class ConfigTask(PrivatTask):
  user_config = None

  def __init__(self, event):
    super(ConfigTask, self).__init__(event)
    self.user_config = event['user_config']

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "cards": [
        {
          "sections": [
            {
              "widgets": [
                {
                  "text": json.dump(self.user_config)
                }
              ]
            }
          ]
        }
      ]
    }
