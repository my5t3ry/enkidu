from task.json.JsonFormatTask import JsonFormatTask
from task.json.JsonValidateTask import JsonValidateTask

json_registry = {
  '-v': JsonValidateTask,
  '-f': JsonFormatTask,
}
