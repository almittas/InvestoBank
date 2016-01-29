import Broker
import MyError

class Client():
    
    #All clients need to access the same Brokers. Therefore two Brokers are defined as static objects here. 
    Broker1 = Broker.Broker(1.49, [[10, 100, 0.05]])
    Broker2 = Broker.Broker(1.52, [[10, 40, 0.03], [50, 80, 0.025], [90, 100, 0.02]])
    
    def __init__(self, name):
        """Constructor. Creates a new Client.
        Keyword arguments:
        name -- ID of the client
        """

        #This list holds the details of every transaction of the client. It contains pairs of the value paid for digicoins and the number of them.
        #eg. [[15.645, 10], [77.9, 50]].  The list is getting extended with a new pair when a transation completes.
        self.transactions = []
        self.name = name
     
    def transact(self, transaction_type, digicoins_No):
        """Transacts digicoins_No digicoins. Checks whether Broker1 or Broker2 is providing the best choise and proceeds with the transactions accordingly.
        Transactions can be slpit to different Brokers. Once a transaction is done updates the list that holds clients net position information.
        If the number of digicoins to be transacted are not a multiple of 10 a MyError type Exception is being raised.
        Keyword arguments:
        transaction_type -- whether is a sell or buy transaction
        digicoins_No -- Number of digicoins to be transacted
        """

        #Raise an exception of digicoins_No is not multiple of 10.
        try:
            if digicoins_No % 10 != 0:
                raise MyError.MyError(digicoins_No)
        except Exception as inst:
            print "\nYou can only transact multiples of 10 of digicoins.\nTransaction Failed!"
            return

        lowest_price = 0
        digicoins_remain = digicoins_No
        while digicoins_remain > 0:
            if digicoins_remain > 100:
                digicoins_No_to_be_transacted = 100
            else:
                digicoins_No_to_be_transacted = digicoins_remain

            A_price = self.Broker1.offered_price(digicoins_No_to_be_transacted)
            B_price = self.Broker2.offered_price(digicoins_No_to_be_transacted)

            if A_price < B_price:
                self.Broker1.execute_transaction(digicoins_No_to_be_transacted)
                lowest_price += A_price
            else:
                self.Broker2.execute_transaction(digicoins_No_to_be_transacted)
                lowest_price += B_price
            digicoins_remain -= 100

        if transaction_type == "BUY":
            print self.name, "buys", digicoins_No_to_be_transacted, "at", lowest_price
            #update the clients list with a pair [price, digicoins]
            self.transactions.append([lowest_price, digicoins_No])
        else:
            print self.name, "sells", digicoins_No_to_be_transacted, "at", lowest_price
            self.transactions.append([lowest_price, -digicoins_No])
        
    def net_position(self):
        """Calculates the client's net position by calculating the average price of all transactions and multiplying that by the sum of all orders.
        returns -- The client's net position
        """
        average_price = 0
        sum = 0
        for transaction in self.transactions:
            average_price += abs(transaction[0]/transaction[1])
            sum += transaction[1]

        average_price /= len(self.transactions)  
        average_price *= sum
    
        return average_price
