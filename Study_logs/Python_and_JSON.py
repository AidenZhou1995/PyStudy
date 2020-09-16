"""Translating JSON string to JSON

JSON string ---> loads ---> python object ---> dumps ---> JSON

"""

import json

jsonData = '{"a":1,"b":{"b1":2},"f":3,"d":4,"e":5,"hello":[1]}'

text = json.loads(jsonData)
txt = json.dumps(text, sort_keys=True, indent=2)
print(txt)