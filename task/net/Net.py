from task.net.NetPingTask import NetPingTask
from task.net.NetWhoisTask import NetWhoisTask

net_registry = {
  '--whois': NetWhoisTask,
  '--ping': NetPingTask,
  'default': NetPingTask,
}
