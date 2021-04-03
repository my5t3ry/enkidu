import json

import jsbeautifier
import whois

from task.PrivatTask import PrivatTask


class NetWhoisTask(PrivatTask):

  def __init__(self, event, payload):
    super(NetWhoisTask, self).__init__(event, payload)

  def run(self):
    self.domain = whois.query(self.payload)
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    return {
      "text": "```\n" + jsbeautifier.beautify(str(self.domain.__dict__),
                                              opts) + "\n```"}
