class Party:
    def __init__(self):
        self.people = []


party = Party()
command = input()
while command != "End":
    party.people.append(command)

    command = input()
