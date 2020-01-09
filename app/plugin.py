#!/usr/bin/env python3

import random
import signal
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


def bernoulli_process(p="0.5"):
    p = float(p)
    while True:
        yield int(random.random() < p)

# plugin:
# register sequence generator functions in this dictionary
# functions only accept keyword arguments (kwargs)
# functions are responsible for parsing kwarg types from string
choices = {
    "bernoulli_process": bernoulli_process
}

def generate_sequence(func, n, kwargs):
    for idx, ele in enumerate(func(**kwargs), start=1):
        yield ele
        if idx == n:
            break

def parse_argv(argv):
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("seq", help="the sequence name", choices=choices)
    parser.add_argument("n", help="the number of sequence elements to generate", type=int)
    parser.add_argument("-kwargs", help="the '='-delimited key-value pairs passed to the sequence generator function", nargs="+", default="")
    args = parser.parse_args(argv)
    return args

def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)

def main(argv):
    args = parse_argv(argv[1:])
    kwargs = dict(ele.split("=") for ele in args.kwargs) if args.kwargs else {}
    print(*generate_sequence(choices[args.seq], args.n, kwargs), sep="\n")
    return 0

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    sys.exit(main(sys.argv))
