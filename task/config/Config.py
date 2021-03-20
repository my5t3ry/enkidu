from task.config.ConfigEditTask import ConfigEditTask
from task.config.ConfigPrintTask import ConfigPrintTask

config_registry = {
  '-e': ConfigEditTask,
  'default': ConfigPrintTask,
}
