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
            print(storage.all()[key])

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
        or not on the class name. Ex: $ all BaseModel
        '''

        if not args:
            print([str(obj) for obj in storage.all().values()])
            return

        if error_in_command(parse(args), 'all'):
            return

        all_obj_in_class = [obj for obj in storage.all().values()
                            if obj.to_dict()['__class__'] == args]
        print([str(obj) for obj in all_obj_in_class])

    def do_update(self, args):
        '''Updates an instance based on the class name and id by
        adding or updating attribute'''

        if error_in_command(parse(args), 'update'):
            return

        args = parse(args)
        key = '.'.join(args[:2])
        obj = storage.all().get(key, None)

        if (not obj):  # no object found
            print('** no instance found **')
            return

        setattr(obj, args[2], args[3])
        obj.save()

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

    def help_class(self):
        """help for commands with dot notation"""
        print("Use dot notation e.g: User.all() => all Users")

    do_EOF = do_quit


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
