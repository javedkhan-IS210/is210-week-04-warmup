#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """A function that knows what you mean
    
    Args:
         wink (mixed):Arg to be arthmatically incremented to numwink.
         numwink (mixed):Arg to increment wink. Default: 2.
         winks optional(str): Arg to be multiplied by numwink and stripped of
         no characters. 
         nudges optional(str):Arg to muliply 'nudge' by numwink and stripped of
         no characters.
         retstr optional(str): Arg to concatenate optional parameters with a
         string and comma,then inserts winks and nudges. 
    Returns:
         str: concatenates all three arguments with commas  winks and
         nudges multiplied by numwink value.

    Examples:
         >>>>know_what_i_mean'
         'Know what I mean>? wink wink, nudge nudge' 
    
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr

