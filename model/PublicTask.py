import re

from model.Task import Task


class PublicTask(Task):

  def __init__(self, event):
    p = re.compile('([^\s]+)')
    match = p.search(event['message']['text'])
    target_display_name = match.groups()[0]
    event['message']['text'] = event['message']['text'].replace(
        ' ' + target_display_name + ' ', "")
    super(PublicTask, self).__init__(event, self.find_target_space_name(
        target_display_name, event['spaces_ctx']))

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def find_target_space_name(self, target_display_name, spaces_ctx):
    for cur_space in spaces_ctx:
      if target_display_name.lower() in cur_space[
        'displayName'].lower():
        return cur_space['name']
