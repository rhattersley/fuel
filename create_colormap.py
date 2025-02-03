#!/usr/bin/python3
import pprint
import sys

import matplotlib._cm_listed as cms


def create_map(name):
    values = getattr(cms, f"_{name}_data")
    values = [[round(v, 3) for v in rgb] for rgb in values]
    with open(f"colormaps/{name}.json", "w") as f:
        pprint.pprint(values, f)


if __name__ == '__main__':
    _, name = sys.argv
    create_map(name)
