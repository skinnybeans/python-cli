import argparse

def start():
    print('hello')
    parser = argparse.ArgumentParser(description='Testing some arg parsing')
    parser.add_argument( '-log', '--log-level', help='Logging level. default=warning', default='warning')
    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    start()
