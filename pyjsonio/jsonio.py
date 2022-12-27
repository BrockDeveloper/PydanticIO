import json


class JsonIO:


    def __init__(self, json_file: str) -> None:
        
        self.file = json_file

        with open(json_file, "r") as f:
            self._dict = json.load(f)
            f.close()


    def read(self, json_file: str) -> None:
        with open(json_file, "r") as f:
            self.file = json_file
            self._dict = json.load(f)
            f.close()


    def write(self, json_file: str = None) -> None:
        if json_file is None:
            json_file = self.file
        with open(json_file, "w") as f:
            json.dump(self._dict, f, indent=4)
            f.close()



    def dict(self) -> dict:
        return self._dict

    
    def json(self) -> str:
        return json.dumps(self._dict)

    
    def __getitem__(self, key: int) -> dict:
        return self._dict[key]

    
    def __str__(self) -> str:
        return self.json()

     
    def __del__(self) -> None:
        del self