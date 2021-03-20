from task.PrivatTask import PrivatTask
from task.codesnippet.AbstractCodeSnippetTask import AbstractCodeSnippetTask


class PrivateCodeSnippetTask(AbstractCodeSnippetTask, PrivatTask):

  def __init__(self, event, payload):
    super(PrivateCodeSnippetTask, self).__init__(event, payload)

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
