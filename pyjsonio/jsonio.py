import json
from pydantic import BaseModel



class JsonIO:



    def __init__(self, json_file: str, model: BaseModel = None) -> None:

        '''
        Initialize the JsonIO class
        
        :param json_file: The json file to read from
        :param model: The pydantic model to use for validation
        
        :return: None
        '''

        self.model = model
        self.switch = False
        self.file = json_file

        with open(json_file, "r") as f:
            self._dict = json.load(f)
            f.close()



    def validate(self) -> bool:

        '''
        Validate the json file with the pydantic model
        
        :return: True if the json file is valid, False if not
        '''

        for element in self._dict:
            try:
                self.model(**element)
            except:
                return False

        return True



    def read(self, json_file: str) -> None:

        '''
        Read a json file
        
        :param json_file: The json file to read from
        
        :return: None
        '''

        with open(json_file, "r") as f:
            self.file = json_file
            self._dict = json.load(f)
            f.close()



    def write(self, json_file: str = None) -> None:

        '''
        Write the json file
        
        :param json_file: The json file to write to, if None the file from the constructor is used
        
        :return: None
        '''

        if json_file is None:
            json_file = self.file

        with open(json_file, "w") as f:
            json.dump(self._dict, f, indent=4)
            f.close()



    def dict(self) -> dict:

        '''
        Get the json file as a dict

        :return: The json file as a dict
        '''

        return self._dict

    
    def json(self) -> str:

        '''
        Get the json file as a string

        :return: The json file as a string
        '''

        return json.dumps(self._dict)



    def pydantic(self) -> list:

        '''
        Get the json file as a list of pydantic objects

        :return: The json file as a list of pydantic objects
        '''

        return [self.model(**element) for element in self._dict]


    
    def __len__(self) -> int:

        '''
        Get the length of the json file

        :return: The length of the json file
        '''

        return len(self._dict)

    

    def switch_to_pydantic(self, switch: bool) -> None:

        '''
        Switch between dict and pydantic objects

        :param switch: True to switch to pydantic objects, False to switch to dicts

        :return: None
        '''

        self.switch = switch



    def __getitem__(self, key: int) -> dict:
        
        '''
        Get an item from the json file

        :param key: The key of the item to get

        :return: The item as a dict or pydantic object
        '''

        if self.switch:
            return self.model(**self._dict[key])
        else:
            return self._dict[key]

    

    def __str__(self) -> str:

        '''
        Get the json file as a string

        :return: The json file as a string
        '''

        return self.json()

     
    def __del__(self) -> None:

        '''
        Delete the object

        :return: None
        '''
        
        del self