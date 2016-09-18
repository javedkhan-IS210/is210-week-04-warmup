#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Figuring out if we have enough litterboxes and catfood"""


def too_many_kittens(kittens, litterboxes, catfood)
    """This checks if we have litterboxes and catfood for all kittens.

    Args:
        kittens(int): the number of kittens
        litterboxes(int): the number of available litterboxes
        catfood(bool): representing whether or not catfoof exists

    Returns:
        bool: If the number of kittens is more than the available litterboxes
         and catfood, return False. If not return True'

    Example:
        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 14, True)
        False

    """"

return not (litterboxes >= kittens and catfood)
