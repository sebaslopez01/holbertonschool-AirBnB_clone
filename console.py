#!/usr/bin/python3

"""

This module defines a HBNBCommand Class

"""

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

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
        if model_name != 'BaseModel':
            print('class doesn\'t exist')
            return False

        bm = BaseModel()
        bm.save()

        print(bm.id)

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

        model_name, model_id = args_lst
        if model_name != 'BaseModel':
            print('class doesn\'t exist')
            return False

        bm = models.storage.all().get(f'{model_name}.{model_id}')
        if not bm:
            print('** no instance found **')
            return False

        print(bm)

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

        model_name, model_id = args_lst
        if model_name != 'BaseModel':
            print('class doesn\'t exist')
            return False

        bm = models.storage.all().get(f'{model_name}.{model_id}')
        if not bm:
            print('** no instance found **')
            return False

        del models.storage.all()[f'{model_name}.{model_id}']
        models.storage.save()

    def do_all(self, model_name: str):
        """ all [model]
        Shows all string representation of all instances in storage"""
        storage_data = models.storage.all()

        if model_name:
            if model_name != 'BaseModel':
                print('class doesn\'t exist')
                return False
            print([str(value) for key, value in storage_data.items()
                   if key.split('.')[0] == model_name])
            return False

        print([str(value) for value in storage_data.values()])

    def do_update(self, args: str):
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

        model_name, model_id, attr_name, value = args_lst
        if model_name != 'BaseModel':
            print('class doesn\'t exist')
            return False

        bm = models.storage.all().get(f'{model_name}.{model_id}')
        if not bm:
            print('** no instance found **')
            return False

        if value.startswith('"') and value.endswith('"'):
            value = value.strip('"')
        else:
            value = int(value)

        bm.__dict__[attr_name] = value
        bm.save()

    def emptyline(self) -> bool:
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
