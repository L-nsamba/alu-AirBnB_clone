#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


# Map of allowed classes
classes = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    # ---------- Basic behavior ----------
    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    # ---------- CREATE ----------
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

    # ---------- SHOW ----------
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

        key = f"{args[0]}.{args[1]}"
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        print(objs[key])

    # ---------- DESTROY ----------
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

        key = f"{args[0]}.{args[1]}"
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        del objs[key]
        storage.save()

    # ---------- ALL ----------
    def do_all(self, arg):
        args = shlex.split(arg)
        objs = storage.all()
        result = []

        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return

        for obj in objs.values():
            if len(args) == 0 or obj.__class__.__name__ == args[0]:
                result.append(str(obj))

        print(result)

    # ---------- UPDATE ----------
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

        key = f"{args[0]}.{args[1]}"
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objs[key]
        attr_name = args[2]
        value = args[3]

        # Cast value to correct type if attribute exists
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                value = attr_type(value)
            except Exception:
                pass

        setattr(obj, attr_name, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
