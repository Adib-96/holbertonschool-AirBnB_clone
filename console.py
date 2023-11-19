#!/usr/bin/python3
"""
Module containing functionality for
creating a CLI
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Simple command processor"""
    prompt = '(hbnb) '
    classes= ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """Create a new instance"""
        print(self)
        args = line.split(' ')
        if len(line) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        args = line.split(' ')
        if len(line) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else :
            key = "{}.{}".format(args[0], args[1])
            goods = storage.all()
            if key not in goods:
                print("** no instance found **")
            else:
                print(goods)
                print(key)
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
