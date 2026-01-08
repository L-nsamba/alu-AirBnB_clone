#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter
for the AirBnB clone project. It uses the built-in `cmd` module
to provide a custom interactive shell with specific commands.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implements the command interpreter
    for the AirBnB clone project. It provides custom commands
    such as `quit` and `EOF` to exit, and uses a custom prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Overrides the default behavior of executing the last command
        when an empty line is entered. Here, it does nothing.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command (Ctrl+D) to exit the program.
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
