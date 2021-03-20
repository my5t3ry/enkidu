from components.constant_service.ConsstantsService import ConstantsService
from task.PrivatTask import PrivatTask


class Help(PrivatTask):

  def __init__(self, event, payload):
    super(Help, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": "```\n" + open(ConstantsService.get_value("help_file"),
                             'r').read() + "\n```"}
