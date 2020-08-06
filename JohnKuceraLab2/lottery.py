"""
__filename__ = "lottery.py"
__coursename__ = "SDEV 300 6380 - Building Secure Web Applications (2198)"
__author__ = "John Kucera"
__copyright__ = "None"
__credits__ = ["John Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Kucera"
__email__ = "johnkucera00@gmail.com"
__status__ = "Test"
"""
import random

def main():
    """
    Lottery Main
    """
    # Menu
    print('***** Welcome to the Pick-3, Pick-4 Lottery Number Generator! *****')

    selection = int(input('Select from the following menu:\n'
                          '\t1. Generate 3-Digit Lottery Number\n'
                          '\t2. Generate 4-Digit Lottery Number\n'
                          '\t3. Exit the Application\n'))

    # Sentinel while loop
    while selection != 3:

        # Option 1
        if selection == 1:
            print('You selected 1. The following 3-Digit Lottery Number was '
                  'generated:')
            quantity = 3
            while quantity:
                print(random.randrange(0, 10), end='')
                quantity -= 1
            selection = int(input('\nSelect from the following menu:\n'
                                  '\t1. Generate 3-Digit Lottery Number\n'
                                  '\t2. Generate 4-Digit Lottery Number\n'
                                  '\t3. Exit the Application\n'))

        # Option 2
        elif selection == 2:
            print('You selected 2. The following 3-Digit Lottery Number was '
                  'generated:')
            quantity = 4
            while quantity:
                print(random.randrange(0, 10), end='')
                quantity -= 1
            selection = int(input('\nSelect from the following menu:\n'
                                  '\t1. Generate 3-Digit Lottery Number\n'
                                  '\t2. Generate 4-Digit Lottery Number\n'
                                  '\t3. Exit the Application\n'))

        # Invalid selection
        else:
            print('You must enter 1, 2, or 3. Please try again.')
            selection = int(input('\nSelect from the following menu:\n'
                                  '\t1. Generate 3-Digit Lottery Number\n'
                                  '\t2. Generate 4-Digit Lottery Number\n'
                                  '\t3. Exit the Application\n'))

    # Option 3
    print('You selected 3.')
    print('Thank you for trying the Lottery application.')
    print('**************************************************')
    return

if __name__ == "__main__":
    main()
