#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    # ----------- CREATE -----------
    def do_create(self, arg):
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[args[0]]()
        obj.save()
        print(obj.id)

    # ----------- SHOW -----------
    def do_show(self, arg):
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    # ----------- DESTROY -----------
    def do_destroy(self, arg):
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    # ----------- ALL -----------
    def do_all(self, arg):
        args = shlex.split(arg)
        result = []

        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return

        for obj in storage.all().values():
            if len(args) == 0 or obj.__class__.__name__ == args[0]:
                result.append(str(obj))

        print(result)

    # ----------- UPDATE -----------
    def do_update(self, arg):
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr = args[2]
        value = args[3]

        # Cast value properly
        if hasattr(obj, attr):
            try:
                value = type(getattr(obj, attr))(value)
            except Exception:
                pass
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

        setattr(obj, attr, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
