from pyfiglet import Figlet
import cowsay
import argparse

def main(name: str):
    message = "Hello, my name is " + name
    cowsay.cow(message)
    f = Figlet(font='digital')
    print(f.renderText(name))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processes arguments.')
    parser.add_argument('--name', type=str, default='Betsy', help='Name your cow')
    args = parser.parse_args()
    main(args.name)