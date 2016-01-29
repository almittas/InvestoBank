import Client

if __name__ == '__main__':
        ClientA = Client.Client("ClientA")
        ClientB = Client.Client("ClientB")
        ClientC = Client.Client("ClientC")
        ClientA.transact("BUY", 10)
        ClientB.transact("BUY", 40)
        ClientA.transact("BUY", 50)
        ClientB.transact("BUY", 100)
        ClientB.transact("SELL", 80)
        ClientC.transact("SELL", 70)
        ClientA.transact("BUY", 130)
        ClientB.transact("SELL", 60)
        print "ClientA", ClientA.net_position(), "ClientB", ClientB.net_position(), "ClientC", ClientC.net_position()
        print "Broker1", ClientA.Broker1.digicoins_transacted, "Broker2", ClientB.Broker2.digicoins_transacted
