class Broker:
    def __init__(self, rate, commission):
        """Constructor. Creates a new Broker.
        Keyword arguments:
        rate -- The rate that the broker is offering.
	commission -- Percentage of commission charged for this transaction.
        """
        self.rate = rate
	self.commission = commission
        #initially every Broker has transact 0 digicoins
        self.digicoins_transacted = 0

    def commission_calculation(self, digicoins_No):
       """Calculated the commission for digicoins_No transaction according to Broker's policy.
       Keyword arguments:
       digicoins_No -- The number of digicoins some client wants to transact.
       returns -- commission to be charged for this transaction.
       """
       for commission_category in self.commission:
	   left_bound = commission_category[0]
	   right_bound = commission_category[1]
	   if digicoins_No >= left_bound and digicoins_No <= right_bound:
	      return commission_category[2]

    def execute_transaction(self, digicoins_transacted):
        """Updates and keeps information of the transacted digicoins so far. Performs the transaction.
        Keyword arguments:
        digicoins_transacted -- The number of digicoins some client wants to transact.
        """
        #Transaction being processed.
        self.digicoins_transacted += digicoins_transacted

    def offered_price(self, digicoins_No):
	"""Calculates the price the broker is offering for a transaction of digicoins_No digicoins
        Keyword arguments:
        digicoins_No -- The number of digicoins some client wants to transact.
        returns -- The price offered by the Broker
        """
	offered_commission = self.commission_calculation(digicoins_No)
	return digicoins_No * self.rate * (1 + offered_commission)
