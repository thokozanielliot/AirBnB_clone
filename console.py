#!/usr/bin/python3
"""Define the HBnB Console"""
import cmd
from shlex import split
from models import storage


class HBNBCommand(cmd.Cmd):
    """Represent the HBnB command interpreter"""

    prompt = "(hbnb)"
    allClasses = {
        "BaseModel",
        "User",
        "Amenity",
        "Place",
        "City",
        "Review",
        "State"
    }

    def emptyline(self):
        """Shouldn't execute anything upon recieving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        print("Exit the program")

    def help_quit(self):
        print("Quit the program")


    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to
        JSON file & print the id
        Usage: create <class>
        Exceptions:
            SyntaxError: When there is no args given
            NameError: When there is no object that has the name
        """
        try:
            if not arg:
                raise SyntaxError()
            myList = arg.split(" ")
            obj = eval("{}()".format(myList[0]))
            print("{}".format(obj.id))
            for number in range(1, len(myList)):
                myList[number] = myList[number].replace("=", " ")
                attributes = split(myList[number])
                attributes[1] = attributes[1].replace("_", " ")

                try:
                    var = eval(attributes[1])
                    attributes[1] = var
                except Exception:
                    pass

                if type(attributes[1]) is not tuple:
                    setattr(obj, attributes[0], attributes[1])
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the classs name & id
        Usage: show <class> <class.id>
        Exceptions:
            SyntaxError: When there are no args given
            NameError: When there is no object that has the name
            IndexError: When there is no id given
            KeyError: When there is no valid id given
        """
        try:
            if not arg:
                raise SyntaxError()
            myList = arg.split(" ")
            if myList[0] not in self.allClasses:
                raise NameError()
            if len(myList) < 2:
                raise IndexError()
            obj = storage.all()
            key = myList[0] + "." + myList[1]
            if key in obj:
                print(obj[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instances found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name & id
        (save the changes into JSON file)
        Usage: destroy <class> <class.id>
        Exceptions:
            SynataxError: When there is no args given
            NameError: When there is no object that has the name
            IndexError: When there is no id given
            KeyError: When there is no valid id given
        """
        try:
            if not arg:
                raise SyntaxError()
            myList = arg.split(" ")
            if myList[0] not in self.allClasses:
                raise NameError()
            if len(myList) < 2:
                raise IndexError()
            obj = storage.all()
            key = myList[0] + "." + myList[1]
            if key in obj:
                del obj[key]
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instances found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the same class name
        Usage: all <class>
        Exceptions:
            NameError: when there is no object that has the name
        """
        objects = storage.all()
        myList = []
        if not arg:
            for key in objects:
                myList.append(objects[key])
            print(myList)
            return
        try:
            args = arg.split(" ")
            if args[0] not in self.allClasses:
                raise NameError()
            for key in objects:
                name = key.split(".")
                if name[0] == args[0]:
                    myList.append(objects[key])
            print(myList)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name & id
        by adding or updating attribute (save changes into JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Exceptions:
            SynataxError: When there is no args given
            NameError: When there is no object that has the name
            IndexError: When there is no id given
            KeyError: When there is no valid id given
            AttributeError: When ther is no attribute given
            ValueError: When there is no value given
        """
        try:
            if not arg:
                raise SyntaxError()
            myList = arg.split(" ")
            if myList[0] not in self.allClasses:
                raise NameError()
            if len(myList) < 2:
                raise IndexError()
            obj = storage.all()
            key = myList[0] + "." + myList[1]
            if key not in obj:
                raise KeyError()
            if len(myList) < 3:
                raise AttributeError()
            if len(myList) < 4:
                raise ValueError()

            var = obj[key]
            try:
                var.__dict__[myList[2]] = eval(myList[3])
            except Exception:
                var.__dict__[myList[2]] = myList[3]
                var.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instances found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def strip_clean(self, args):
        """
        Strips the arguement & returns the command
        """
        newList = []
        newList.append(args[0])
        try:
            myDict = eval(args[1][args[1].find("{"):args[1].find("}")+1])
        except Exception:
            myDict = None
        if isinstance(myDict, dict):
            newStr = args[1][args[1].find("(")+1:args[1].find(")")]
            newList.append(((newStr.split(","))[0]).strip('"'))
            newList.append(myDict)
            return newList
        newStr = args[1][args[1].find("(")+1:args[1].find(")")]
        newList.append(" ".join(newStr.split(", ")))
        return " ".join(i for i in newList)
    
    def count(self, arg):
        """
        Count the instances of a class
        """
        count = 0
        try:
            myList = split(arg, " ")
            if myList[0] not in self.allClasses:
                raise NameError()
            objs = storage.all()
            for key in objs:
                name = key.split(".")
                if name[0] == myList[0]:
                    count += 1
            print(count)
        except NameError:
            print("** class doesn't exist **")
    def default(self, arg):
        """
        Retrive all instances of a class & number of instances
        """
        myList = arg.split(".")
        if len(myList) >= 2:
            if myList[1] == "all()":
                self.do_all(myList[0])
            elif myList[1] == "count()":
                self.count(myList[0])
            elif myList[1][:4] == "show":
                self.do_show(self.strip_clean(myList))
            elif myList[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(myList))
            elif myList[1][:6] == "update":
                args = self.strip_clean(myList)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + " " + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + '"{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
