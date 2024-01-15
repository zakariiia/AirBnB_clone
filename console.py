#!/usr/bin/python3
"""This file manage all required implentation for a simple AirBNB console."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand console."""

    prompt = "(hbnb)"
    classes = ["BaseModel", "State", "Place", "Amenity", "City", "Review", "User"]

    def do_help(self, arg):
        """Give help instructions."""
        return super().do_help(arg)

    def do_quit(self, arg):
        """Exit the program when quit is entred."""
        return True

    def emptyline(self):
        """Nothing to do when an empty line is entered."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, arg):
        """Create."""
        cmd = arg.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            clss = eval(f'{cmd[0]}()')
            print(clss.id)
            storage.save()

    def do_show(self, arg):
        """Do show."""
        cmd = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif cmd[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = f"{cmd[0]}.{cmd[1]}"
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Do all."""
        cmnd = arg.split()
        objs = storage.all()
        if len(cmnd) == 0:
            for key, value in objs.items():
                print(str(value))
        elif cmnd[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split(".")[0] == cmnd[0]:
                    print(str(value))

    def do_destroy(self, arg):
        """Destroy inst."""
        objs = storage.all()
        cmnd = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif cmnd[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(cmnd) < 2:
            print("** instance id missing **")
        else:
            key = f"{cmnd[0]}.{cmnd[1]}"
            if key in objs.keys():
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update."""
        objs = storage.all()
        cmnd = arg.split()
        try: 
            cmnd[0] = cmnd[0].split('\'')[1]
        except Exception:
            pass
        try:
            cmnd[3] = cmnd[3].split('\"')[1]
        except Exception:
            pass
        if len(arg) == 0:
            print("** class name missing **")
        elif cmnd[0] not in self.classes:
            print(f"** class doesn't exist **")
        elif len(cmnd) < 2:
            print("** instance id missing **")
        else:
            key = f"{cmnd[0]}.{cmnd[1]}"
            if key not in objs.keys():
                print("** no instance found **")
            elif len(cmnd) < 3:
                print("** attribute name missing **")
            elif len(cmnd) < 4:
                print("** value missing **")
            else:
                obj = objs[key]
                setattr(obj, cmnd[2], cmnd[3])
                storage.save()

    def do_count(self, line):
        """Count and retrieve the number of instances of a class.

        usage: <class name>.count()
        """
        objs = storage.all()

        cmnd = shlex.split(line)

        if line:
            cls_nmme = cmnd[0]

        count = 0

        if cmnd:
            if cls_nmme in self.classes:
                for obj in objs.values():
                    if obj.__class__.__name__ == cls_nmme:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def split_cu_brac(self, line):
        """Split the curly braces for the update method."""
        list_cmnd = line.split(",")
        if len(list_cmnd) == 0:
            print("** instance id missing **")
        elif len(list_cmnd) < 2:
            print("** attribute name missing **")
        elif len(list_cmnd) < 3:
            print("** value missing **")
        else:
            cls_id = list_cmnd[0]
            cls_att = list_cmnd[1]
            cls_value = list_cmnd[2]
            return f"{cls_id[1:-1]} {cls_att[2:-1]} {cls_value}"
        


    def default(self, line):
        """DEf."""
        line_list = line.split('.')

        cls_nm = line_list[0]

        cmnd = line_list[1].split('(')

        cmnd_met = cmnd[0]

        e_line = cmnd[1].split(')')[0]

        cls_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmnd_met in cls_dict.keys():
            if cmnd_met != "update":
                ee_line = e_line[1:-1]
                return cls_dict[cmnd_met](f"{cls_nm} {ee_line}")
            else:
                if not cls_nm:
                    print("** class name missing **")
                    return
                try:
                    arg_update = self.split_cu_brac(e_line)
                except Exception:
                    pass
                try:
                    execu = self.do_update("{} {}".format(cls_nm, arg_update))
                    return execu
                except Exception:
                    pass
        else:
            print("*** Unknownddd syntax: {}".format(line))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
