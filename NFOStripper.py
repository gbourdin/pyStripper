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

import config
import sys
import re
from nfo_tricks import nfo_tricks

EXTRA_SPACES = re.compile('  +')  # This doesn't include \t and that's fine
BEGINS_WITH_SPACES = re.compile('^( +|\t+)', re.M)
INLINE_REPETITIONS = re.compile('(.)(\\1{4,})')
VERTICAL_REPETITIONS_A = re.compile(
    r'(^[^\[^\]^\n^\r-])' + '(.*)(\n)+((\\1(.*)(\n)+){4,})', re.M)
VERTICAL_REPETITIONS_B = re.compile(
    r'([^\[^\]^\n^\r-]$)(\n)+' + '((.*)\\1(\n)+){4,}', re.M)
BLANKLINES = re.compile('^(\r*\n){2,}', re.M)
PRE_TAGS = re.compile(r'\[/?pre\s*\]')


class NFOStripper(object):

    def __init__(self):

        if config.INPUT_FILE:
            try:
                input_stream = open(config.INPUT_FILE, 'r')
            except IOError:
                sys.exit(1)
        else:
            input_stream = sys.stdin

        self.data = input_stream.read(config.FILE_MAX_SIZE)  # Read at most 1MB

        if config.INPUT_FILE:  # Careful do not close stdin!
            input_stream.close()

    def strip(self):

        if config.STRIP:

            # For groups using ascii to mark stuff instead of X.
            self.data = re.sub('[\xc2\x95]', 'X', self.data)

            # Run the tricks to get rid of more complex ascii art.
            self.data = nfo_tricks(self.data)

            # This sucks but it does the job.
            aux = ''
            for char in self.data:
                if ord(char) <= 128:
                    aux += char

            self.data = aux

            # \r makes everything more complicated, take them out of the way.
            self.data = re.sub('\r*\n', '\n', self.data)
            self.data = self.data.replace('\r', '\n')  # Replace the rest.

            # Remove extra spacing:
            self.data = re.sub(EXTRA_SPACES, ' ', self.data)
            self.data = re.sub(BEGINS_WITH_SPACES, '', self.data)
            self.data = self.data.strip()
            self.data = re.sub(BLANKLINES, '\n', self.data)

            # Remove 5+ iterations of the same character in the same line
            while len(re.findall(INLINE_REPETITIONS, self.data)) > 0:
                self.data = re.sub(INLINE_REPETITIONS, '', self.data)

            # Get 5+ vertical repetitions of the same character at
            # the beggining of the line
            while len(re.findall(VERTICAL_REPETITIONS_A, self.data)) > 0:
                exp = re.compile(
                    '(^' +
                    re.escape(
                        re.findall(VERTICAL_REPETITIONS_A, self.data)[0][0]
                    ) +
                    ')(.*)(\n)',
                    re.M
                )
                self.data = re.sub(exp, r'\2\3', self.data)

            while len(re.findall(VERTICAL_REPETITIONS_B, self.data)) > 0:
                exp = re.compile(
                    '(.*)(' +
                    re.escape(
                        re.findall(VERTICAL_REPETITIONS_B, self.data)[0][0]
                    ) +
                    '$)(\n)',
                    re.M
                )
                self.data = re.sub(exp, r'\1\3', self.data)

            # Add a space between : and http:// if necessary.
            self.data = self.data.replace(":http://", ": http://")

            # It's easier to just remove them, and re-add them iif necessary
            # rather than checking for incomplete tags and checking whether to
            # complete or delete them.
            self.data = re.sub(PRE_TAGS, '', self.data)

            # Add promo text before enclosing with tags
            if config.PROMO == True:
                self.data += "\n" + config.PROMO_TEXT

            if config.PRE:
                self.data = "[pre]" + self.data + "[/pre]"

            # Extra run for extra spacing introduced by the stripper:
            self.data = re.sub(EXTRA_SPACES, ' ', self.data)
            self.data = re.sub(BEGINS_WITH_SPACES, '', self.data)
            self.data = self.data.strip()
            self.data = re.sub(BLANKLINES, '\n', self.data)

            # Finally, set the line endings to whatever we put in config
            self.data = self.data.replace('\n', config.NEWLINE)

    def write_output(self):

        if config.OUTPUT_FILE:
            try:
                output_stream = open(config.OUTPUT_FILE, 'w')
            except IOError:
                sys.exit(1)
        else:
            output_stream = sys.stdout

        output_stream.write(self.data)

        if config.OUTPUT_FILE:  # Careful do not close stdout!
            output_stream.close()
