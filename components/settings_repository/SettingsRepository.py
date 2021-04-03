import dbm
import json

from components.constant_service.ConsstantsService import ConstantsService


class SettingsRepository:

  def get_settings(self, user_name):
    with dbm.open(ConstantsService.get_value('db_path'), 'c') as db:
      return json.loads(db[user_name]) if user_name in db else json.loads(
          self.init_default_settings(
              db,
              user_name, "unknown player one"))

  def get_settings_and_init(self, user_name, display_name):
    with dbm.open(ConstantsService.get_value('db_path'), 'c') as db:
      return json.loads(db[user_name]) if user_name in db else json.loads(
          self.init_default_settings(
              db,
              user_name, display_name))

  def get_setting_value(self, user_name, key):
    settings = self.get_settings(user_name)
    return settings[key] if key in settings else None

  def set_settings(self, user_name, settings):
    with dbm.open(ConstantsService.get_value('db_path'), 'c') as db:
      db[user_name] = json.dumps(settings)

  def init_default_settings(self, db, user_name, display_name):
    with open(ConstantsService.get_value('default_settings_path')) as json_file:
      default_settings = json.loads(json_file.read())
      default_settings["display_name"] = display_name
      db[user_name] = json.dumps(default_settings)
      return default_settings
