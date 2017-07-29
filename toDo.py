# toDo.py
import logging
from testStuff import testStuff



def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('started')
    testStuff()
    logging.info('Finished')

if __name__ == '__main__':
    main()