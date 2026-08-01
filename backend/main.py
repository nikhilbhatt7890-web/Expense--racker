from new_user import new
from key import key
from login import login

USER_NAME = input("hello their may i know your name ? : ").lower()
def do_nothing():
     pass

def alr_exists(self):
        pass

def initialization():
    while True:   
        try :
                user_input = input(
                     "what do you wana do\n1) new application(type 'new') \n" \
                     "2) have a keyword (type 'key')\n" \
                     "3) login using mobile number (type 'login') \n" \
                     "plz enter a valid response -> : "
                ).upper()

                if user_input in AVL_OPTIONS :
                    print()
                    return user_input
                else :
                    raise KeyError
                
        except KeyError as k: 
                print("\n INVALID INPUT : \n")
                continue

AVL_OPTIONS = {
    "NEW":new,
    "KEY":key,
    "LOGIN" : login
}

def start_working():
    work = AVL_OPTIONS[initialization()]
    next = work(USER_NAME)
    options = {
         "ALR_EXISTS":initialization, #### assign a work
         None:do_nothing   
    }
    again = options[next]
    again()  ##### assign a work


    
if __name__ == "__main__":
    print(f"\n{USER_NAME} we welcome you to our banking system\n")
    start_working()

    
