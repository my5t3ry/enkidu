from model.Task import Task


class PrivatTask(Task):

  def __init__(self, event, payload):
    super(PrivatTask, self).__init__(event, payload)
    self.target_space_name = event['space']['name']

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_target_space_name(self):
    return self.target_space_name
