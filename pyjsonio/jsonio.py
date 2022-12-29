
import json
from pyjsonio.exceptions import *
from pyjsonio.jsoniomodel import JsonIOModel


class JsonIO:

    '''
    JsonIO class
    
    This module is used to read and write json files with pydantic models.
    '''



    def __init__(self, json_file: str, model: JsonIOModel, key: str = None) -> None:

        '''
        JsonIO class constructor
        
        :param json_file: json file path
        :param model: pydantic model
        :param key: key to sort the list (optional)
        
        :return: None
        
        :raises ModelClassError: if model is not a subclass of JsonIOModel
        :raises FileError: if json_file is not a valid file
        :raises FileItemMatchError: if json_file items don't match model
        :raises KeyError: if key is not a key in the model
        '''

        self.model = None
        self.file = None
        self.items = []
        self.key = None

        if not issubclass(model, JsonIOModel):
            raise ModelClassError() from None

        try:
            with open(json_file, "r") as f:
                f.close()
        except:
            raise FileError(json_file) from None

        self.model = model
        self.file = json_file

        with open(json_file, "r") as f:
            if f.read(1) == "":
                _dict = []
            else:
                f.seek(0)
                _dict = json.load(f)
            f.close()
            
        try:
            self.items = [self.model(**element) for element in _dict]
        except:
            raise FileItemMatchError(json_file) from None
        
        del _dict

        if key is not None:
            if key not in self.model.__fields__: 
                raise KeyError(key, self.model) from None

        self.key = key


    
    def write(self, json_file: str = None) -> None:

        '''
        Write the list to a json file

        :param json_file: json file path (optional)

        :return: None

        :raises FileWriteError: if json_file can't be written
        '''

        if json_file is None:
            json_file = self.file

        try:
            with open(json_file, "w") as f:
                json.dump([element.dict() for element in self.items], f, indent=4)
                f.close()
        except:
            raise FileWriteError(json_file) from None



    def sort(self) -> None:

        '''
        Sort the list by key
        
        :return: None
        
        :raises Exception: if key is not set
        '''

        if self.key is None:
            raise Exception("key not set") from None
        self.items.sort(key=lambda x: x[self.key])



    def dict(self) -> list:

        '''
        Return the list as a list of dictionaries
        
        :return: list of dictionaries
        '''

        return [element.dict() for element in self.items]



    def append(self, item: JsonIOModel) -> None:

        '''
        Append an item to the list
        
        :param item: item to append
        
        :return: None
        
        :raises ItemMatchError: if item doesn't match model
        '''

        if not issubclass(item, self.model):
            raise ItemMatchError() from None

        try:
            self.items.append(item)
        except:
            raise ItemMatchError() from None



    def remove(self, item: JsonIOModel) -> None:

        '''
        Remove an item from the list
        
        :param item: item to remove
        
        :return: None
        '''

        if item in self.items:
            self.items.remove(item)
    


    def remove(self, key) -> None:

        '''
        Remove an item from the list
        
        :param key: key of the item to remove
        
        :return: None
        
        :raises KeyError: if key is not set
        '''

        if self.key is None:
            raise KeyError() from None
        for i in range(len(self.items)):
            if self.items[i][self.key] == key:
                del self.items[i]
                break



    def __getitem__(self, key):

        '''
        Get an item from the list

        :param key: key of the item to get

        :return: item

        :raises KeyError: if key is not set
        :raises ItemNotFoundError: if item is not found
        '''

        if self.key is None:
            raise KeyError() from None
        else:
            for i in range(len(self.items)):
                if self.items[i][self.key] == key:
                    return self.items[i]

            raise ItemNotFoundError() from None 



    def __iter__(self):

        '''
        Iterate over the list

        :return: iterator
        '''

        return iter(self.items)


    
    def __len__(self):

        '''
        Get the length of the list

        :return: length of the list
        '''

        return len(self.items)



    def __str__(self):

        '''
        Get the string representation of the list

        :return: string representation of the list
        '''
        
        return str(self.items)