import time

class ParkingGarage():

    def __init__(self):
        self.tickets = [0] * 50
        self.parkingSpaces = [False] * 50
        self.paidFor = [False] * 50
        self.currentTicket = {'paid' : False, 'index' : 0}
        self.pricePerSecond = .01

    def takeTicket(self):
        for i in range(len(self.parkingSpaces)):
            if not self.parkingSpaces[i]:
                self.currentTicket['index'] = i
                self.tickets[self.currentTicket['index']] = time.time()
                self.parkingSpaces[self.currentTicket['index']] = True
                print(f"Ticket number: {self.currentTicket['index']}")
                break
            elif i == 49:
                print("No more available spaces!")

    def payForParking(self):
        if self.parkingSpaces[self.currentTicket['index']]:
            if not self.currentTicket['paid']:
                try:
                    cost = (time.time() - self.tickets[self.currentTicket['index']]) * self.pricePerSecond
                    payment = float(input(f"please pay %.2f " % cost))
                    if (payment + .01) <= cost:
                        print("insufficient funds!")
                        self.payForParking()
                    else:
                        self.currentTicket['paid'] = True
                        self.paidFor[self.currentTicket['index']] = True
                        print(f"you have 15 minutes to leave")
                except:
                    print("Please enter a valid response")
                    self.payForParking()
            else:
                print("Ticket already payed!")
        else:
            print("No current ticket!")


    def leaveGarage(self):
        if self.parkingSpaces[self.currentTicket['index']]:
            if self.currentTicket['paid']:
                print("Thank You, have a nice day")
                self.parkingSpaces[self.currentTicket['index']] = False
                self.paidFor[self.currentTicket['index']] = False
                self.currentTicket['index'] = 0
                for i in range(len(self.parkingSpaces)):
                    if self.parkingSpaces[i]:
                        self.currentTicket['index'] = i
                        self.currentTicket['paid'] = self.paidFor[self.currentTicket['index']]
                        print(f"Ticket number: {self.currentTicket['index']}")
                        break
            else:
                print("Please pay for your ticket")
                self.payForParking()
        else:
            print("No current ticket!")

    def selectTicket(self):
        try:
            ticketNumber = int(input("select ticket number "))
            if (self.parkingSpaces[ticketNumber]):
                self.currentTicket['index'] = ticketNumber
                self.currentTicket['paid'] = self.paidFor[self.currentTicket['index']]
            else:
                print("Ticket is not yet taken")
        except:
            print("Please enter a valid response")
            self.selectTicket()
        

parking_garage = ParkingGarage()

while True:
    print("Welcome to the parking garage, what would you like to do?")
    try:
        action = int(input("[1] Take ticket\n[2] Pay for parking\n[3] Leave garage\n[4] Select ticket\n"))
        if action == 1:
            parking_garage.takeTicket()
        elif action == 2:
            parking_garage.payForParking()
        elif action == 3:
            parking_garage.leaveGarage()
        elif action == 4:
            parking_garage.selectTicket()
    except:
        print("Please enter a valid response")
