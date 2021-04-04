import asyncio

from task.AsyncTask import AsyncTask
from task.PrivatTask import PrivatTask


class NetScanTask(PrivatTask, AsyncTask):

  def __init__(self, event, payload):
    super(NetScanTask, self).__init__(event, payload)

  async def run(self):
    self.set_message(
        "scanning for active ips @ ['{}'] this can take a while ...".format(
            self.payload))
    proc = await asyncio.create_subprocess_shell(
        "nmap -sn " + self.payload,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    self.finished = True
    self.set_message(stdout.decode())
    pass

  def get_message(self):
    return self.message
