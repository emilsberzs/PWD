import re

# Define patterns with regex
pattern_dict = {
    r"\b(hello|hi|hey|hiya|greetings)\b": "Hi there! How are you doing today?",
    r"\b(taxi|bus|public transport|uber|private hire)":"There are taxis parked on road at south of campus and bus stop just by the main gate",
    r"\b(tea|coffee|food|meal|lunch|hungry|breakfast|drink)":"Sure, where would You like to have it? A cafe in campus maybe?",
    r"\b(cafe|campus|near|here|local)\b":"There are two cafes - in main building and near the lecture halls",
    r"\b(restaurant|best|classy|expensive|glamorous)\b":"There is a restaurant on the North part of the Campus",
    r"\b(what time|closing|opening hours|working hours|business hours)":"Both cafes and the restaurant are open from 8AM till 8PM",
    r"\b(bye|goodbye|see you|thank you|that's all)\b": "Goodbye! Have a great day."
}

def detect_pattern(user_input):
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