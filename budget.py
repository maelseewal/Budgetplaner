# @Name: Mael Seewald
# @Email: maelseewald@gmx.net
# @GitHub: https://github.com/maelseewal
# @Version:
# @Created at: 2024-12-04 09:16:00
# @Last Modified: 2024-12-04 09:16:00
import json
import os

# set a variable for the path of the json
bjson = "budget.json"

# Function for adding information
def addtransaction(bjson):
    try:
        # User input
        name = input("Warum gab es eine Änderung: ")
        geld = float(input("Um wie viel Geld geht es: "))

        # formating
        new_entry = {
            "name": name,
            "geld": geld,
        }
        # If the file exists
        if os.path.exists(bjson): 
            with open(bjson, "r") as json_file:
                try:
                    data = json.load(json_file)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    data = []
            data.append(new_entry)
        # If the file not exists
        else:
            data = [new_entry]

        with open(bjson, "w") as json_file:
            json.dump(data, json_file, indent=4)
        menu()
    # Reaction to an error
    except ValueError:
        print("\033[31mDeine Eingabe ist nicht akzeptiert!\033[0m")
        menu()
 
# Function for the output of all actions
def showtransaction(bjson):
    # Open and load the file
    with open(bjson, 'r') as file:
        data = json.load(file)
    # the top line separately
    print("\033[32m-\033[0m" * 20) 
    # Output of the elements
    for item in data:
        for key, value in item.items():
            print(f"{key}: {value}")
        print("\033[32m-\033[0m" * 20)  

    menu()

# Function for spending the assets
def showsum(bjson):
  count = 1
  # Open and load the file
  with open(bjson,'r') as file:
    data = json.load(file)
  allegeld = [item['geld'] for item in data]

  # Find number of elements in json
  allegeldmenge = len(allegeld)
  summe = 0

  # Calculation of the credit balance
  while count < allegeldmenge:
     summe = summe + allegeld[count -1]
     count = count + 1
  # add last element separately
  summe = summe + allegeld[allegeldmenge-1]
  # Output of the total
  print(summe)
  menu()

# Function for the start screen
def menu():
  try:
    choice = int(input("Was Willst du tun?\nTransaktion hinzufügen \033[32m[1]\033[0m\nTransaktionen anzeigen \033[32m[2]\033[0m\nSumme anzeigen \033[32m[3]\033[0m\nBeenden \033[32m[ctrl + C]\033[0m\n"))
    if choice == 1:
        addtransaction(bjson)
    elif choice == 2:
        print (showtransaction(bjson))
    elif choice == 3:
      print (showsum(bjson))
    else:
     print("Das war keine Auswahlmöglichkeit!!")

  # Interception of error messages
  except ValueError:
    print("\033[31mDeine Eingabe ist nicht Aktzeptiert!\033[0m")
    menu()
  except KeyboardInterrupt:
     print("\033[31mProgramm beendet\033[0m")
  except FileNotFoundError:
     print("\033[31mDas Dokument ist leer!\033[0m")
     menu()

# Function call for the start screen
menu()
