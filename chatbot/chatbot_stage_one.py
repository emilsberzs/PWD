precepts = ["Hello","tea", "cafe","Thank You"]

responses = ["Hello, how can I assist You today?",
             "Sure, where would You like to have it? A cafe in campus maybe?",
             "There are two cafes - in main building and near the lecture halls",
             "You are welcome"
             ]

#Function to get user input and respond
def chatbot():
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
            
        #3. Search fot a pattern in the percepts and fetch a prepared responses
            #3.1 Check if any of percepts are in the input
        response_found = False
        for pattern in precepts:
            if pattern in user_input:
                response_found = True
            #3.2 Return the index
                ind = precepts.index(pattern)
            
            #3.3 Use index to find response
                response = responses[ind]
                print("Chatbot: ", response)
            #3.4 Break the loop
                break
        if response_found == False:
            print("I'm sorry, I don't know how to help You with that.")

chatbot()