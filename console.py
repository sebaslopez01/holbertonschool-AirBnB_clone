#!/usr/bin/python3

"""

This module defines a HBNBCommand Class

"""

import cmd


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

    def emptyline(self) -> bool:
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
