# ! /usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Shows possibilities how to write decorators (wrappers for fornctions)
"""

from functools import wraps


def get_text(name):
    """Dies ist die base-methode
    """
    return "lorem ipsum, {0} dolor sit amet".format(name)


def div_decorate(func):
    """Dies ist eine weitere decorator methode
    """

    def func_wrapper(name):
        """Diese methode umschliesst die uebergebene methode mit func
        """
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


def p_decorate(func):
    """Dies ist die decorator methode
    """
    def func_wrapper(name):
        """Diese methode umschliesst die uebergebene methode mit func
        """
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


@p_decorate
def decorated_get_text(name):
    """Dies ist die base-methode versehen mit einem decorator
    """
    return "lorem ipsum, {0} dolor sit amet".format(name)


@div_decorate
@p_decorate
def multi_decorated_get_text(name):
    """Dies ist die base-methode versehen mit mehreren decorators
       Wrapping erfolgt nach reihenfolge der decoratoren
    """
    return "lorem ipsum, {0} dolor sit amet".format(name)


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


def p_decorate_functools(func):
    """Dies ist die decorator methode
    """

    @wraps(func)
    def func_wrapper(name):
        """Diese methode umschliesst die uebergebene methode mit func
        """
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


@p_decorate_functools
def functools_decorated_get_text(name):
    """Dies ist die base-methode versehen mit functools decorator
       Wrapping erfolgt nach reihenfolge der decoratoren
    """
    return "lorem ipsum, {0} dolor sit amet".format(name)


@tags("my_tag")
def parameter_decorated_get_text(name):
    """Dies ist die base-methode versehen mit parameter
       Wrapping erfolgt nach reihenfolge der decoratoren
    """
    return "lorem ipsum, {0} dolor sit amet".format(name)
# Erste moeglichkeit decorator zu verwenden

my_get_text = p_decorate(get_text)
print(my_get_text("John"))

# Zweite moeglichkeit decorator zu verwenden

print(decorated_get_text("Johannes"))

# Mehrere decorators
print(multi_decorated_get_text("Julia"))

# Decorater mit parameter
print(parameter_decorated_get_text("Test"))

# Decorater mit functools
print(functools_decorated_get_text("Julien"))
