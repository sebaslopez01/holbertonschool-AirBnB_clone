#!/usr/bin/python3

"""

This module defines a HBNBCommand Class

"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    valid_models = ['BaseModel', 'User', 'State',
                    'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, _arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, _arg):
        """ End of File, exit the program
        """
        return True

    def do_create(self, model_name: str):
        """ create [model]
        Creates a new instance of BaseModel"""
        if not model_name:
            print('** class name missing **')
            return False
        if model_name not in self.valid_models:
            print('** class doesn\'t exist **')
            return False

        if model_name == 'BaseModel':
            model = BaseModel()
        elif model_name == 'User':
            model = User()
        elif model_name == 'State':
            model = State()
        elif model_name == 'City':
            model = City()
        elif model_name == 'Amenity':
            model = Amenity()
        elif model_name == 'Place':
            model = Place()
        else:
            model = Review()

        model.save()

        print(model.id)

    def do_show(self, args: str):
        """ show [model] [id]
        Shows the string representation of the model"""
        args_lst = args.split()

        if len(args_lst) == 0:
            print('** class name missing **')
            return False
        elif len(args_lst) == 1:
            print('** instance id missing **')
            return False

        model_name, model_id, *_other = args_lst
        if model_name not in self.valid_models:
            print('** class doesn\'t exist **')
            return False

        model = models.storage.all().get(f'{model_name}.{model_id}')
        if not model:
            print('** no instance found **')
            return False

        print(model)

    def do_destroy(self, args: str):
        """ destroy [model] [id]
        Deletes an instance from the storage"""
        args_lst = args.split()

        if len(args_lst) == 0:
            print('** class name missing **')
            return False
        elif len(args_lst) == 1:
            print('** instance id missing **')
            return False

        model_name, model_id, *_other = args_lst
        if model_name not in self.valid_models:
            print('** class doesn\'t exist **')
            return False

        model = models.storage.all().get(f'{model_name}.{model_id}')
        if not model:
            print('** no instance found **')
            return False

        del models.storage.all()[f'{model_name}.{model_id}']
        models.storage.save()

    def do_all(self, model_name: str):
        """ all [model]
        Shows all string representation of all instances in storage"""
        storage_data = models.storage.all()

        if model_name:
            if model_name not in self.valid_models:
                print('** class doesn\'t exist **')
                return False
            print([str(value) for key, value in storage_data.items()
                   if key.split('.')[0] == model_name])
            return False

        print([str(value) for value in storage_data.values()])

    def do_update(self, args: str):
        """ update [model] [id] [attribute name] [attribute value]
        Updates an instance attribute"""
        args_lst = args.split()

        if len(args_lst) == 0:
            print('** class name missing **')
            return False
        elif len(args_lst) == 1:
            print('** instance id missing **')
            return False
        elif len(args_lst) == 2:
            print('** attribute name missing **')
            return False
        elif len(args_lst) == 3:
            print('** value missing **')
            return False

        model_name, model_id, attr_name, value, *_other = args_lst
        if model_name not in self.valid_models:
            print('** class doesn\'t exist **')
            return False

        model = models.storage.all().get(f'{model_name}.{model_id}')
        if not model:
            print('** no instance found **')
            return False

        if value.startswith('"') and value.endswith('"'):
            value = value.strip('"')
        else:
            value = int(value)

        model.__dict__[attr_name] = value
        model.save()

    def emptyline(self) -> bool:
        return False

    def default(self, line: str):
        args_lst = line.split('.')
        model_name, method, *_other = args_lst

        storage_data = models.storage.all()

        if model_name not in self.valid_models:
            print('** class doesn\'t exist **')
            return False

        if method == 'all()':
            print([str(value) for key, value in storage_data.items()
                if key.split('.')[0] == model_name])
        elif method == 'count()':
            print(sum(1 for key in storage_data
                if key.split('.')[0] == model_name))
        elif 'show' in method:
            model_id = method.split('"')[1]
            self.do_show(f'{model_name} {model_id}')
        elif 'destroy' in method:
            model_id = method.split('"')[1]
            self.do_destroy(f'{model_name} {model_id}')
        elif 'update' in method:
            if '{' in method:
                update_data = method[7:-1].split(',', 1)
                model_id = update_data[0].replace('"', '')
                dict_data = json.loads(
                    update_data[1].replace("'", '"').strip()
                )
                model = models.storage.all().get(f'{model_name}.{model_id}')
                if not model:
                    print('** no instance found **')
                    return False
                model.__dict__.update(dict_data)
                model.save()
            else:
                update_data = method[7:-1].replace(',', '').replace('"', '', 4)

                self.do_update(f'{model_name} {update_data}')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
