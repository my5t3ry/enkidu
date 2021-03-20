from model.config.ConfigEditTask import ConfigEditTask
from model.config.ConfigPrintTask import ConfigPrintTask

config_registry = {
  '-e': ConfigEditTask,
  'default': ConfigPrintTask,
}
