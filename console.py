#!/usr/bin/python3
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
import re
import ast





class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console
    """
    prompt = "(hbnb)"
    classes = ["BaseModel", "State", "Place", "Amenity",
                "City", "Review", "User"]

    def do_help(self, arg):
        return super().do_help(arg)
    
    def do_quit(self, arg):
        """
        exit the program when quit is entred
        """
        return True
    
    def emptyline(self):
        """
        nothing to do when an empty line is entered
        """
        pass

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        return True
    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
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
        """
         Prints the string representation of an instance based on the class name and id
        """
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
    def do_all(self,arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
        """
        cmnd =arg.split()
        objs = storage.all()
        if len(cmnd) == 0:
            for key , value in objs.items():
                print(str(value))
        elif cmnd[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else :
            for key , value in objs.items():
                if key.split(".")[0] == cmnd[0]:
                    print(str(value))

    def do_destroy(self, arg):
        """
        Delete an instance using on the class name and id as arg.
        Usage: destroy <class_name> <id>
        """
        objs = storage.all()
        cmnd = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif cmnd[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(cmnd) < 2:
            print("** instance id missing **")
        else :
            key =f"{cmnd[0]}.{cmnd[1]}"
            if key in objs.keys():
                del objs[key]
                storage.save()
            else :
                print("** no instance found **")
                
    def do_update(self,arg):
        """
        Update an instance by adding or changing an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        objs = storage.all()
        cmnd = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif cmnd[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmnd) < 2:
            print("** instance id missing **")
        else :
            key = f"{cmnd[0]}.{cmnd[1]}"
            if key not in objs.keys():
                print("** no instance found **")
            elif len(cmnd) < 3:
                print("** attribute name missing **")
            elif len(cmnd) < 4:
                print("** value missing **")
            else :
                obj = objs[key]
                setattr(obj, cmnd[2], cmnd[3])
                storage.save()
                # attrb_name = cmnd[1]
    def do_count(self, line):
        """
        Counts and retrieves the number of instances of a class
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

    def split_cu_brac(line):
        """
        Split the curly braces.
        """
        c_brace = re.search(r"\{(.*?)\}", line)

        if c_brace:
            id_with_comma = shlex.split(line[:c_brace.span()[0]])
            id = [i.strip(",") for i in id_with_comma][0]

            string_data = c_brace.group(1)
            try:
                line_dict = ast.literal_eval("{" + string_data + "}")
            except Exception:
                print("**  invalid dictionary format **")
                return
            return id, line_dict
        else:
            cmnd = line.split(",")
            if cmnd:
                try:
                    id = cmnd[0]
                except Exception:
                    return "", ""
                try:
                    attr_nm = cmnd[1]
                except Exception:
                    return id, ""
                try:
                    attr_val = cmnd[2]
                except Exception:
                    return id, attr_nm
                return f"{id}", f"{attr_nm} {attr_val}"
        
    
    def default(self, line):
        """
        Default behavior for cmd
        """
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
                    obj_id, line_dict = self.split_cu_brac(e_line)
                    print(obj_id, line_dict)
                except Exception:
                    pass
                try:
                    execu = cls_dict[cmnd_met]
                    return execu("{} {} {}".format(cls_nm, obj_id, line_dict))
                except Exception:
                    pass
        else:
            print("*** Unknownddd syntax: {}".format(line))
            return False

   

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    

