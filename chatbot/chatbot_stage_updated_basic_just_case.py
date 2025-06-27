import re

# Define patterns with regex
#Matches the name if uppercase, but if can takes first word starting with uppercase
name_regex = r"\b[A-Z]\w+"
#lookback and lookahead to match only the word for coor instead of the whole input string
color_regex = r"(?<=color is )\w+|(?<=color )\w+|\w+ (?=color)|\w+ (?=tone)"
pattern_dict = {
    r"\b(hello|hi|hey|hiya|greetings)\b": "Hi there! How are you doing today?",
    r"\b(taxi|bus|public transport|uber|private hire)":"There are taxis parked on road at south of campus and bus stop just by the main gate",
    r"\b(tea|coffee|food|meal|lunch|hungry|breakfast|drink)":"Sure, where would You like to have it? A cafe in campus maybe?",
    r"\b(cafe|campus|near|here|local)\b":"There are two cafes - in main building and near the lecture halls",
    r"\b(restaurant|best|classy|expensive|glamorous)\b":"There is a restaurant on the North part of the Campus",
    r"\b(what time|closing|opening hours|working hours |business hours)":"Both cafes and the restaurant are open from 8AM till 8PM",
    r"\b(bye|goodbye|see you|thank you|that's all)\b": "Goodbye! Have a great day."
}
user_state = {'name':'there',
            'color':'None'}


def detect_pattern(user_input):
    if re.search(color_regex,user_input):
        
        color_result = re.search(color_regex, user_input)
        user_state['color'] = color_result.group(0)
        print("Bot: Your favourite color is",user_state["color"])
        
    if re.search(name_regex,user_input):
        name_result = re.search(name_regex, user_input)
        user_state['name'] = name_result.group()
        print('Bot: Pleased to meet You', user_state["name"])

    
    

    matched = False
    for pattern, response in pattern_dict.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            print("Bot:", response)
            matched = True
            break
    if not matched:
        print("Bot: I'm sorry, I didn't understand that.")
        
# Main chatbot loop
def chat():
    print("Hello, how can I help You today?")
    while True:
        user_input = input("You: ")
        if re.search(r"\b(bye|goodbye|see you|thank you|that's all)\b", 
                    user_input, re.IGNORECASE):
            print("Goodbye")
            exit()
        else:
            detect_pattern(user_input)
            
chat()


formated = 'You can have {food_item} and a {drink_item} with me'.format(drink_item='soda', food_item = 'burger')
food = 'burger'
drink = 'soda'


fstring = f'Grab a {food} and a {drink} with me'
# print(formated)
# print(fstring)

color = "My favourite tone is red"
name = "Emils"

#print(re.search(name_regex, name))
#print('color check: ')
#print(re.search(color_regex, color))
#print('name check: ')
#print(re.search(name_regex, name))