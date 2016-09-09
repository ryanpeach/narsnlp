def do_check(ask, check, error = lambda x: print("Error: "+str(x))):
    """ Given an ask function, ask() returning some value \"answer\",
        Loop until check(answer) returns True. 
        Runs error(answer) each time check returns False."""
    while True:
        answer = ask()
        if check(answer):
            return answer
        else:
            error(answer)

def str_to_logic(text):
    """ Converts a string into logic, or returns None if no logic found. """
    try:
        return bool(float(text))
    except:
        text = str(text).lower()
        if text in ['y','yes','confirm','t','true']:
            return True
        elif text in ['n','no','f','false']:
            return False
        
def confirmYN(question):
    """ Asks a simple yes/no question and returns True/False """
    ask = lambda: str_to_logic(raw_input(question + " [Y/n]: "))
    check = lambda x: x != None
    error = lambda x: print("Invalid response, please respond Y or n.")
    return do_check(ask, check, error)