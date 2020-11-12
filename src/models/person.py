class Person:
  def __init__(self, params):
    self.name = params.get('name')
    self.birth_date = params.get('birth_date')

  def params_str(self):
    return "{{name: '{}', birth_date: '{}'}}".format(self.name, self.birth_date)
