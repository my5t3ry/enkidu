from task.PublicTask import PublicTask
from task.codesnippet.AbstractCodeSnippetTask import AbstractCodeSnippetTask


class PublicCodeSnippetTask(AbstractCodeSnippetTask, PublicTask):

  def __init__(self, event, payload):
    super(PublicCodeSnippetTask, self).__init__(event, payload)

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
