#!/usr/bin/env python3

import json
import os
import random
import sys
import urllib.request
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, FileType

from midiutil import MIDIFile


def oeis(q):
    """Retrieve the OEIS accession data.
    
    Arguments:
        q {[str]} -- [the A-number]
    """
    url = f"https://oeis.org/search?q=id:{q}&fmt=json"
    with urllib.request.urlopen(url) as file:
        return json.load(file)

# generates portion of result from Cantor's diagonalization argument
def countabilityProof():
    floatList = []
    result = ''
    for i in range(50):
        # excludes 0, to comply with proof requirement
        num = 0
        while float(num) == 0:
            num = random.random()
        floatList.append('{0:.50f}'.format(num))

    for i in range(2, 50):
        if int(floatList[i][i]) == 0:
            result += str(1)
        else:
            result += str(0)

    return result

def parse_argv(argv):
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("file", type=FileType())
    parser.add_argument("-out", help="the output file", nargs="?", type=FileType("wb"), default=os.fdopen(sys.stdout.fileno(), "wb", closefd=False))
    parser.add_argument("-base", help="the base degree", type=int, default=60)
    parser.add_argument("-separation", help="the separation time between notes", type=float, default=1.0)
    parser.add_argument("-duration", help="the note duration in beats", type=float, default=1.0)
    parser.add_argument("-volume", help="the volume in [0-127]", type=int, default=100)
    parser.add_argument("-tempo", help="the tempo in BPM", type=int, default=100)
    args = parser.parse_args(argv)
    return args

def main(argv):
    args = parse_argv(argv[1:])
    base = args.base

    data = [args.base + int(line) for line in args.file]
    degrees = set(data)
    track, channel, time = 0, 0, 0

    midi = MIDIFile(1)
    midi.addTempo(track, time, args.tempo)

    for i, pitch in enumerate(data):
        midi.addNote(track, channel, pitch, time + i * args.separation, args.duration, args.volume)

    with args.out as file:
        midi.writeFile(args.out)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
