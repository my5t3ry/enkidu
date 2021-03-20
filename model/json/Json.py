from model.json.JsonFormatTask import JsonFormatTask
from model.json.JsonValidateTask import JsonValidateTask

json_registry = {
  '-v': JsonValidateTask,
  '-f': JsonFormatTask,
}
