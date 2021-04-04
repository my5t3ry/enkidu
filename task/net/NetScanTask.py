import subprocess

from task.PrivatTask import PrivatTask


class NetScanTask(PrivatTask):

  def __init__(self, event, payload):
    super(NetScanTask, self).__init__(event, payload)

  def run(self):
    return {
      "text": "scanning for active ips @ ['{}'] this can take a while ...".format(self.payload)}
    pass

  def get_message(self):
    result = subprocess.check_output(
        "nmap -v -sn " + self.payload, shell=True)
    return {
      "text": "```\n" + result.decode("utf-8") + "\n```"}
