import re

# Predefined response patterns
pattern_dict = {
    r"\b(hello|hi|hey|hiya|greetings)\b": "Hi there! How are you doing today?",
    r"\b(taxi|bus|public transport|uber|private hire)\b": "There are taxis parked on road at south of campus and bus stop just by the main gate",
    r"\b(tea|coffee|food|meal|lunch|hungry|breakfast|drink)\b": "Sure, where would you like to have it? A cafe in campus maybe?",
    r"\b(cafe|campus|near|here|local)\b": "There are two cafes - in main building and near the lecture halls",
    r"\b(restaurant|best|classy|expensive|glamorous)\b": "There is a restaurant on the North part of the Campus",
    r"\b(what time|closing|opening hours|working hours|business hours)\b": "Both cafes and the restaurant are open from 8AM till 8PM",
    r"\b(bye|goodbye|see you|thank you|that's all)\b": "Goodbye! Have a great day."
}

# Captured user info
state = {}

# Dynamic patterns for capturing data
dynamic_patterns = {
    r"my name is (?P<name>\w+)": "Nice to meet you, {name}!",
    r"my favorite color is (?P<color>\w+)": "{color} is a beautiful color!"
}

# Predefined fallback detection
def detect_pattern(user_input):
    matched = False
    for pattern, response in pattern_dict.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            print("Bot:", response)
            matched = True
            break
    if not matched:
        print("Bot: I'm sorry, I didn't understand that.")

# Chatbot main function
def chat():
    print("Hello, how can I help you today?")
    while True:
        user_input = input("You: ")
        matched = False  # Track if a response was generated
        
        for pattern, template in dynamic_patterns.items():
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                group_dict = match.groupdict()
                state.update(group_dict)
                print("Bot:", template.format(**state))
                matched = True
                break  # Stop checking further patterns

        if not matched:
            # Check for exit first
            if re.search(r"(bye|goodbye|see you|thank you|that's all)", user_input, re.IGNORECASE):
                print("Goodbye!")
                exit()
            else:
                detect_pattern(user_input)


# Start chatbot
chat()