from simpleeval import simple_eval

from task.PrivatTask import PrivatTask


class ArithmeticEval(PrivatTask):

  def __init__(self, event, payload):
    super(ArithmeticEval, self).__init__(event, payload)

  def run(self):
    pass

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    return {
      "text": "```\n" + str(simple_eval(self.payload)) + "\n```"}
