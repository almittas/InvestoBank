import unittest
import os.path
import sys
#importing the tested module which is one directory up in the file system.
myPath = os.path.dirname(os.path.realpath(__file__))
ind = myPath.find('unit_tests')
sys.path.append(myPath[0:ind])
import Client

class test_Client(unittest.TestCase):

  def test_transact(self):

      #Creating a Client 
      ClientA = Client.Client("ClientA")

      #Try to buy 10 digicoins at 15.645 
      ClientA.transact("BUY", 10)
      value = round(ClientA.transactions[0][0], 3)
      #check if bought on the expected price.
      self.assertEqual(value, 15.645)

      #Try to sell 80 digicoins at 124.64
      ClientA.transact("SELL", 80)
      value = round(ClientA.transactions[1][0], 3)
      #check if bought on the expected price.
      self.assertEqual(value, 124.64)
      #check if -80 has been inserted in the list of transactions in the second transcation.
      self.assertEqual(ClientA.transactions[1][1], -80)

      #Try to buy 130 digicoins at 201.975
      ClientA.transact("BUY", 130)
      value = round(ClientA.transactions[2][0], 3)
      #check if bought on the expected price.
      self.assertEqual(value, 201.975)

      # Try to trascact non multiple of 10 digicoins.
      try:
        ClientA.transact("BUY", 11)
      except Exception as inst:
        print "\nYou can only transact multiples of digicoins.\nTransaction of 11 digicoins Failed!"

  def test_net_position(self):
    #Create 3 Clients
    ClientA = Client.Client("ClientA")
    ClientB = Client.Client("ClientB")
    ClientC = Client.Client("ClientC")

    #make a few transactions for them.
    ClientA.transact("BUY", 10)
    ClientB.transact("BUY", 40)
    ClientA.transact("BUY", 50)
    ClientB.transact("BUY", 100)
    ClientB.transact("SELL", 80)
    ClientC.transact("SELL", 70)
    ClientA.transact("BUY", 130)
    ClientB.transact("SELL", 60)

    # check if the net positions of all 3 clients are the expexted.
    self.assertEqual(round(ClientA.net_position(),3), 296.156)
    self.assertEqual(round(ClientB.net_position(),3), 0)
    self.assertEqual(round(ClientC.net_position(),3), -109.06)

    #broker 1 should have transacted 80 digicoins whereas Broker 2 should havet transacted 460 digicoins.
    self.assertEqual(ClientA.Broker1.digicoins_transacted, 80)
    self.assertEqual(ClientA.Broker2.digicoins_transacted, 460)
    

if __name__ == '__main__':
    unittest.main()
