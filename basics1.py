
# ! /usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
This is a script for testing different python3.6/python features
and basic functionality, just to learn python from scratch and by doing.
I intend to stick to the PEP-8 coding guidelines.
"""


import sys

# Print version
print("System Info: ", sys.version_info)


# Die ersten Schritte mit python

def check_array_changes():
    """Ueberprueft referenz oder kopieuebergabe in arrays
    """
    my_test_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print('Das ganze array ', my_test_array)

    my_test_array2 = my_test_array[:3]
    print('Das zweite aus dem ersten Array', my_test_array2)

    my_test_array3 = my_test_array  # Referenzuebergabe

    my_test_array4 = my_test_array[:]  # Kopieuebergabe

    my_test_array2[1] = 'Change'
    my_test_array3[2] = 'Change2'
    my_test_array4[3] = 'Change3'

    print("Array1 nach change", my_test_array)
    print("Array2 nach change", my_test_array2)
    print("Array3 nach change", my_test_array3)
    print("Array4 nach change", my_test_array4)

check_array_changes()

# Variablen und zuweisung


def check_type_assignment():
    """Ueberprueft ob zuweisung typsicherheit hat
    """
    my_type_variable = 123
    print("All ", my_type_variable)
    my_type_variable = "ploetzlich ein string"
    print("All nach change", my_type_variable)

check_type_assignment()

# If bedingungen sind sie true?


def check_how_if_conditions_work():
    """Ueberprueft wie die konditionen mit verschiedenen datentypen funktionieren
    """
    def checkifconditions(index, iftest):
        """Ueberprueft einen einzelnen wert auf true oder false und schreibt in output
        """
        print("T"+str(index)+"\t Iftest is: ", iftest)
        print("T"+str(index)+"\t", iftest is True, iftest is False)
        # pylint: disable=C0121
        print("T"+str(index)+".1\t", iftest == True, iftest == False)

    list_for_iftests = [-1, None, '', 5, 'somelongerstring', True, False]

    for i, element in enumerate(list_for_iftests):
        checkifconditions(i, element)

check_how_if_conditions_work()


# Schauen ob listen als referenz oder kopie übergeben
def check_how_lists_are_passed():
    """Prueft ob listen als referenz oder als kopie uebergeben werden
    """
    ref_test_list = ['re1', 're2']

    def modify_list(list_to_modify):
        """Mache eine kleine aenderung an element 2 der liste
        """
        list_to_modify[1] = 'change'
        print('changed in function ', list_to_modify)

    print('list vor funktionsaufruf ', ref_test_list)
    modify_list(ref_test_list)
    print('list nach funktiosaufruf ', ref_test_list)

    if ref_test_list[1] == 'change':
        print(" listenänderung über referenz")
    else:
        print(" für liste wird in funktion kopie angelegt")

check_how_lists_are_passed()


# Optionale Argumente

def check_optional_args1():
    """Testet optionale eingangsargumente
    """
    def function_with_opts(arg1, *arg2):
        """ eine einfache funktion, die die eingabeargumente ausgiebt
        """
        print("functionWithOpts has ", arg1, arg2)

    function_with_opts(1, 2)
    function_with_opts(1, None)
    function_with_opts(1)
    function_with_opts(1, 2, 3, 4, 5, 6)

check_optional_args1()


def check_optional_args2():
    """Testet optionale eingangsargumente
    """

    def check_kwargs(arg1, **kwarg1):
        """Testet kwargs
        """
        print("functionWithKwargs has ", arg1, kwarg1)
        # if test1 : NameError: name 'test1' is not defined
        #    print("test1 is defined",test1)
        check_test1 = kwarg1['test1']
        print(" check_test1 is ", check_test1)

        # Wege, um die definition zu pruefen
        if isinstance(kwarg1['test1'], str):
            print("test1 is defined in kwarg1", kwarg1['test1'])

        if 'test1' in kwarg1.keys():
            print("test1 is defined in kwarg1", kwarg1['test1'])

        check_test2 = kwarg1.pop('test1')
        array = []
        array.append(check_test2)

        if 'test1' not in kwarg1.keys():
            print("test1 was popped")

    def test_without_kwargs(arg1, arg2, arg3):
        """Funktion ohne kwargs, um alternative Uebergabe mit kwargs zu testen
        """
        print("functionTestWithoutKwargs ", arg1, arg2, arg3)

    check_kwargs("hi", test1="hallo", test2="5")

    my_kwargs = {"arg3": 3, "arg2": "two"}
    test_without_kwargs("hi", **my_kwargs)

check_optional_args2()


# Defaultwerte für eingabeparamter
def check_default_parameters():
    """Teste wie default paramter funktionieren
    """

    def hidden_add(summand1, summand2, summand_hidden=1):
        """Addiere 2-3 Zahlen, wenn dritte nicht definiert, verwende +1
        """
        result = summand1+summand2+summand_hidden
        print("hiddenAdd result is:", result)

    def strange_hidden_add(summand1=1, summand2=1, summand_hidden=1):
        """Addiere 0-3 Zahlen, entweder mit default-werten oder definierten
        """
        result = summand1+summand2+summand_hidden
        print("strangeHiddenAdd result is:", result)

    hidden_add(1, 1)
    hidden_add(1, 1, 2)

    strange_hidden_add(2)


check_default_parameters()


class MyClass:
    """A simple example class"""
    i = 12345

    def some_method(self):
        """just a test method"""
        return 'hello world'


# Formatierung mit printfunktion
def check_print_formatting():
    """Testet unterschiedliche formatierungen
    """

    my_object = MyClass()
    my_decimal_number = 12
    my_floating_number = 34.123456789
    my_tuple_object = (123, 222, 123, "333")

    my_string = "hallo das ist ein text"
    print("str representation if decimal \t", my_decimal_number)
    print("str representation if my_string \t", str(my_string))
    print("repr representation of my_object \t", repr(my_object))
    print("repr representation2 of my_object \t", my_object.__repr__)
    print("str representation of my_object \t", str(my_object))
    print("get documentation of my_object \t", my_object.__doc__)
    print("get documentation of my_tuple_object \t", my_tuple_object)
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other= 'Georg'))
    print('My floating point number is  {0:.3f}.'.format(my_floating_number))
    print('My floating point number is  {0:.6f}.'.format(my_floating_number))

check_print_formatting()