from enum import Enum

#Character tags
class Tag(Enum):
    #main tags
    SAIYAN = "Saiyan"
    HYBRID_SAIYAN = "Hybrid Saiyan"
    SUPER_SAIYAN = "Super Saiyan"
    SUPER_SAIYAN_2 = "Super Saiyan 2"
    SUPER_SAIYAN_3 = "Super Saiyan 3"
    SUPER_SAIYAN_4 = "Super Saiyan 4"
    SUPER_SAIYAN_GOD = "Super Saiyan God"
    SUPER_SAIYAN_GOD_SS = "Super Saiyan God SS"
    SUPER_SAIYAN_ROSE = "Super Saiyan Rose"
    NAMEKIAN = "Namekian"
    ANDROID = "Android"
    SHADOW_DRAGON = "Shadow Dragon"
    GOD_OF_DESTRUCTION = "God of Destruction"
    ANGEL = "Angel"
    KIDS = "Kids"
    GIRLS = "Girls"
    REGENERATION = "Regeneration"
    POWERFUL_OPPONENT = "Powerful Opponent"
    TRANSFORMING_WARRIOR = "Transforming Warrior"
    LINEAGE_OF_EVIL = "Lineage of Evil"
    MINION = "Minion"
    TWINS = "Twins"
    OTHERWORLD_WARRIOR = "Otherworld Warrior"
    FUSION_WARRIOR = "Fusion Warrior"
    GODKI = "Godki"
    SON_FAMILY = "Son Family"
    VEGETA_CLAN = "Vegeta Clan"
    SUPER_WARRIOR = "Super Warrior"
    FRIEZA_FORCE = "Frieza Force"
    GINYU_FORCE = "Ginyu Force"
    TEAM_BARDOCK = "Team Bardock"
    HERA_CLAN = "Hera Clan"
    TURLES_CRUSHER_CORPS = "Turles Crusher Corps"
    FUTURE = "Future"
    GT = "GT"
    DAIMA = "Daima"
    MERGING = "Merging"
    ABSORPTION = "Absorption"
    FUSION = "Fusion"
    POTARA = "Potara"
    WEAPON_WIELDER = "Weapon Wielder"
    RIVAL_UNIVERSE = "Rival Universe"
    UNIVERSE_2 = "Universe 2"
    UNIVERSE_4 = "Universe 4"
    UNIVERSE_6 = "Universe 6"
    UNIVERSE_9 = "Universe 9"
    UNIVERSE_11 = "Universe 11"
    UNIVERSE_REP = "Universe Rep"
    DB = "DB"
    EVENT_EXCLUSIVE = "Event Exclusive"
    LEGENDS_ROAD = "Legends Road"

    #episodes tags
    GAME_ORIGINALS = "Game Originals"
    DRAGON_BALL_SAGA = "Dragon Ball Saga"

    #Z Sagas
    SAIYAN_SAGA = "Saiyan Saga (Z)"
    FRIEZA_SAGA = "Frieza Saga (Z)"
    ANDROID_SAGA = "Android Saga (Z)"
    CELL_SAGA = "Cell Saga (Z)"
    MAJIN_BUU_SAGA = "Majin Buu Saga (Z)"

    #GT Sagas
    BLACK_STAR_DRAGON_BALL_SAGA = "Black Star Dragon Ball Saga (GT)"
    SUPER_BABY_SAGA = "Super Baby Saga (GT)"
    SUPER_17_SAGA = "Super #17 Saga (GT)"
    SHADOW_DRAGON_SAGA = "Shadow Dragon Saga (GT)"

    #Super sagas, uses (S) in string
    GOD_OF_DESTRUCTION_BEERUS_SAGA = "God of Destruction Beerus Saga (S)"
    FRIEZA_RESURRECTED_SAGA = "Frieza Resurrected Saga (S)"
    GOD_OF_DESTRUCTION_CHAMPA_SAGA = "God of Destruction Champa Saga (S)"
    FUTURE_TRUNKS_SAGA = "Future Trunks Saga (S)"
    UNIVERSE_SURVIVAL_SAGA = "Universe Survival Saga (S)"

    #Other sagas
    SAGAS_FROM_THE_MOVIES = "Sagas from the Movies"
    ANIME_ORIGINAL_SAGAS = "Anime Original Sagas"
    DRAGON_BALL_FIGHTERZ = "Dragon Ball FighterZ"
    DRAGON_BALL_Z_KAKAROT = "Dragon Ball Z: Kakarot"
    DAIMA_SAGA = "Daima Saga"
    DRAGON_BALL_40TH_ANNIVERSARY = "Dragon Ball 40th Anniversary"


#Character colors
class Color(Enum):
    YELLOW = ("Yellow")
    BLUE = ("Blue")
    PURPLE = ("Purple")
    RED = ("Red")
    GREEN = ("Green")
    LIGHT = ("Light")

    def __init__(self, label):
        self.__label = label
    @property
    def label(self):
        return self.__label

   



#Character rarities
class Character_Rarity(Enum):
    EXTREME = ("Extreme", 1)
    SPARKING = ("Sparking", 2)
    ULTRA = ("Ultra", 3)
    LEGEND = ("Legend", 4)

    def __init__(self, label, rank):
        self.__label = label
        self.__rank = rank

    @property
    def label(self):
        return self.__label
    @property
    def rank(self):
        return self.__rank

    


#Zenkai / LL
class SpecialBadge(Enum):
    LEGENDS_LIMITED = "Legends_Limited"
    ZENKAI = "Zenkai"

#Type
class Character_Type(Enum):
    MELEE = "Melee"
    RANGED = "Ranged"
    DEFENSE = "Defense" 
    SUPPORT = "Support"

class Equipment_Rarity(Enum):
    GOLD = ("Gold", 1)
    GOLD_AWAKENED = ("Gold Awakened", 2)
    UNIQUE = ("Unique", 3)
    UNIQUE_AWAKENED = ("Unique Awakened", 4)
    PLATINUM = ("Platinum", 5)

    def __init__(self, label, rank):
        self.__label = label
        self.__rank = rank

    @property
    def label(self):
        return self.__label
    @property
    def rank(self):
        return self.__rank

    
    

class EqCondType(Enum):
    #string 
    ID = "id" 
    NAME = "name" 

    #enum 
    COLOR = "color" 
    TYPE = "type"  
    TAG = "tag" 
    
    #dictionaries
    NAME_AND_COLOR = "name_and_color" 
    NAME_AND_TYPE = "name_and_type"    
    NAME_AND_TAG = "name_and_tag" 

    TYPE_AND_COLOR = "type_and_color" 
    
    TAG_AND_COLOR = "tag_and_color"  
    TAG_AND_TYPE = "tag_and_type"   

    #sets
    TAG_OR_TAG = "tag_or_tag"
    TAG_AND_TAG = "tag_and_tag"



class Admin_Type(Enum):
    ZENO = 4 #delete users  
    SUPREME_KAI = 3 #create users, promote G_O_D to ANGEL
    ANGEL = 2   #add characters, and equipments  
    GoD = 1   #edit guides w existing characters only 


class Admin_Permissions(Enum):
    #GoD
    EDIT_GUIDE = 1 

    #Angel
    ADD_ASSET = 2
    EDIT_ASSET = 2
    ASSIGN_GUIDE = 2

    #Supreme Kai
    DELETE_ASSET = 3
    EDIT_ADMIN = 3
    
    #Zeno
    DELETE_ADMIN = 4
             
                    
                                      
                                       



    
    






    

    
    

 