from pygments import highlight
from pygments.formatters import get_formatter_for_filename
from pygments.lexers import guess_lexer
from pygments.styles import get_style_by_name

from components.constant_service.ConsstantsService import ConstantsService
from task.Task import Task


class AbstractCodeSnippetTask(Task):
  user_config = None
  html_url = None
  img_url = None

  urls = []

  def __init__(self, event, payload):
    super(AbstractCodeSnippetTask, self).__init__(event, payload)
    self.user_config = event['user_config']

  def run(self):
    global constants_service

    for cur_format in self.user_config['codesnippet-formats']:
      file_name = self.uuid + "." + cur_format
      file_path = ConstantsService.get_value(
          'dist_store') + "/" + file_name
      file_url = ConstantsService.get_value(
          'enkidu_url') + '/dist/' + file_name
      formatter = get_formatter_for_filename(file_name,
                                             style=get_style_by_name(
                                                 self.user_config['theme']),
                                             font_size=self.user_config[
                                               'image-fontsize'])
      if "jpg" in file_name or "gif" in file_name:
        self.img_url = file_url

      formatter.noclasses = True
      formatter.linenos = "inline"
      lexer = guess_lexer(self.payload.encode())
      result = highlight(self.payload, lexer, formatter)
      open(file_path, 'wb').write(
          str.encode(result) if type(result) is str else result)
      self.urls.append(file_url)

  def get_message(self):
    links = ""
    for url in self.urls:
      links = links + "<a href=" + url + ">" + url + "</a>\n"
    link_widget = {
      "widgets": [
        {
          "textParagraph": {
            "text": links
          }
        }
      ]
    }

    if self.img_url != None:
      return {
        "cards": [
          {
            "sections": [{
              "widgets": [
                {
                  "image": {
                    "imageUrl": self.img_url,
                    "aspectRatio": 3,
                    "onClick": {
                      "openLink": {
                        "url": self.html_url
                      }
                    }
                  }
                }
              ]},
              link_widget
            ]
          }
        ]
      }
    else:
      return {
        "cards": [
          {
            "sections": [
              link_widget
            ]
          }
        ]
      }
