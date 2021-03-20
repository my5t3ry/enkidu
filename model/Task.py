import uuid


class Task(object):
  code = None
  user_name = None
  uuid = None
  target_space_name = None

  def __init__(self, event, target_space_name):
    self.target_space_name = target_space_name
    self.uuid = uuid.uuid4().hex
    self.code = event['message']['text']
    self.user_name = event['user']['name']

  def get_target_space_name(self):
    return self.target_space_name
