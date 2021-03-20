from model.Task import Task


class PrivatTask(Task):

  def __init__(self, event):
    super(PrivatTask, self).__init__(event, event['space']['name'])

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
