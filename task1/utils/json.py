import json


class JsonParsable:
    def json(self):
        raise NotImplementedError()

    def json_str(self):
        return json.loads(self.json())