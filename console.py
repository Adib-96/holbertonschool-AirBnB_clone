#!/usr/bin/python3
"""
Module containing functionality for
creating a CLI
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
