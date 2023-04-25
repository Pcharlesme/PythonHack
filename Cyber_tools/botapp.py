import re
import  long_reponses as long


def message_probability(user_message, recognised_words, single_response =False, requires_words=[] ):
    message_certainty = 0
    has_received_words =True
    
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
            
            
    percentage= float(message_certainty) / float(len(recognised_words))
    
    for word in requires_words:
        if word not in user_message:
            has_received_words = False
            break
        
    if has_received_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
    
    def check_all_messages(message):
        highest_prob_list ={ }
        
    def response(bot_response, list_of_word, single_response=False, required_words=[ ]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]= message_probability(message, list_of_words, single_response, required_words)
        
    
    # response
    response('hello')
    
    
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))