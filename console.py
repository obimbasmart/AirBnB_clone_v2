#!/usr/bin/env python3

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
import re
from models.state import State
from models.user import User

from pprint import pprint as pp


class HBNBCommand(cmd.Cmd):
    '''HBNB command line interpreter'''

    intro = ''
    prompt = '(hbnb) '
    original_input = ''

    def do_create(self, args):
        '''Creates a new instance of "arg"'''
        tokens = tokenize(args)
        if error_in_command(parse(args), 'create'):
            return

        new_obj = globals()[tokens['class']](**tokens['params'])
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
        print(args)
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
        print(args)
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
                   if class_name in key]))

    def do_BaseModel(self, args):
        """BaseModel.command(<argument>) := perform command on BaseModel class
        using the arguments"""
        self.__perform_advanced_command('BaseModel', args)

    def do_User(self, args):
        """BaseModel.command(<argument>) := perform command on BaseModel class
        using the arguments"""
        self.__perform_advanced_command('User', args)

    def do_Place(self, args):
        """Place.command(<argument>) := perform command on Place class
        using the arguments"""
        self.__perform_advanced_command('Place', args)

    def do_City(self, args):
        """City.command(<argument>) := perform command on City class
        using the arguments"""
        self.__perform_advanced_command('City', args)

    def do_Amenity(self, args):
        """Amenity.command(<argument>) := perform command on Amenity class
        using the arguments"""
        self.__perform_advanced_command('Amenity', args)

    def do_State(self, args):
        """State.command(<argument>) := perform command on State class
        using the arguments"""
        self.__perform_advanced_command('State', args)

    def do_Review(self, args):
        """Review.command(<argument>) := perform command on Review class
        using the arguments"""
        self.__perform_advanced_command('Review', args)

    do_EOF = do_quit

    def __perform_advanced_command(self, klass, args):
        """helper function for advanced commands"""

        commands = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        arg_list = args.replace(".", ' ').replace('(', " "). \
            replace(')', "").split()
        command = arg_list[0]
        print(arg_list)
        # print(command)

        if command in commands:
            if command in "all | count":
                commands[command](klass)
            elif command in "destroy | show":
                commands[command](klass + ' ' + arg_list[1])
            else:
                input_string = klass + ' ' + args
                match = re.search(r'({.*?})', input_string)
                if match:
                    print(match.group(1))
                    obj_dict = eval(match.group(1))
                    print(obj_dict)
                    for attr, val in obj_dict.items():
                        commands[command](
                            klass + ' ' + arg_list[1].replace(',', '') +
                            ' ' + attr + ' ' + str(val))
                else:
                    commands[command](
                        klass + ' ' + ' '.join(arg_list[1:]).replace(',', ''))


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


def tokenize(args):
    """convert input string into tokens
    return a dictionary of class_name and parameters"""
    arg_list = args.split(' ')
    params = {item.split('=')[0]: item.split("=")[1] for item in arg_list[1:]}
    params = {key: int(val) if all(char not in val for char in '".-')
              else float(val) if '"' not in val and "." in val
              else val.replace('_', ' ') if '_' in val
              else val for key, val in params.items()}
    tokens = {'class': arg_list[0], 'params': params}
    return tokens


if __name__ == '__main__':
    HBNBCommand().cmdloop()
