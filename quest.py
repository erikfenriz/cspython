STRENGTH = 'STRENGTH'
WISDOM = 'WISDOM'
AGILITY = 'AGILITY'

RAM = 'RAM'
FIREBALL = 'FIREBALL'
RANGE = 'RANGE'

KNIGHT = 'KNIGHT'
MAGE = 'MAGE'
RANGER = 'RANGER'

defaultStrengthLvl = 5
defaultWisdomLvl = 5
defaultAgilityLvl = 5

strengthLvl = defaultStrengthLvl
wisdomLvl = defaultWisdomLvl
agilityLvl = defaultAgilityLvl

skill = ''
companion = ''

firstResult = ''
secondResult = ''
thirdResult = ''


def getParameters():
    return f"Your parameters are: strength {strengthLvl}; wisdom {wisdomLvl}; agility {agilityLvl};"


firstResult = input(
    f"You launch a new game. The game asks: what would you like to do? Build {STRENGTH}, {WISDOM} or {AGILITY}? ").upper()

if (firstResult == STRENGTH):
    print(
        f"You change the parameters of your character. You see how power grows: {strengthLvl} >> {strengthLvl + 2}")
    strengthLvl = strengthLvl + 2
elif (firstResult == WISDOM):
    print(
        f"You change the parameters of your character. You see how brain gets bigger: {wisdomLvl} >> {wisdomLvl + 2}")
    wisdomLvl = wisdomLvl + 2
elif (firstResult == AGILITY):
    print(
        f"You change the parameters of your character. You see how mobility increases: {agilityLvl} >> {agilityLvl + 2}")
    agilityLvl = agilityLvl + 2
else:
    print("Why would you even play the game if nothing fits.")

print("")

if (strengthLvl == 6):
    print("With great strength comes  great responsibility. You wield the sword and think that it fits you.")
elif (wisdomLvl == 6):
    print("Knowing yourself is the beginning of all wisdom. You grab the stuff and think that it fits you.")
elif (agilityLvl == 6):
    print("Strength without agility is a mere mass. You take the bow and think that it fits you.")

secondResult = input(
    f"You continue to create your character. The game asks: what would you like to learn? {RAM}, {FIREBALL} or {RANGE}? ").upper()

if (secondResult == RAM):
    print(
        f"You have learned something new. You see how power grows: {strengthLvl} >> {strengthLvl + 1}")
    strengthLvl = strengthLvl + 1
    skill = RAM
elif (secondResult == FIREBALL):
    print(
        f"You have learned something new. You see how brain gets bigger: {wisdomLvl} >> {wisdomLvl + 1}")
    wisdomLvl = wisdomLvl + 1
    skill = FIREBALL
elif (secondResult == RANGE):
    print(
        f"You have learned something new. You see how mobility increases: {agilityLvl} >> {agilityLvl + 1}")
    agilityLvl = agilityLvl + 1
    skill = RANGE
else:
    print("Why would you even play the game if nothing fits.")

print("")

thirdResult = input(
    f"You continue to create your character. Who will be your partner along the way? Partner's knowledge will go to you: {KNIGHT}, {MAGE} or {RANGER}? ").upper()

if (thirdResult == KNIGHT):
    print(
        f"You chose the knight. You see how power grows: {strengthLvl} >> {strengthLvl + 1}")
    strengthLvl = strengthLvl + 1
    companion = KNIGHT
elif (thirdResult == MAGE):
    print(
        f"You chose the mage. You see how brain gets bigger: {wisdomLvl} >> {wisdomLvl + 1}")
    wisdomLvl = wisdomLvl + 1
    companion = MAGE
elif (thirdResult == RANGER):
    print(
        f"You chose the ranger. You see how mobility increases: {agilityLvl} >> {agilityLvl + 1}")
    agilityLvl = agilityLvl + 1
    companion = RANGER
else:
    print("One does not simply walk into Mordor.")

print("")

if (strengthLvl == defaultStrengthLvl and wisdomLvl == defaultWisdomLvl and agilityLvl == defaultAgilityLvl):
    print("You never loved any games in the first place. You turn off the game and go sleep.")
elif (strengthLvl == wisdomLvl == agilityLvl):
    print(f"{getParameters()} This is what I call balanced development.")
elif ((strengthLvl > agilityLvl and skill == RANGE) or
      (strengthLvl > wisdomLvl and skill == FIREBALL) or
      (wisdomLvl > strengthLvl and skill == RAM) or
      (wisdomLvl > agilityLvl and skill == RANGE) or
      (agilityLvl > strengthLvl and skill == RAM) or
      (agilityLvl > wisdomLvl and skill == FIREBALL)):
    print(
        f"Well, this is unusual. You chose {skill} that might be not the perfect fit for your build. {getParameters()}. I hope that you know what you are doing. Of course you do. Do you?")

if (companion == KNIGHT or companion == MAGE or companion == RANGER):
    print(
        f"You start the game with {companion}. He will follow you and help throughout your adventure.")

# Creativity points
# The creativity lies in the questions a player can pick that portrays the process of creating a character for an rpg game. The choices a player makes will reflect one's playthrough experience of which player is notified through the system

# The program shown and explained points
# The program was shown to my wife. She is quite comfortable with coding as she learned Unity engine with me. She didn't like that everything is one place but since it is not a commercial product then it is fine.