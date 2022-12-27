from pydantic import BaseModel

class JsonIOModel(BaseModel):

    # make the model subscriptable
    def __getitem__(self, key):
        return self.dict()[key]

    # make the model item assignable
    def __setitem__(self, key, value):
        setattr(self, key, value)