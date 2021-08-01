#!/usr/bin/env python3

import argparse
from .tt import generate_files


def apply_generation(arg):
    generate_files(arg.scheme_path, arg.template_path)


def get_arguments():
    parser = argparse.ArgumentParser(
        description='takes in a path to a template folder and generates corresponding structures')
    parser.set_defaults(func=apply_generation)
    parser.add_argument('scheme_path', help='path to scheme json file to be used with template')
    parser.add_argument('template_path', help='path to source template folder to be used')

    return parser.parse_args()


def main():
    args = get_arguments()
    args.func(args)


if __name__ == '__main__':
    main()

