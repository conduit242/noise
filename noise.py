#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#
# Copyright 2014 Robert Bird
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# noise.py
# Version 0.1
# A simple program for adding random normal noise to values of a csv


from sys import stdin
import argparse
import random


def add_noise(a, s):
    a = [float(x) for x in a.split(',')]
    for x in xrange(len(a)):
        a[x] = random.gauss(a[x], s)
    return ",".join(map(str, a))


def add_noise_ignore_zeros(a, s):
    a = [float(x) for x in a.split(',')]
    for x in xrange(len(a)):
        if a[x] != 0:
            a[x] = random.gauss(a[x], s)
    return ",".join(map(str, a))



parser = argparse.ArgumentParser()

parser.add_argument(
    '-z',
    action='store_true',
    dest='perturb_zeros',
    default=False,
    help='Perturb zeros; default=False',
    )

parser.add_argument(
    '-s',
    action='store',
    dest='sigma',
    default=0.25,
    type=float,
    help='Set sigma; default=0.25',
    )

args = vars(parser.parse_args())
sigma = args['sigma']

if args['perturb_zeros']:
    for line in stdin:
        print add_noise(line, sigma)
else:
    for line in stdin:
        print add_noise_ignore_zeros(line, sigma)


