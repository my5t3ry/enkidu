from task.config.ConfigEditTask import ConfigEditTask
from task.config.ConfigListOutputFormats import ConfigListOutputFormats
from task.config.ConfigListStyles import ConfigListStyles

from task.config.ConfigPrintPublicKey import ConfigPrintPublicKeyTask
from task.config.ConfigPrintTask import ConfigPrintTask

config_registry = {
  '-e': ConfigEditTask,
  '--list-styles': ConfigListStyles,
  '--list-formats': ConfigListOutputFormats,
  '--print-public-key': ConfigPrintPublicKeyTask,
  'default': ConfigPrintTask,
}
