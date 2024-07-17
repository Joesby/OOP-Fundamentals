#create a class for Events with variables for names and dates
class Event:
    def __init__(self, name, date, num_pars):
        self.name = name
        self.date = date
        self.num_participants = num_pars
    
    #add a method for adding participants
    def add_participant(self):
        self.num_participants += 1

    #add a method for getting the number of participants
    def get_participant_count(self):
        return self.num_participants
    
#create an object for an Event with its own name, date, and number of participants
party = Event("Office Party", "7-3-24", 3)

#display the current number of participants
print(party.num_participants)

#run a loop for adding more participants
for i in range(10):
    party.add_participant()

#display the new number of participants
print(party.num_participants)