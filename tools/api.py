from data.apiConfig import INPUT_FUNCTION, OUTPUT_FUNCTION


class Api(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ApiSettings()
        return cls.instance


class ApiSettings:
    def __init__(self):
        self.input = INPUT_FUNCTION
        self.output = OUTPUT_FUNCTION

        self.input = self.input if self.input is not None else input
        self.output = self.output if self.output is not None else print
