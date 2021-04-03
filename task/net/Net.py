from task.net.NetPingTask import NetPingTask
from task.net.NetScanTask import NetScanTask
from task.net.NetWhoisTask import NetWhoisTask

net_registry = {
  '--whois': NetWhoisTask,
  '--ping': NetPingTask,
  '--scan': NetScanTask,
  'default': NetPingTask,
}
