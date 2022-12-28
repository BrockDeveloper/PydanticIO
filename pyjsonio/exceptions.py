


class Exception(Exception):

    '''
    Base class for all exceptions in this module.
    '''

    def __init__(self):
        super().__init__("Exception: generic exception occurred")



class ModelClassError(Exception):

    '''
    Exception raised when the model is not a valid model class.
    '''

    def __init__(self):
        super().__init__("Exception: model must be a JsonIOModel")



class FileError(Exception):

    '''
    Exception raised when the file is not found.
    '''

    def __init__(self, file_name):
        super().__init__("Exception: file not found: " + file_name)



class FileItemMatchError(Exception):

    '''
    Exception raised when an item in the file does not match the model.
    '''

    def __init__(self, file_name):
        super().__init__("Exception: an item in the file" + file_name + " does not match model")



class ItemMatchError(Exception):

    '''
    Exception raised when an item does not match the model.
    '''

    def __init__(self):
        super().__init__("Exception: item does not match model")



class KeyError(Exception):

    '''
    Exception raised when the key is not a field in the model.
    '''

    def __init__(self, key, model):
        super().__init__("Exception: key " + key + " must be a field in the model")



class FileWriteError(Exception):

    '''
    Exception raised when the file could not be written.
    '''

    def __init__(self, file_name):
        super().__init__("Exception: file " + file_name + " could not be written")



class ItemNotFoundError(Exception):

    '''
    Exception raised when the item is not found in the item list.
    '''

    def __init__(self):
        super().__init__("Exception: item not found")