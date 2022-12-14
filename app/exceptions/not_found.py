class NotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class UserNotFoundException(NotFoundException):
    def __init__(self, user=None):
        self.resource = "User"
        self.resource_id = user


class TransactionNotFoundException(NotFoundException):
    def __init__(self, transaction=None):
        self.resource = "Transaction"
        self.resource_id = transaction
