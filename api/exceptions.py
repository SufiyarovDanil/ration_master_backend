class UserNotFoundException(Exception):
    def __init__(self):
        super().__init__('User not found!')


class UserAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__('User already exists!')


class ProductNotFoundException(Exception):
    def __init__(self):
        super().__init__('Product not found!')


class ProductAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__('Product already exists!')
