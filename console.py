#!/usr/bin/python3
"""
This module defines the command interpreter for the AirBnB clone project.
It provides commands to create, show, destroy, list, and update instances.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel

# Dictionary of available classes
classes = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implements the command interpreter
    for the AirBnB clone project.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command (Ctrl+D) to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = shlex.split(arg)
        objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objects.items()
                   if key.startswith(args[0] + ".")])

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        # Cast value to correct type
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            else:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
        except Exception:
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
