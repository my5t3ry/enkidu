from task.Task import Task


class AsyncTask(Task):
  finished = False
  msg = None

  def __init__(self, event, payload):
    super(AsyncTask, self).__init__(event, payload)
    self.async_task = True

  def set_message(self, msg):
    self.message = {
      "text": msg}

  def get_target_space_name(self):
    return self.target_space_name

  def is_finished(self):
    return self.finished
