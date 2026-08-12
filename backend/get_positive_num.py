def get_positive(prompt:str):
    while True :
        try :

            value = int(input(f"{prompt}: "))

            if value <= 0:
                print("plz enter a positive number : ")
                continue
            elif  len(str(value)) >= 20:
                print("plz enter a small number:")
                continue
            return value

        except ValueError :
            print("INVALID INPUT")