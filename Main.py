from CaeserCipher import CaeserCipher
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--encode', type=str)
    parser.add_argument('--decode', type=str)
    parser.add_argument('--shift', type=int)
    args = parser.parse_args()
    if not args:
        exit()
    elif args.encode:
        string = CaeserCipher.encode(args.encode, args.shift)
        print(string)
    elif args.decode:
        string = CaeserCipher.decode(args.decode, args.shift)
        print(string)
    exit(0)


if __name__ == "__main__":
    main()
