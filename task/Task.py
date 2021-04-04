
import shortuuid


class Task(object):
  payload = None
  uuid = None
  async_task = False

  def __init__(self, event, payload):
    self.uuid = shortuuid.ShortUUID().random(length=8)
    self.payload = payload

  def get_description(self):
    return self.description

  def is_async_task(self):
    return self.async_task
