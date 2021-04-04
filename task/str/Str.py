from task.str.StUrlEncode import StrUrlEncodeTask
from task.str.StrRndTask import StrRndTask
from task.str.StrToLowerTask import StrToLowerTask
from task.str.StrToUpper import StrToUpperTask

str_registry = {
  '-tl': StrToLowerTask,
  '-tu': StrToUpperTask,
  '-url': StrUrlEncodeTask,
  '-rnd': StrRndTask,
  'default': StrRndTask,
}
