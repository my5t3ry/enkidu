import hashlib


class Task(object):
  payload = None
  uuid = None

  def __init__(self, event, payload):
    self.uuid =  hashlib.sha1(event['user']['name'].encode("UTF-8")).hexdigest()[:10]

    self.payload = payload

  def get_description(self):
    return self.description
