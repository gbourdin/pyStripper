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

from tricks import (amiable_trick, lol_trick, ftp_trick,
                    c4tv_trick, psychd_trick, invandraren_trick)


def nfo_tricks(data):
    """ This function runs all the special ripping tricks on data. """
    # Order matters, invandraren has to be run before amiable
    data = invandraren_trick(data)
    data = amiable_trick(data)
    data = lol_trick(data)
    data = ftp_trick(data)
    data = c4tv_trick(data)
    data = psychd_trick(data)

    return data
