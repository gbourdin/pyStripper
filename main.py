#!/usr/bin/env python
# coding=utf-8

#    pyStripper is an open-source nfo stripper written in python
#
#    Copyright (C) 2012  German Bourdin - James Baumeister
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from argparse import ArgumentParser
from NFOStripper import NFOStripper
import os
import sys
import config


def is_readable(path):
    """ Checks if a file is readable """
    return os.access(path, os.R_OK)


def is_writeable(path):
    """ Checks if a file is writeable """
    return os.access(path, os.W_OK)


def main():

    parser = ArgumentParser()

    parser.add_argument("-o", "--output", default=config.OUTPUT_FILE,
                        help="Specify an output file")
    parser.add_argument("-i", "--input", default=config.INPUT_FILE,
                        help="Specify an input file")
    parser.add_argument("-p", "--pre", action="store_true",
                        help="Use this flag if you want [pre] [/pre]"
                        " tags added")
    parser.add_argument("-d", "--dontstrip", action="store_true",
                        help="Use this flag to prevent ascii"
                        " from being stripped")
    parser.add_argument("--promo", default=None,
                        help="Specify a text to add at the end of the "
                             "stripped text")

    args = parser.parse_args()

    if args.input != None:
        args.input = os.path.abspath(args.input)

        if not os.path.isfile(args.input) or not is_readable(args.input):
            sys.stderr.write("Could not open {0}\n".format(args.input))
            sys.exit(1)

        # Check Filesize!
        if os.path.getsize(args.input) > config.FILE_MAX_SIZE:
            sys.stderr.write("Input file exceeds file max size\n")
            sys.exit(1)

        config.INPUT_FILE = args.input

    if args.output != None:
        args.output = os.path.abspath(args.output)

        if os.path.isfile(args.output) and not is_writeable(args.output):
            sys.stderr.write("Could not open {0}\n".format(args.output))
            sys.exit(1)
        if os.path.isdir(args.output):
            sys.stderr.write("You must specify a filename\n")
            sys.exit(1)

        # Crete the output file (if it doesn't exist)
        try:
            open(args.output, 'w')
        except(IOError):
            sys.stderr.write("Could not create/open {0}\n".format(args.output))
            sys.exit(1)

        config.OUTPUT_FILE = args.output

    if args.pre:
        config.PRE = True

    if args.dontstrip:
        config.STRIP = False

    if args.promo != None:
        config.PROMO = True
        config.PROMO_TEXT = args.promo

    # Here's where the magic happens:
    # Create new stripper.
    stripper = NFOStripper()

    # Strip all the ascii
    stripper.strip()

    # Write the output
    stripper.write_output()


if __name__ == '__main__':
    main()
