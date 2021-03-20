import shortuuid

from task.PrivatTask import PrivatTask


class StrRndTask(PrivatTask):

  def __init__(self, event, payload):
    super(StrRndTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": "```\n" + shortuuid.ShortUUID().random(length=16) + "\n```"}
