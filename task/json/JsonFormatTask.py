import jsbeautifier

from task.PrivatTask import PrivatTask


class JsonFormatTask(PrivatTask):
  def __init__(self, event, payload):
    super(JsonFormatTask, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    return {
      "text": "```\n" + jsbeautifier.beautify(self.payload, opts)+ "\n```"}
