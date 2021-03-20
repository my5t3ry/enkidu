from requests.utils import quote
from task.PrivatTask import PrivatTask


class StrUrlEncodeTask(PrivatTask):

  def __init__(self, event, payload):
    super(StrUrlEncodeTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": "```\n" +  quote(self.payload, safe='') + "\n```"}
