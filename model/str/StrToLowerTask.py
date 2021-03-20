import json

from model.PrivatTask import PrivatTask


class StrToLowerTask(PrivatTask):

  def __init__(self, event, payload):
    super(StrToUpperTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": json.dumps("```\n"+self.payload.lower()+"\n```")}
