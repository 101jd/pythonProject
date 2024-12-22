import argparse as ap

def main():
    parser = ap.ArgumentParser(description='Test getting args')

    parser.add_argument('-s', type=str, help='String to output')
    parser.add_argument('--verbose', '-store_true', help='Additional info')
    parser.add_argument('--repeat', type=int, default=1, help='Repeat string')


    args = parser.parse_args()

    if args.repeat:
        print(str(args.s) * int(args.repeat))

    if args.verbose:
        print(args.s, args.repeat, args.verbose)

if __name__ == '__main__':
    main()