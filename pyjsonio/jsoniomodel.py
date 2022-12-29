
from pydantic import BaseModel
from pyjsonio.exceptions import AttributeNotFoundError


class JsonIOModel(BaseModel):

    '''
    Base class for all models used in this module.
    This class is a subclass of pydantic.BaseModel.
    '''



    def __getitem__(self, key):

        '''
        Returns the value of the attribute with the given key.
        
        :param key: the key of the attribute
        
        :return: the value of the attribute
        '''

        if not hasattr(self, key):
            return None
        else:
            return self.dict()[key]



    def __setitem__(self, key, value):

        '''
        Sets the value of the attribute with the given key.

        :param key: the key of the attribute
        :param value: the value of the attribute

        :return: None

        :raises AttributeNotFoundError: if the attribute does not exist
        '''

        if not hasattr(self, key):
            raise AttributeNotFoundError(key) from None
        else:
            setattr(self, key, value)