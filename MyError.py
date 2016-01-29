class MyError(Exception):
    def __init__(self, value):
        """Constructor. Creates a MyError object. Such an object is being created
        when the number of digicoins to be transacted are not a multiple of 10.
        Keyword arguments:
        value -- The non valid value representing the number of digicoins that the client tried to transact.
        """
        self.value = value
    def __str__(self):
        return repr(self.value)

