import random
import io

''' Text messaging APP:
Make a Template Class
    Good morning subclass
    Good night subclass
    Happy birthday subclass
    Good luck subclass
    Inspirational subclass
Make a Contact Class
    Individual Message - Contact subclass
    
'''


class Contact(object):
    def __init__(self, contact_name: str, contact_phonenum: int, relation: str)
    
        
class Template(Contact):
'''
Default templates would be: Good Morning, Good Night, Good Luck, Happy Birthday
'''
    def __init__(self, template_name: str, greetings: List, send_to_names: List, day_adjectives:List, locations: List, closing_statements: List, emoji_choices: List,cdate_of_message: int, time_of_message: Array):
        self.template_name = template_name
        self.greetings = greetings
        self.send_to_names = send_to_namesc# Note to user: include desired punctuation after name. ex) Good night mom! vs Good night mom. 
        self.day_adjectives = day_adjectives
        self.locations = locations # Note to user: include desired punctuation after location. ex) at ...work! vs at ...work. 
        self.closing_statements = closing_statements
        self.emoji_choices = emoji_choices
        self.date_of_message = date_of_message
        self.time_of_message = time_of_message:
        self.template_name = template_name
        
    def randomize_choices(self):
        greeting = random.choice(self.greetings)
        day_adj = random.choice(self.day_adjectives) 
        location = random.choice(self.locations)
        closing_statement = random.choice(self.closing_statements)
        emoji_choice = random.choice(self.emoji_choices)
        
    def format_message(self):
        structure = greeting + send_to_name + day_adj + ", at " + location ", " + closing_statement + ", " + emoji
        return structure
        
    def preview_message(self):
        approval_process = False
        while (approval_process = False):
            self.randomize_choices()
            self.format_message()
            print(structure)
            approval_process = input("Are you happy with this preview message: ") # This will be True or False
            return approval_process
            
contact_file = open('contact.txt','a') 
greeting_file = open('greetings.txt', 'a')
day_adj_file = open('day_adjectives.txt', 'a')
location_file = open('location.txt','a')
closing_file = open('closing_statements.txt', 'a')

while (contact_file != 'x'):
    contact_file.write(input("Contact name: ")) #Will eventually pull from contacts list
    
while (greeting_file != 'x'):
    greeting_file.write(input("Greeting: ")) #Create list of greetings
    
while (day_adj_file != 'x'):
    day_adj_file.write(input("Day adjective: ")) #Create list of day adjectives
    
while (location_file != 'x'):
    location_file.write(input("Location: ")) #Create list of locations
    
while (closing_file != 'x'):
    closing_file.write(input("Closing statement: ")) #Create list of closing statements

contact_1 = Contact()
contact_1.contact_name = "Matt"
contact_1.contact_phonenum = 5417515727
contact_1.relation = "boyfriend"

contact_file.close()
greeting_file.close()
day_adj_file.close()
location_file.close()
closing_file.close()
