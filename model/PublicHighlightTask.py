from model.HiglightTask import HighlightTask
from model.PublicTask import PublicTask


class PublicHighlightTask(HighlightTask, PublicTask):

  def __init__(self, event, payload):
    super(PublicHighlightTask, self).__init__(event, payload)

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
