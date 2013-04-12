# -*- coding: utf-8 -*-
import collections
import optparse
import codecs
import sys
import re

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'


def count(words, all_chars=False):
    """Character frequency analysis.

    A simple analysis of the characters in the text.

    :param words: string to count
    :param all_chars: set counting all characters
    """
    regex = re.compile(u'^[a-zA-ZĄĘŚĆŻŹŁÓĆŃąęśćżźłóćń]+$')
    char_dict = collections.Counter()

    for char in words:
        if not all_chars:
            if regex.match(char):
                char_dict[char] += 1
        else:
            if not char in ['\r', '\n', u'\u2013']:
                char_dict[char] += 1

    for char in sorted(char_dict, key=char_dict.get, reverse=True):
        print '    %s: %d  (%.2f%%)' % (
            char, char_dict[char], (float(char_dict[char])) / float(sum(char_dict.values())) * 100)

    print ' Suma: %d' % (sum(char_dict.values()))


if __name__ == '__main__':
    parser = optparse.OptionParser(version='1.0')
    parser.set_usage(sys.argv[0] + ' [option]')

    parser.add_option('-f', dest='file', action='store', default=False,
                      help='wskaz plik z tekstem')
    parser.add_option('-a', dest='allchars', action='store_true', default=False,
                      help='zliczaj wszystkie znaki')

    (options, args) = parser.parse_args()

    print ''
    print 'Czestotliwosc wystepowania znakow'
    print ''
    print 'Autor: ' + __author__

    if not options.allchars:
        print ' Tryb: Zliczanie tylko liter'
    else:
        print ' Tryb: Zliczanie wszystkich znakow'

    if options.file:
        print ''
        print ' IN> ' + options.file

        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
            count(file_stream.read(), all_chars=options.allchars)
            file_stream.close()
        except IOError as e:
            print '\nI/O error({0}): {1}'.format(e.errno, e.strerror)
            sys.exit(1)

    else:
        while 1:
            print ''
            try:
                text = raw_input(' IN> ').decode(sys.stdin.encoding)
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)

            count(text, all_chars=options.allchars)