from model.HiglightTask import HighlightTask
from model.PrivatTask import PrivatTask


class PrivateHighlightTask(HighlightTask, PrivatTask):

  def __init__(self, event, payload):
    super(PrivateHighlightTask, self).__init__(event, "")

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
