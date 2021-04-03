from task.net.NetWhoisTask import NetWhoisTask, NetPingTask

net_registry = {
  '--whois': NetWhoisTask,
  '--ping': NetPingTask,
}
