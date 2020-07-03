#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "LeanneBenson"

import cProfile
import pstats
import functools
import timeit
import collections


def timeit_helper():
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    time = t.repeat(repeat=7, number=5)
    print("Minimum of Average Performances: {}".format(min(time) / 5))

def profile(func):
    @functools.wraps(func)
    def profiler(*args, **kwargs):
        cp = cProfile.Profile()
        cp.enable()
        result = func(*args, **kwargs)
        cp.disable()
        sortby = 'cumulative'
        ps = pstats.Stats(cp).sort_stats(sortby)
        ps.print_stats()
        return result
    return profiler

def read_movies(src):
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()

def is_duplicate(title, movies):
    """Needs Space; @Profile needs social distaaaanncccingggggg LOL"""
@profile

def find_duplicate_movies(src):
    movies = read_movies(src)
    return [movie for movie, count in collections.Counter(movies).items() if count > 1]


def main():
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
