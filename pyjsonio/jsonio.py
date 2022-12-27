import json


class JsonIO:


    def __init__(self, json_file: str) -> None:
        
        with open(json_file, "r") as f:
            self._dict = json.load(f)
            f.close()


    def dict(self) -> dict:
        return self._dict

    
    def json(self) -> str:
        return json.dumps(self._dict)

    
    def __getitem__(self, key: int) -> dict:
        return self._dict[key]