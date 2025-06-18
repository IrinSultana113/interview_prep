# Polymorphism refers to the ability of different object types to respond 
# to the same method name in their own way. 

# Base notification class with a send() method
class notification:
    def send(self, message):
        print("Welcome to our services")

# Child class that sends email notifications
class email_notification:
    def send(self, message):
        print("Welcome to our services in Email")

# Child class that sends SMS notifications
class sms_notification:
    def send(self, message):
        print("Welcome to our services in SMS")

# Function that takes any object with a 'send' method and calls it
def start_notification(sender):
    sender.send("Welcome to our service!")  


# Create instances (objects) of each notification type
Notification = notification()
Email = email_notification()
SMS = sms_notification()


# Polymorphic behavior: same function works with different object types
start_notification(Notification)
start_notification(Email)
start_notification(SMS)
