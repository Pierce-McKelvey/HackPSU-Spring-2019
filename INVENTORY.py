# Team: Vijay Balaji, Jacob Ryan, Luke McCleery, Pierce McKelvey
# Inventory

class Inv:
    def __init__(self):
        self.ourInventory = {} # We are using a dictionary
        
    def __str__(self):
        return str(self.ourInventory)

    def add(self, thing, amount):
        if thing in self.ourInventory:
            self.ourInventory[thing] += amount
        else:
            self.ourInventory[thing] = amount

        return '{} {} ADDED'.format(amount, thing)

    def remove(self, thing, amountRemoved):  # We could either remove all or just one.

        if amountRemoved == self.ourInventory[thing]:
            del self.ourInventory[thing]
        else:
            self.ourInventory[thing] -= amountRemoved
        return '{} {} REMOVED'.format(amountRemoved, thing)




