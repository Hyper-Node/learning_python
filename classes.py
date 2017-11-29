
# ! /usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
This is a script for testing different python3.6/python features
and basic functionality, just to learn python from scratch and by doing.
I intend to stick to the PEP-8 coding guidelines.

This document tests class functionalities.
"""


class MyAnimalClass(object):
    """Klasse um grundsaetzliche funktionatiten zu testen
    """

    _private_member = "this is a private string"

    def __init__(self):
        """Klassenkonstruktor
        """
        print("Init is called with ", self)
        self._animal = ""

    def im_a_zebra2(self):
        """ setzt animal auf zebra2, bekommt self
        """
        self._animal = "zebra2"

    def get_animal(self):
        """beispiel fuer get methode
        """
        return self._animal

    def set_animal(self, value):
        """beispiel fuer set methode
        """
        self._animal = value

    def show_animal_state(self):
        """ logt den animal status
        """
        print("_animal is:", self._animal)

animal = MyAnimalClass()
animal.show_animal_state()
animal.im_a_zebra2()
animal.show_animal_state()
print("Animal get", animal.get_animal())
animal.set_animal("Lion")
print("Animal after set", animal.get_animal())


class MyMammalClass(MyAnimalClass):
    """Klasse um Vererbung zu testen
    """
    
    _info = "mammals are any vertebrates in the class Mammalia"

    def __init__(self):
        MyAnimalClass.__init__(self)
        self._type = "mammal"
             
    def get_type(self):
        """beispiel fuer get methode
        """
        return self._type

    @staticmethod
    def whats_mammals():
        """Test fuer statische methoden
        """

        print("Mammals are any verbrates of some class")


mammal = MyMammalClass()
print("Mammal created with type", mammal.get_type())
mammal.im_a_zebra2()
print("Mammal animal", mammal.get_animal())

# Zugriff auf private variablen geht
print("Mammal privateinfo ", mammal._info)
# Statischer methodentest
mammal.whats_mammals()
MyMammalClass.whats_mammals()
try:
    print("Do non-static methods work", MyMammalClass.get_type())
except Exception as inst:
    print("doesn't work Exception:", inst)


class MyAlternativeAnimalClass(object):
    """Klasse um alternative getter und setter zu testen
    """

    _private_member = "this is a private string"

    def __init__(self):
        """Klassenkonstruktor
        """
        print("Init is called with ", self)
        self._animal = ""

    @property
    def animal(self):
        return self._animal # das ist sozusagen der getter

    @animal.setter
    def animal(self, value):
        self._animal = value # das ist der setter

    def show_animal_state(self):
        """ logt den animal status
        """
        print("_animal is:", self._animal)

penguin = MyAlternativeAnimalClass()
penguin.animal = "penguin"
penguin.show_animal_state()
print("es is wirklich ein", penguin.animal)