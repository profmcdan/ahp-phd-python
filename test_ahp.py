from library.parser import parse, validate_model

import json

with open('sample.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(model)
priorities = ahp_model.get_priorities()
print(priorities)
