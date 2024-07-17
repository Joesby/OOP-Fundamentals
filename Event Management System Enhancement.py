#create a class for Events with variables for names and dates
class Event:
    def __init__(self, name, date, num_pars):
        self.name = name
        self.date = date
        self.num_participants = num_pars

    def add_participant(self):
        self.num_participants += 1

    def get_participant_count(self):
        return self.num_participants
    
party = Event("Office Party", "7-3-24", 3)

print(party.num_participants)

for i in range(10):
    party.add_participant()

print(party.num_participants)