class DataSet:
    def __init__(self):
        raise NotImplementedError('abstract class')

    def sample(self):
        raise NotImplementedError('abstract class')

    def next(self):
        raise NotImplementedError('abstract class')
