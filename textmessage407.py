import random

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
    
        
class Template(object):
    def __init__(self, template_name: str):
        self.template_name = template_name
        
    def randomize_choices(self):
        greeting = random.choice(self.greetings)
        send_to_name = random.choice(send_to_names)
        day_adj = random.choice(self.day_adjectives) 
        location = random.choice(self.locations)
        closing_statement = random.choice((self.closing_statements)
        emoji_choice = random.choice(self.emoji_choices)
        
        def format_message(self):
        structure = "%(greeting) %(name) %(adj) at %(location) %(closing_statement) %(emoji)" 
            % {'greeting': greeting, 'send_to_name': send_to_name, 'day_adj': day_adj, 'location':                  location, 'closing_statement': closing_statement, 'emoji_choice': emoji_choice)
        return structure
        
    def preview_message(self):
        approval_process = False
        while approval_process = False:
            self.randomize_choices()
            self.format_message()
            print(structure)
            approval_process = input("Are you happy with this preview message: ") # This will be True or False
            return approval_process
            
        
class Good_Morning(Template):
    def __init__(self, greetings: List, send_to_names: List, day_adjectives:List, locations: List, closing_statements: List, emoji_choices: List, date_of_message: int, time_of_message: Array):
        super().__init__()
        self.template_name = template_name
        self.greetings = greetings
        self.send_to_names = send_to_namesc# Note to user: include desired punctuation after name. ex) Good morning mom! vs Good morning mom. 
        self.day_adjectives = day_adjectives
        self.locations = locations # Note to user: include desired punctuation after location. ex) at ...work! vs at ...work. 
        self.closing_statements = closing_statements
        self.emoji_choices = emoji_choices
        self.date_of_message = date_of_message
        self.time_of_message = time_of_message
        
class Good_Night(Template):
    def __init__(self, greetings: List, send_to_names: List, day_adjectives:List, locations: List, closing_statements: List, emoji_choices: List,cdate_of_message: int, time_of_message: Array):
        super().__init__()
        self.template_name = template_name
        self.greetings = greetings
        self.send_to_names = send_to_namesc# Note to user: include desired punctuation after name. ex) Good night mom! vs Good night mom. 
        self.day_adjectives = day_adjectives
        self.locations = locations # Note to user: include desired punctuation after location. ex) at ...work! vs at ...work. 
        self.closing_statements = closing_statements
        self.emoji_choices = emoji_choices
        self.date_of_message = date_of_message
        self.time_of_message = time_of_message
                
class Good_Luck(Template):
    def __init__(self, greetings: List, send_to_names: List, day_adjectives:List, locations: List, closing_statements: List, emoji_choices: List. date_of_message: int, time_of_message: Array):
        super().__init__()
        self.template_name = template_name
        self.greetings = greetings
        self.send_to_names = send_to_namesc# Note to user: include desired punctuation after name. ex) Good luck mom! vs Good luck mom. 
        self.day_adjectives = day_adjectives
        self.locations = locations # Note to user: include desired punctuation after location. ex) at ...work! vs at ...work. 
        self.closing_statements = closing_statements
        self.emoji_choices = emoji_choices
        self.date_of_message = date_of_message
        self.time_of_message = time_of_message
        
class Happy_Birthday(Template):
    def __init__(self, greetings: List, send_to_names: List, day_adjectives:List, locations: List, closing_statements: List, emoji_choices: List, date_of_message: int, time_of_message: Array):
        super().__init__()
        self.template_name = template_name
        self.greetings = greetings
        self.send_to_names = send_to_namesc# Note to user: include desired punctuation after name. ex) Happy birthday mom! vs Happy Birthday mom. 
        self.day_adjectives = day_adjectives
        self.locations = locations # Note to user: include desired punctuation after location. ex) at ...work! vs at ...work. 
        self.closing_statements = closing_statements
        self.emoji_choices = emoji_choices
        self.date_of_message = date_of_message
        self.time_of_message = time_of_message