import argparse
from clrext import ColorExtractor


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-image', type=str)
    return parser.parse_args()


def main(args):
    extractor = ColorExtractor()
    colors = extractor.extract(args.in_image)
    print(colors)


if __name__ == '__main__':
    args = get_args()
    main(args)
