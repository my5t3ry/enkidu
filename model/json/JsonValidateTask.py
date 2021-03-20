from jsonschema import Draft7Validator

from model.PrivatTask import PrivatTask


class JsonValidateTask(PrivatTask):
  validation_result = ""

  def __init__(self, event, payload):
    super(JsonValidateTask, self).__init__(event, payload)

  def run(self):
    schema = {
      "items": {
        "anyOf": [
          {"type": "string", "maxLength": 2},
          {"type": "integer", "minimum": 5}
        ]
      }
    }
    instance = [{}, 3, "foo"]
    v = Draft7Validator(schema)
    errors = sorted(v.iter_errors(instance), key=lambda e: e.path)
    for error in errors:
      for suberror in sorted(error.context, key=lambda e: e.schema_path):
        self.validation_result = self.validation_result + \
                                 str(suberror.schema_path[0]) + ':' + \
                                 str(suberror.schema_path[
                                       1]) + ' -> ' + suberror.message + '\n'

  def get_data(self):
    print(f'{self.real}+{self.imag}j')

  def get_message(self):
    response = self.validation_result if len(
      self.validation_result) > 0 else "json is valide"
    return {
      "text": "```\n" + self.validation_result + "\n```"}
