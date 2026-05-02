import json
from .Enums import Color, Character_Rarity, Tag, Character_Type, SpecialBadge


class Character:
    def __init__(self, char_id, name, color, rarity, tags, special, character_type, img_url):
        self.char_id = char_id #string 
        self.name = name #string
        self.color = color #ordered tuple  of enum
        self.rarity = rarity #enum
        self.tags = tags #set of enums
        self.special = special #set of enums
        self.char_type = character_type #1 enum
        self.__image_url = img_url #string

    #id
    @property
    def char_id(self):
        return self.__char_id

    @char_id.setter
    def char_id(self, char_id):
        if not isinstance(char_id, str):
            raise TypeError("Id must be a string")
        self.__char_id = char_id

    #name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name

    #color
    @property
    def color_enum(self):
        return self.__color  # raw tuple of Color enums
    
    @property
    def color(self):
        return [color.value for color in self.__color]

    @color.setter
    def color(self, color):
        #color assignment should be tuple of length 1 or 2
        if not (isinstance(color, tuple) and len(color) in (1,2)):
            raise TypeError("colors should be a tuple of max length 2")
        for c in color:
            if not isinstance(c, Color):
                raise TypeError("each color should be Color enum")
        self.__color = color

    #rarity
    @property
    def rarity(self):
        return self.__rarity.label
    #rarity rank
    @property
    def rarity_rank(self):
        return self.__rarity.rank
    
    @rarity.setter
    def rarity(self, rarity):
        if not isinstance(rarity, Character_Rarity):
            raise TypeError("condition must be Character rarity enum ")
        self.__rarity = rarity


    #tags
    @property
    def tags(self):
        return [tag.value for tag in self.__tags]
    
    @property
    def tags_enum(self):
        return self.__tags

    @tags.setter
    def tags(self, tags):
        if not isinstance(tags, set):
            raise TypeError("tags should be a set")
        for tag in tags:
            if not isinstance(tag, Tag):
                raise TypeError("each tag should be enum Tag")
        self.__tags = tags

    #LL / Zenaki
    @property
    def special(self):
        return [badge.value for badge in self.__special]
        
    
    @special.setter
    def special(self, specials):
        if not isinstance(specials, set):
            raise TypeError("specials should be a set")
        for badge in specials:
            if not isinstance(badge, SpecialBadge):
                raise TypeError("badge should be a Special Badge enum")
        self.__special = specials

    #Character Type
    @property
    def char_type_enum(self):
        return self.__char_type
    
    @property
    def char_type(self):
        return self.__char_type.value
    
    @char_type.setter
    def char_type(self, char_type):
        if not isinstance(char_type, Character_Type):
            raise TypeError("char_type should be Character Type enum")
        self.__char_type = char_type

    #list of valid equips from equipment list
    def get_valid_equips(self, all_equipment):
        valids = []

        #check which equips are valid
        for equip in all_equipment: 
            if equip.is_valid(self):
                valids.append(equip)

        #return them sorted by rarity
        return sorted(valids, key=lambda e: e.rarity_rank, reverse=True)
        
    
    

    def to_dict(self):
        #return dictionary of the character info
        return {
            "id": self.char_id,
            "name": self.name,
            "colors": self.color,
            "tags": self.tags,
            "badges": self.special,
            "rarity": self.rarity,
            "char_type": self.char_type, 
            "image": self.__image_url
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent = 2)


