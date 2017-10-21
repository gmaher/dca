import tensorflow as tf

class Model:
    def __init__(self):
        raise NotImplementedError('abstract class')

    def predict(self):
        raise NotImplementedError('abstract class')
