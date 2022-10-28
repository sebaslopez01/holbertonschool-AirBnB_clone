# holbertonschool-AirBnB_clone

### Description

This repository contains the files to simulate a basic console with the implementetion of basic models and a serialization and deserialization model.


### Command Interpreter
To start the command interpreter run de the console.py program: ./console.py
  #(hbnb) 

### How to use it
Enter a valid command follow by an argument
  #(hbnb) create BaseModel

### Available Commands
  create [model] - Creates a new instance of a valid class name, saves it to a JSON file and prints the id.
  
  show [model] [id] - Prints the string representation of an instance based on the class name and id.
  
  destroy [model] [id] - Deletes an instance based on the class name and id (save the change into the JSON file).
  
  all [model] - Prints all string representation of all instances based or not on the class name.
  
  update [model] [id] [attribute name] [attribute value] - Updates an instance based on the class name and id, by adding or updating attribute.
  
  quit - Exit the program
  
  help [command] - Get help with a command or in general with the program.
  
### Examples
  ./console.py
  
  (hbnb) create BaseModel
  49faff9a-6318-451f-87b6-910505c55907
  
  show BaseModel 49faff9a-6318-451f-87b6-910505c55907
  [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
  
  all BaseModel
  ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
  
  destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
  
  all BaseModel
  [""]
