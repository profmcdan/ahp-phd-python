from .library.parser import parse, validate_model

import json

with open('wiki_leader.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(model)
priorities = ahp_model.get_priorities()
print(priorities)


# print(get_user_attributes(ahp_model))
