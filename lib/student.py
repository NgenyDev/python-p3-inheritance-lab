
#!/usr/bin/env python

from user import User

class Student(User):
    def _init_(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = []  # Initialize 'knowledge' as an empty list


    
    
    
    def learn(self,knowledge_str):
        self.knowledge.append(knowledge_str)
        pass