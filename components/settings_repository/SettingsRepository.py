import dbm
import json

from components.constant_service.ConsstantsService import ConstantsService


class SettingsRepository:

  def get_settings(self, user_name):
    with dbm.open(ConstantsService.get_value('db_path'), 'c') as db:
      return json.loads(db[user_name]) if user_name in db else json.loads(
          self.init_default_settings(
              db,
              user_name))

  def get_setting_value(self, user_name, key):
    settings = self.get_settings(user_name)
    return settings[key] if key in settings else None

  def set_settings(self, user_name, settings):
    with dbm.open(ConstantsService.get_value('db_path'), 'c') as db:
      db[user_name] = json.dumps(settings)

  def init_default_settings(self, db, user_name):
    with open(ConstantsService.get_value('default_settings_path')) as json_file:
      default_settings_json = json_file.read()
      db[user_name] = default_settings_json
      return default_settings_json




