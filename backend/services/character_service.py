from backend.data.database import CHARACTERS
from backend.models.Enums import Tag, SpecialBadge


# -------------- FILTERS -------------

#by tag, this list goes in Team constructor
def filter_by_tag(characters, tag):
    filtered_list = [character for character in characters if tag in character.tags_enum]

    #filter the return list by character rarity
    return sorted(filtered_list, key=lambda e: e.rarity_rank, reverse=True)

#by color
def filter_by_color(characters, color): #list + enum
    filtered = [character for character in characters if color in character.color_enum]

    #sort by rarity
    return sorted(filtered, key=lambda e: e.rarity_rank, reverse=True)

#by rarity
def filter_by_rarity(characters, rarity): #list + enum
    return  [character for character in characters if character.rarity == rarity]

    



# ------------- ADD / REMOVE / EDIT -------------


def add_character(character):
    if character.char_id not in CHARACTERS_BY_ID:
        CHARACTERS.append(character)  #add to list
        CHARACTERS_BY_ID[character.char_id] = character  #add to dict too
    else:
        raise Exception("Character already exists")
    


def delete_character(char_id):
    if char_id not in CHARACTERS_BY_ID:
        raise Exception("Character Id not found")
    else:
        character = CHARACTERS_BY_ID.get(char_id) #get the character from dict
        del CHARACTERS_BY_ID[char_id] #delete from dictionary
        CHARACTERS.remove(character) #delete from list


def edit_character(char_id, **kwargs):
    character = CHARACTERS_BY_ID.get(char_id)

    if not character:
        raise Exception("Character not found")

    # name
    if "name" in kwargs:
        character.name = kwargs["name"]

    # rarity (must be enum)
    if "rarity" in kwargs:
        character.rarity = kwargs["rarity"]

    # char_type (enum)
    if "char_type" in kwargs:
        character.char_type = kwargs["char_type"]

    # tags (convert strings → enums)
    if "tags" in kwargs:
        character.tags = {
            Tag[t] if isinstance(t, str) else t
            for t in kwargs["tags"]
        }

    # special badges (convert strings → enums)
    if "special" in kwargs:
        character.special = {
            SpecialBadge[s] if isinstance(s, str) else s
            for s in kwargs["special"]
        }

    # image (simple string)
    if "image" in kwargs:
        character._Character__image_url = kwargs["image"]

    return character
    


CHARACTERS_BY_ID = {char.char_id: char for char in CHARACTERS}

