import json
from .Enums import Equipment_Rarity, EqCondType, Color, Character_Type, Tag


class Equipment:
    def __init__(self, name, eqRarity, cond_type, condition, img_url):
        self.name = name #string
        self.rarity = eqRarity #enum
        self.cond_type = cond_type #character color, tag, or id combs
        self.condition = condition #dict 
        self.__image_url = img_url #string 
    
    #name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name
        
    #rarity
    @property
    def rarity(self):
        return self.__rarity.label
    
    @property #rarity rank for sorting
    def rarity_rank(self):
        return self.__rarity.rank
    
    @property
    def rarity_enum(self):
        return self.__rarity

    @rarity.setter
    def rarity(self, rarity):
        if not isinstance(rarity, Equipment_Rarity):
            raise TypeError("rarity must be Equipment Rarity enum")
        self.__rarity = rarity

    
    #condition type
    @property
    def cond_type_enum(self):  #enum for comparasion
        return self.__cond_type      
    
    @property
    def cond_type(self):  #for the to_dict
        return self.__cond_type.value

    @cond_type.setter
    def cond_type(self, cond_type):
        if not isinstance(cond_type, EqCondType):
            raise TypeError("condition type must EqCondType enum")
        self.__cond_type = cond_type
    
    
    
    #actual condition
    #will be used with Character to validate equipping
    @property
    def condition_raw(self): 
        return self.__condition

    #for to_dict
    @property
    def condition(self):
        #convert function depending on what value is 
        def convert(val): 
            if hasattr(val, "label"): #for those with the label attribute, return label val
                return val.label 
            
            elif hasattr(val, "value"): #if it only has the value attribute
                return val.value   
            
            return val #otherwise return val, (strings...)
            
        data = self.__condition

        # Case 1: dictionary (combinations), keys here are strings+enum
        if isinstance(data, dict):
            return {
                "cond_type": self.cond_type,
                #each dictionary key is converted appropriately depending on what it is
                "data": {              
                    k: convert(v) 
                    for k, v in data.items()
                }
            }

        # Case 2: set (tag AND/OR)
        elif isinstance(data, set):
            return {
                "cond_type": self.cond_type,
                "data": [convert(x) for x in data] #list of Tag.values
            }

        # Case 3: single value
        else:
            return {
                "cond_type": self.cond_type,
                "data": convert(data) #string
            }
        
        
    @condition.setter
    def condition(self, cond):
        ct = self.cond_type_enum #enum type
        if ct not in self._VALIDATORS:
            raise TypeError("Unsupported condition type")
        validator = self._VALIDATORS[ct]
        self.__condition = validator(cond)

            
    def to_dict(self):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "condition": self.condition, #type + value
            "image": self.__image_url
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent = 2)
    
    #validate id
    @staticmethod
    def _validate_id(cond):
        if not isinstance(cond, str):
            raise TypeError("idCond should be a string")
        return cond
    
    #validate name
    @staticmethod
    def _validate_name(cond):
        if not isinstance(cond, str):
            raise TypeError("nameCond should be a string")
        return cond

    #validate color
    @staticmethod
    def _validate_color(cond):
        if not isinstance(cond, Color):
            raise TypeError("color should be Enum Color")
        return cond

    #validate type
    @staticmethod
    def _validate_type(cond):
        if not isinstance(cond, Character_Type):
            raise TypeError("char type should be Enum Character Type")
        return cond
    
    #tag
    @staticmethod
    def _validate_tag(cond):
        if not isinstance(cond, Tag):
            raise TypeError("Tag should be Enum Tag")
        return cond
    

    #############################################
    #for combinations below, check entry format
    #each key condition is then checked to follow correct format

    #name and color
    @staticmethod
    def _validate_name_and_color(cond):

        if not isinstance(cond, dict):
            raise TypeError("Must be a dictionary")
        
        allowed = {"name", "color"}
        if set(cond.keys()) != allowed:
            raise TypeError(f"Expected keys {allowed}, got {set(cond.keys())}")
        
        if not isinstance(cond["name"], str):
            raise TypeError("name must be str")
        
        if not isinstance(cond["color"], Color):
            raise TypeError("color must be Color enum")
        return cond

    #name and type
    @staticmethod
    def _validate_name_and_type(cond):
        if not isinstance(cond, dict):
            raise TypeError("Must be a dictionary")

        allowed = {"name", "char_type"}
        if set(cond.keys()) != allowed:
            raise TypeError(f"Expected keys {allowed}, got {set(cond.keys())}")

        if not isinstance(cond["name"], str):
            raise TypeError("name must be str")

        if not isinstance(cond["char_type"], Character_Type):
            raise TypeError("type must be Character_Type enum")
        return cond

    #name and tag
    @staticmethod
    def _validate_name_and_tag(cond):
        if not isinstance(cond, dict):
            raise TypeError("Must be a dictionary")

        allowed = {"name", "tag"}
        if set(cond.keys()) != allowed:
            raise TypeError(f"Expected keys {allowed}, got {set(cond.keys())}")

        if not isinstance(cond["name"], str):
            raise TypeError("name must be str")

        if not isinstance(cond["tag"], Tag):
            raise TypeError("tag must be Tag enum")
        return cond
    
   

    #tag AND tag / tag OR tag
    @staticmethod
    def _validate_tag_pair(cond):
        if not (isinstance(cond, set) and len(cond) == 2):
            raise TypeError("tag and tag should be a set of 2")
        tags = cond #set of 2 tags

        #check tag
        if not all(isinstance(tag, Tag) for tag in tags):
            raise TypeError("tags should be Tag enum")
        return cond
    
    #tag and color
    @staticmethod
    def _validate_tag_and_color(cond):
        if not isinstance(cond, dict):
            raise TypeError("Must be a dictionary")

        allowed = {"tag", "color"}
        if set(cond.keys()) != allowed:
            raise TypeError(f"Expected keys {allowed}, got {set(cond.keys())}")

        if not isinstance(cond["tag"], Tag):
            raise TypeError("tag must be Tag enum")

        if not isinstance(cond["color"], Color):
            raise TypeError("color must be Color enum")
        return cond
    
    #tag and type
    @staticmethod
    def _validate_tag_and_type(cond):
        if not isinstance(cond, dict):
            raise TypeError("Must be a dictionary")

        allowed = {"tag", "char_type"}
        if set(cond.keys()) != allowed:
            raise TypeError(f"Expected keys {allowed}, got {set(cond.keys())}")

        if not isinstance(cond["tag"], Tag):
            raise TypeError("tag must be Tag enum")

        if not isinstance(cond["char_type"], Character_Type):
            raise TypeError("type must be Character Type enum")
        return cond
    
    #type and color
    @staticmethod
    def _validate_type_and_color(cond):
        if not isinstance(cond, dict):
            raise TypeError("Must be a dictionary")

        allowed = {"char_type", "color"}
        if set(cond.keys()) != allowed:
            raise TypeError(f"Expected keys {allowed}, got {set(cond.keys())}")

        if not isinstance(cond["char_type"], Character_Type):
            raise TypeError("type must be Character_Type enum")

        if not isinstance(cond["color"], Color):
            raise TypeError("color must be Color enum")
        return cond
    

    

    ########## CAN A CHARACTER EQUIP THIS EQUIP ############


    #check if equipment valid for a character
    def is_valid(self, character):
        return self.evaluate_condition(character) #will return true or false


    #takes in this equip, + a character, compare condition_type to
    #the valid character attribute
    def evaluate_condition(self, character): #evaluation based on inner functions
        data = self.condition_raw
        cond_type = self.cond_type_enum

        # --- Case 1: SINGLE VALUE ---   #Single Enums or Single Strings
        if not isinstance(data, (dict, set)):
            return self.match_single(cond_type, data, character) 

        # --- Case 2: DICTIONARY  --- complex and combinations
        if isinstance(data, dict):
            return all(
                self.match_field(key, value, character) #call the function for each key
                for key, value in data.items()
            )

        # --- Case 3: SET (TAG PAIR) ---
        
        if isinstance(data, set):
            if cond_type == EqCondType.TAG_OR_TAG:
                #any character tag part of the character
                return any(tag in character.tags_enum for tag in data)
            elif cond_type == EqCondType.TAG_AND_TAG:
                #both condition tags must be part of the character tags
                return all(tag in character.tags_enum for tag in data)

        return False

    #dictionary oondition for complex combination between
    # enum + tag, string + enum, ....
    def match_field(self, key, value, character):
        if key == "name":
            return character.name == value

        elif key == "char_type":
            return character.char_type_enum == value

        elif key == "color":
            return value in character.color_enum

        elif key == "tag":
            return value in character.tags

        return False

    #Single Enum or String
    def match_single(self, cond_type, value, character):
        if cond_type == EqCondType.ID:
            return character.char_id == value

        elif cond_type == EqCondType.NAME:
            return character.name == value

        elif cond_type == EqCondType.COLOR:
            return value in character.color_enum

        elif cond_type == EqCondType.TYPE:
            return character.char_type_enum == value

        elif cond_type == EqCondType.TAG:
            return value in character.tags

        return False


#store the functions as objects for the each validation
Equipment._VALIDATORS = {
    EqCondType.ID: Equipment._validate_id,
    EqCondType.NAME: Equipment._validate_name,
    EqCondType.COLOR: Equipment._validate_color,
    EqCondType.TYPE: Equipment._validate_type,
    EqCondType.TAG: Equipment._validate_tag,

    EqCondType.NAME_AND_COLOR: Equipment._validate_name_and_color,
    EqCondType.NAME_AND_TYPE: Equipment._validate_name_and_type,
    EqCondType.NAME_AND_TAG: Equipment._validate_name_and_tag,

    EqCondType.TAG_OR_TAG: Equipment._validate_tag_pair,
    EqCondType.TAG_AND_TAG: Equipment._validate_tag_pair,

    EqCondType.TAG_AND_COLOR: Equipment._validate_tag_and_color,
    EqCondType.TAG_AND_TYPE: Equipment._validate_tag_and_type,
    EqCondType.TYPE_AND_COLOR: Equipment._validate_type_and_color,
}