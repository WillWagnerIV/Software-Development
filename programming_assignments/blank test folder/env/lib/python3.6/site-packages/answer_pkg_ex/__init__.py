name = "answer_pkg_ex"

class BigQ:

    # Ask the question
    def ask_question():
        
        user_answer = input ('\nEnter the answer to Life, the Universe, and Everything. 0 to quit. (Hint: 42): ')
        return user_answer

    # Give an appropriate response
    def give_response(user_answer):

        if user_answer == "42":
            print ('\nThat is the correct answer.  Please come back in 1,000,000 years for the Question.')

        elif user_answer == "0" :
            return False

        else:
            print ('\nIncorrect.')  
            print ('Please restart your World or contact Magrathean Technical Support if the problem persists.')




def provide_insight():

    insight_main_looping = True

    while insight_main_looping == True:

        user_answer = BigQ.ask_question()

        if BigQ.give_response (user_answer) == False:
            insight_main_looping = False