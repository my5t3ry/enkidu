import subprocess

from task.PrivatTask import PrivatTask


class NetPingTask(PrivatTask):

  def __init__(self, event, payload):
    super(NetPingTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_message(self):
    result = subprocess.check_output(
        "ping -c 5 " + self.payload, shell=True)
    return {
      "text": "```\n" + result.decode("utf-8") + "\n```"}
