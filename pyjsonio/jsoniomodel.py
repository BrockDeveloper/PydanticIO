from pydantic import BaseModel

class JsonIOModel(BaseModel):

    def __getitem__(self, key):

        if not hasattr(self, key):
            return None
        else:
            return self.dict()[key]


    def __setitem__(self, key, value):

        if not hasattr(self, key):
            raise AttributeError(f"Model {self.__class__.__name__} has no attribute {key}")
        else:
            setattr(self, key, value)