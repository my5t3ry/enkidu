import uuid


class Task(object):
  payload = None
  uuid = None

  def __init__(self, event, payload):
    self.uuid = uuid.uuid4().hex
    self.payload = payload

  def get_description(self):
    return self.description
