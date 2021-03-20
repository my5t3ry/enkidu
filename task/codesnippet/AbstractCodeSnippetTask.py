from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.img import ImageFormatter
from pygments.lexers import guess_lexer
from pygments.styles import get_style_by_name

from components.constant_service.ConsstantsService import ConstantsService
from task.Task import Task


class AbstractCodeSnippetTask(Task):
  user_config = None
  html_url = None
  img_url = None

  def __init__(self, event, payload):
    super(AbstractCodeSnippetTask, self).__init__(event, payload)
    self.user_config = event['user_config']

  def run(self):
    global constants_service
    jpg_file_name = self.uuid + ".jpg"
    html_file_name = self.uuid + ".html"
    img_file_path = ConstantsService.get_value(
        'img_store') + "/" + jpg_file_name
    html_file_path = ConstantsService.get_value(
        'html_store') + "/" + html_file_name
    self.img_url = ConstantsService.get_value(
        'enkidu_url') + '/img/' + jpg_file_name
    self.html_url = ConstantsService.get_value(
        'enkidu_url') + '/html/' + html_file_name
    image_formater = ImageFormatter(
        style=get_style_by_name(self.user_config['theme']),
        font_size=self.user_config['image-fontsize'])
    html_formatter = HtmlFormatter(
        style=get_style_by_name(self.user_config['theme']))
    html_formatter.noclasses = True
    html_formatter.linenos = True
    lexer = guess_lexer(self.payload.encode())
    jpg_result = highlight(self.payload, lexer, image_formater)
    html_result = highlight(self.payload, lexer, html_formatter)
    open(img_file_path, 'wb').write(jpg_result)
    with open(html_file_path, "w") as f:
      f.write(html_result)

  def get_message(self):
    return {
      "cards": [
        {
          "sections": [
            {
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
                  },
                  "textParagraph": {
                    "text": self.html_url + "\n" + self.img_url
                  }
                }
              ]
            }
          ]
        }
      ]
    }
