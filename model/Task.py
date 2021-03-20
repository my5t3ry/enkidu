import uuid


class Task(object):
  payload = None
  uuid = None
  target_space_name = None

  def __init__(self, payload):
    self.uuid = uuid.uuid4().hex
    self.payload = payload

  def get_target_space_name(self):
    return self.target_space_name

  def get_description(self):
    return self.description
