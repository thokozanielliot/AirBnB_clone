#!/usr/bin/python3
"""Define the HBnB Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Represent the HBnB command interpreter"""
    
    prompt = "(hbnb)"

    def emptyline(self):
        """Shouldn't execute anything upon recieving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
