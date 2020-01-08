#!/usr/bin/env python3

import random
import signal
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

# def countabilityProof():
#     # generates portion of result from Cantor's diagonalization argument
#     floatList = []
#     result = ''
#     for i in range(50):
#         # excludes 0, to comply with proof requirement
#         num = 0
#         while float(num) == 0:
#             num = random.random()
#         floatList.append('{0:.50f}'.format(num))
# 
#     for i in range(2, 50):
#         if int(floatList[i][i]) == 0:
#             result += str(1)
#         else:
#             result += str(0)
# 
#     return result

def bernoulli_process(p="0.5"):
    p = float(p)
    while True:
        yield int(random.random() < p)

# plugin:
# register sequence generator functions in this dictionary
# functions only accept keyword arguments (kwargs)
# functions are responsible for parsing kwarg types from string
choices = {
    "bernoulli_process": bernoulli_process,
    # "countability_proof": countability_proof
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
    parser.add_argument("-kwargs", help="the space-separated list of key-value pairs passed to the sequence generator", default="")
    args = parser.parse_args(argv)
    return args

def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)

def main(argv):
    args = parse_argv(argv[1:])
    kwargs = dict(ele.split("=") for ele in args.kwargs.split(" ")) if args.kwargs else {}
    print(*generate_sequence(choices[args.seq], args.n, kwargs), sep="\n")
    return 0

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    sys.exit(main(sys.argv))
