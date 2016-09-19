#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This tests the values of two parameters within a function"""

def defaults(my_optional=True, my_reqired)
    """ This function tests whether or not the parameters aare the same.

    Args:
        my_optional(bool): This parameter has a default value of True.
        my_required(mixed): This parameter has no default value.

    Returns:
        bool: returns a logical comparison of the two parameters.

     Examples:
         >>> defaults (True, True)
         True

         >>> defaults (Fals, True)
         False

   """
return my_optional is my_required
