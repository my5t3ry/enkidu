class PrivateHighlightTask:
  code = None

  def __init__(self, code):
    self.code=code

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
