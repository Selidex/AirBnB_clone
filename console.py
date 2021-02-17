#!/usr/bin/python3
"""console"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """class for console"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing"""
        pass

    def do_quit(self, args):
        """Quit to exit"""
        return True

    def do_EOF(self, args):
        """EOF to exit"""
        pass
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, and saves it"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            func = models.class_dict[x[0]]
            temp = func()
            temp.save()
            print(temp.id)

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exits **")
        elif len(x) < 2:
            print("** instance id missing **")
        else:
            sdict = models.storage.all()
            fb = 0
            for y in sdict:
                z = y.split(".")
                if z[0] == x[0]:
                    if z[1] == x[1]:
                        fb = 1
                        print(sdict[y])
            if fb == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exits **")
        elif len(x) < 2:
            print("** instance id missing **")
        else:
            sdict = models.storage.all()
            fb = 0
            for y in sdict:
                z = y.split(".")
                if z[0] == x[0]:
                    if z[1] == x[1]:
                        fb = 1
                        var = y
            if fb == 1:
                del sdict[var]
                models.storage.save()
            if fb == 0:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name"""
        pdict = models.storage.all()
        if args == "" or args is None:
            lc = []
            for key in pdict:
                lc.append(str(pdict[key]))
            print(lc)
        else:
            x = args.split()
            if x[0] not in models.class_dict:
                print("** class doesn't exits **")
            else:
                lc = []
                for key in pdict:
                    z = key.split(".")
                    if z[0] == x[0]:
                        lc.append(str(pdict[key]))
                print(lc)

    def do_update(self, args):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exits **")
        elif len(x) < 2:
            print("** instance id missing **")
        elif len(x) < 3:
            print("** attribute name missing **")
        elif len(x) < 4:
            print("** value missing **")
        else:
            sdict = models.storage.all()
            fb = 0

            str_cat = x[3]
            if not x[3].endswith('"'):
                for i in range(4, len(x)):
                    str_cat += " " + x[i]
                    if x[i].endswith('"'):
                        break
            if not str_cat.endswith('"'):
                print("** value missing **")
                return
            str_cat = str_cat.split('"')

            for y in sdict:
                z = y.split(".")
                if z[0] == x[0]:
                    if z[1] == x[1]:
                        fb = 1
                        var = y
            if fb == 1:
                var2 = x[2]
                sdict[var].__dict__[var2] = str_cat[1]
                models.storage.save()
            if fb == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()