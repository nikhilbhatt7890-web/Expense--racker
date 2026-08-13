from new_user import new
from key import key
from main_interaction import Start_interaction
while True:
     USER_NAME = input("Hello their may i know your name ? (max 20 char): ").lower()
     if len(USER_NAME) > 20 :
          print("Name can only have at most 20 charactors ")
          continue
     break
     
     



def authenticate():
        
        file = f"backend/{USER_NAME}_data.txt"
        try:
            with open(file,"r"):
               return True
            
        except FileNotFoundError:
            return False
        
        except Exception as e :
            print(e)
            return None
    
# def after_new_login(name):
#      print("--"*10)
#      print(f"Thank you {name}\n For choosing us\nYour registration is successful\n")
#      next = initialization(name)
#      key_r = AVL_OPTIONS[next](name)
#      return key_r

     
def terminate(name):
     print(f"\nsorry {name} but something bad happen in our side ")
     


def initialization(name):
    print("--"*20,"\n")

    while True:   
        try :
                user_input = input(
                     "Want to login using a keyword\n" \
                     "(type 'key')\n" \
                     "plz enter a valid response -> : "
                ).upper().strip()

                if user_input in AVL_OPTIONS :
                    print()
                    return user_input
                
        except KeyError: 
                print("\n INVALID INPUT : \n")
                continue

def start_working(task:bool): # task values: true or false 
    if not(task) :
       initialize_work = AVL_OPTIONS[new(USER_NAME)](USER_NAME) # output --> key
    else :
       initialize_work = AVL_OPTIONS[task](USER_NAME)  # output --> key

    key_status = AVL_OPTIONS[initialize_work](USER_NAME)  # output --> approved , none 
    if key_status is None:
             return "END"                        
    interaction_start = AVL_OPTIONS[key_status](USER_NAME) # output --> yet to decide 
    print("success till interaction")

    
AVL_OPTIONS = {
    True : initialization,
    False:new,
    "KEY":key,
    "NEW_SUCCESS":initialization,
    "APPROVED":Start_interaction,
}
 
if __name__ == "__main__":
    
    exists_status = authenticate()
    if exists_status is None :
            terminate(USER_NAME)
    else:             
     start_working(exists_status)


    
