class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}:" \
               f" {self.content}. Sent: {self.is_sent}"

emails = []
indexes = []
while True:
    data = input().split()
    if data[0] == "Stop":
        break
    sender, receiver, content = data
    email = Email(sender, receiver, content)
    emails.append(email)

indexes = [int(x) for x in input().split(", ")]

for idx in indexes:
    if 0 <= idx <= len(emails):
        emails[idx].send()

for email in emails:
    print(email.get_info())