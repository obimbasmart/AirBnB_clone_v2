#!/usr/bin/python3

'''
Module contains entry point of the console which serves
as the command line interpreter for managing Objects
'''

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
import cmd
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''HBNB command line interpreter'''

    intro = ''
    prompt = '(hbnb) '
    original_input = ''

    def do_create(self, arg):
        '''Creates a new instance of "arg"'''
        if error_in_command(parse(arg), 'create'):
            return

        new_obj = globals()[arg]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, args):
        '''Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234'''

        args = parse(args)
        if (error_in_command(args, 'show')):
            return

        key = '.'.join(args)
        if (storage.all().get(key)):
            print(globals()[args[0]](**storage.all()[key]))

        else:
            print('** no instance found **')

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id'''
        if (error_in_command(parse(args), 'destroy')):
            return

        key = '.'.join(parse(args))
        if (storage.all().pop(key, None)):
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, args):
        ''' Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel'''

        if not args:
            all_objects = [globals()[val['__class__']](**val)
                           for key, val in storage.all().items()]
            print([str(obj) for obj in all_objects])
            return

        if error_in_command(parse(args), 'all'):
            return

        all_obj_in_class = [globals()[val['__class__']](**val)
                            for key, val in storage.all().items()
                            if val['__class__'] == args]
        print([str(obj) for obj in all_obj_in_class])

    def do_update(self, args):
        '''Updates an instance based on the class name and id by
        adding or updating attribute'''

        if error_in_command(parse(args), 'update'):
            return

        args = parse(args)
        key = '.'.join(args[:2])
        obj_dict = storage.all().get(key, None)

        if (not obj_dict):  # no object found
            print('** no instance found **')
            return

        updated_obj = globals()[args[0]](**obj_dict)
        setattr(updated_obj, args[2], args[3])
        updated_obj.save()

    # def do_class(self, args):
    #     """enable command usage using dot notation
    #     E.g: show User <id> = User.show(<id>)
    #          User.count() - return number of instance of class User
    #     """
    # args = HBNBCommand.original_input.replace('.', ' ').replace('(', ' ') \
    #         .replace(')', '').replace('"', '').replace(',', '').split()

    #     class_name = args[0]
    #     action = args[1]
    #     match action:
    #         case 'all':
    #             self.do_all(class_name)
    #         case 'count':
    #             self.count(class_name)
    #         case 'show':
    #             self.do_show(class_name + ' ' + args[2])
    #         case 'destroy':
    #             self.do_destroy(class_name + ' ' + args[2])
    #         case 'update':
    #             self.do_update(
    #                 ' '.join([class_name, args[2], args[3], args[4]]))

    def do_quit(self, arg):
        '''Quit command to exit the program\n'''
        quit()

    def precmd(self, line: str) -> str:
        """return original command line input before cmd_line manipulation"""
        HBNBCommand.original_input = line
        return line

    def emptyline(self):
        """empty line should do nothing"""
        pass

    def count(self, class_name):
        '''retrieve the number of instances of a class'''
        print(len([obj for key, obj in storage.all().items()
              if obj['__class__'] == class_name]))

    do_EOF = do_quit
    # do_BaseModel = do_Place = do_City = do_User = do_class
    # do_Review = do_Amenity = do_State = do_class


def parse(arg):
    'Convert a series of args (strings) to a list of strings'
    return arg.split()


def error_in_command(args, command):
    '''handle errors in command. return True if error
    exist in command, False if no error is found
    '''

    valid_class_names = ['BaseModel', 'User',
                         'Place', 'State', 'City', 'Amenity', 'Review']

    if not args and command != 'all':
        print('** class name missing **')
        return True

    elif args[0] not in valid_class_names:
        print("** class doesn't exist **")
        return True

    elif len(args) < 2 and command not in 'all | create':
        print('** instance id missing **')
        return True

    elif len(args) < 3 and command in 'update':
        print('** attribute name missing **')
        return True

    elif len(args) < 4 and command in 'update':
        print('** value missing **')
        return True

    return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
