import json

from pprintjson import pprintjson as ppjson

from model.PrivatTask import PrivatTask


class JsonFormatTask(PrivatTask):
  def __init__(self, event, payload):
    super(JsonFormatTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": "```\n" + ppjson(self.payload) + "\n```"}
