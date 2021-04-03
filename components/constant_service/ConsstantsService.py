import os
from os.path import expanduser


class ConstantsService:
  const = {
    "home": expanduser("~"),
    "dist_store": os.path.join(expanduser("~"), '.enkidu/assets/dist'),
    "enkidu_url": 'https://enkidu.dgm-it.de',
    "db_path": os.path.join(expanduser("~"), '.enkidu/db'),
    "help_file": os.path.join(expanduser("~"), '.enkidu/help.txt'),
    "scopes": ['https://www.googleapis.com/auth/chat.bot'],
    "default_settings_path": os.path.join(expanduser("~"),
                                          '.enkidu/defaultsettings.json'),
    "credentials": os.path.join(expanduser("~"),
                                '.enkidu/cred.json')
  }

  @staticmethod
  def get_value(key):
    return ConstantsService.const[
      key] if key in ConstantsService.const else None

  def get_constant(self):
    print(f'{self.real}+{self.imag}j')
