#!/usr/bin/env python3

import json
import os
import sys
import urllib.request
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, FileType

from midiutil import MIDIFile


def parse_argv(argv):
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("file", help="the sequence of MIDI pitch numbers [Integer, 0-127] or rest indicator [Integer, -1]", type=FileType())
    parser.add_argument("-out", help="the output file", nargs="?", type=FileType("wb"), default=os.fdopen(sys.stdout.fileno(), "wb", closefd=False))
    parser.add_argument("-separation", help="the separation time between notes", type=float, default=1.0)
    parser.add_argument("-duration", help="the note duration in beats", type=float, default=1.0)
    parser.add_argument("-volume", help="the volume in [0-127]", type=int, default=100)
    parser.add_argument("-tempo", help="the tempo in BPM", type=int, default=100)
    args = parser.parse_args(argv)
    return args

def main(argv):
    args = parse_argv(argv[1:])

    data = list(map(int, args.file))
    degrees = set(data)
    track, channel, time = 0, 0, 0

    midi = MIDIFile(1)
    midi.addTempo(track, time, args.tempo)

    sep = args.separation

    for i, pitch in enumerate(data):
        if pitch != -1:
            midi.addNote(track, channel, pitch, time + i * sep, args.duration, args.volume)

    with args.out as file:
        midi.writeFile(args.out)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
