import re
precepts = [r"Hello|hi|hiya|greetings|aloha",
            r"tea|coffee|drink|lunch|breakfast|meal|food", 
            r"cafe|restaurant|bar",
            r"Thank You|Thanks|tnx|appreciated|Thats it"]

responses = ["Hello, how can I assist You today?",
             "Sure, where would You like to have it? A cafe in campus maybe?",
             "There are two cafes - in main building and near the lecture halls",
             "You are welcome"
             ]


#Zips two lists into one dictionary, first list as keys, second list as values
def zip_responses(precepts, responses):
    return dict(zip(precepts,responses))

zip_res = zip_responses(precepts,responses)
    
def chatbot_response(user_input):
    response = False
    for pattern in zip_res.keys():
            
            if re.search(pattern, user_input,re.IGNORECASE):
                response = zip_res[pattern]#get value of the precept as a key
                print("Chatbot: ", response)
            
                
              
    if response== False:
                print("I'm sorry, I don't know how to help You with that.")
   



#Function to get user input and respond
def chat():
    #User welcome and termination instruction
    print("Welcome! Type 'bye' to exit.")
    
    

    #Main loop
    while True:
        #1. Get user input
        user_input = input("You: ")

        
        
        #2. Check if user wants to exit
        if user_input == 'bye':
            print("Bye Bye")
            break
        
            
        #3. Search for a pattern in the percepts and fetch a prepared responses            
        chatbot_response(user_input)

#chat()

formated = 'You can have {food_item} and a {drink_item} with me'.format(drink_item='soda', food_item = 'burger')
food = 'burger'
drink = 'soda'


fstring = f'Grab a {food} and a {drink} with me'
# print(formated)
# print(fstring)

name_regex = r"\b[A-Z]\w+"
color_regex = r"color|tone|shade"
color = "My favourite color is red"
name = "Emils"

#print(re.search(name_regex, name))
print(re.search(color_regex, color))