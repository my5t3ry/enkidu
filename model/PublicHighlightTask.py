import re

class PublicHighlightTask:
  target_display_name = None
  code = None

  def __init__(self, code):
    p = re.compile('([^\s]+)')
    match = p.search(code)
    self.target_display_name = match.groups()[0]
    self.code = code.replace(self.target_display_name+' ', '')

  def get_data(self):
    print(f'{self.real}+{self.imag}j')
