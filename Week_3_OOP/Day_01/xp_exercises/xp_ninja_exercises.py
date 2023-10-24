# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. 

class Phone :
    
    def __init__(self, phone_number) :
        self.phone_number = phone_number
# When instantiating an object create an attribute called call_history which value is an empty list.
        self.call_history = []
# Add another attribute called messages to your __init__() method which value is an empty list.
        self.sent_messages = []
        self.received_messages = []

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. 
# The method should print a string stating who called who, and add this string to the phone’s call_history.
    def call(self, other_phone) :
        self.other_phone = other_phone
        print(f"{self.phone_number} called {self.other_phone}")
        self.call_history.append(f"{self.phone_number} called {self.other_phone}")

# Add a method called show_call_history. This method should print the call_history.
    def show_call_history(self) :
        print(self.call_history)

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content    
    def send_message(self, other_phone, content) :
        self.other_phone = other_phone
        self.content = content 
        self.message = dict()
        self.message["to"] = self.other_phone
        self.message["from"] = self.phone_number
        self.message["content"] = self.content
        self.sent_messages.append(self.message)

    def receive_message(self, other_phone, content) :
        self.other_phone = other_phone
        self.content = content 
        self.message = dict()
        self.message["to"] = self.phone_number
        self.message["from"] = self.other_phone
        self.message["content"] = self.content
        self.received_messages.append(self.message)

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
    def show_outgoing_messages(self) :
        print(self.sent_messages)
    
    def show_incoming_messages(self) :
        print(self.received_messages)
    
    def show_messages_from(self, other_phone) :
        self.other_phone = other_phone
        for element in self.received_messages :
            if element["from"] == self.other_phone :
                print(element) 


my_phone = Phone("055-1112233")
# my_phone.call("053-9998877")
# my_phone.call("054-8887766")
# my_phone.call("052-7776655")
# my_phone.show_call_history()

my_phone.send_message("053-9998877", "Hi, how are you?")
my_phone.receive_message("053-9998877", "I'll come late today!")
my_phone.send_message("054-8887766", "Hi, we have a meeting at 10.")
my_phone.receive_message("054-8887766", "Thanks for reminding me about the meeting!")
my_phone.send_message("053-9998877", "Where are you?")
my_phone.receive_message("053-9998877", "I'm stuck in a traffic jam...")
my_phone.send_message("052-7776655", "Please clean the litter box, it is stinking!")
my_phone.receive_message("052-7776655", "Yep. Will do.")

my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()
my_phone.show_messages_from("053-9998877")