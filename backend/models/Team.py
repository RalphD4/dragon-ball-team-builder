
class Team:
    def __init__(self, tag, characters):
        self.name = tag.value
        self.tag = tag
        self.characters = characters #list of Character
        

    #tag 
    @property
    def tag(self):
        return self.__tag
    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    #name , value of the enum
    @property
    def name(self):
        return self.tag.value
    @name.setter
    def name(self, name):
        self.__name = name
    

    #filtered characters of the tag
    @property
    def characters(self):
        return self.__characters
    @characters.setter
    def characters(self, characters):
        self.__characters = characters

    def to_dict(self):
        return{
            "name": self.name,
            "characters": [character.to_dict() for character in self.characters]
        }

    
