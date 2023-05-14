#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd
import shlex
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '
    classes = ["BaseModel"]

    valid_classes = ["BaseModel", "User"]  # Add User to the valid_classes list


    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        args = shlex.split(arg)
        if arg in self.valid_classes:
            new_object = eval(arg)()  # Create a new object of the specified class
            new_object.save()
            print(new_object.id)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                models.storage.save()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        objects = storage.all()
        if arg and arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            if arg:
                filtered_objs = {k: v for k, v in objects.items() if arg in k}
                print([str(v) for v in filtered_objs.values()])
            else:
                print([str(v) for v in objects.values()])
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            class_objects = [str(obj) for obj in objects.values() if type(obj).__name__ == args[0]]
            print(class_objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) < 3:
            print("** instance id missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                setattr(obj, args[2], args[3])
                obj.save()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args)
