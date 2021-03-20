from model.HiglightTask import HighlightTask
from model.PublicTask import PublicTask


class PublicHighlightTask(HighlightTask, PublicTask):

  def __init__(self, event):
    super(PublicHighlightTask, self).__init__(event)

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
