from pygments.formatters import get_all_formatters

from task.PrivatTask import PrivatTask


class ConfigListOutputFormats(PrivatTask):

  def __init__(self, event, payload):
    super(ConfigListOutputFormats, self).__init__(event, payload)

  def run(self):
    pass

  def get_message(self):
    result = ""
    for cur_formater in get_all_formatters():
      result = result + ("".join(cur_formater.filenames))
    return {
      "text": json.dumps(result.replace("*", ", *"))}
