class ProductNotFoundException(Exception):
    def __init__(self):
        super().__init__('Product not found!')


class ProductAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__('Product already exists!')
