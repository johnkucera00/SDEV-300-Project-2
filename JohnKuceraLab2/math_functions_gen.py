"""
__filename__ = "math_functions_gen.py"
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
import math

def floatrange(beg, end, step):
    """
    range() function to support floats
    """
    while True:
        if beg >= end and step > 0:
            break
        elif beg <= end and step < 0:
            break
        yield beg
        beg = beg + step
    return

def main():
    """
    Math Functions Generator main
    """
    # Menu
    print('***** Welcome to the Math Function Generator! *****')

    selection = int(input('Select from the following menu:\n'
                          '\t1. Generate x, sin(x) for x = -2pi to x = 2pi'
                          ' with an increment of pi/64\n'
                          '\t2. Generate x, cos(x) for x = -2pi to x = 2pi'
                          ' with an increment of pi/64\n'
                          '\t3. Generate x, sqrt(x) for x = 0 to x = 200'
                          ' with an increment of 0.5\n'
                          '\t4. Generate x, log10(x) for x = 0 to x = 200'
                          ' with an increment of 0.5\n'
                          '\t5. Exit the application\n'))

    # Option 1: Sine values, x = -2pi to x = 2pi
    if selection == 1:
        print('********** SINE VALUES - START **********\n')
        for xvalue in floatrange(-2*math.pi, 2*math.pi, math.pi/64):
            yvalue = float(math.sin(xvalue))
            print(str(xvalue) + ',' + str(yvalue))
        print('\n********** SINE VALUES - END **********\n')

    # Option 2: Cosine values, x = -2pi to x = 2pi
    elif selection == 2:
        print('********** COSINE VALUES - START **********\n')
        for xvalue in floatrange(-2*math.pi, 2*math.pi, math.pi/64):
            yvalue = float(math.cos(xvalue))
            print(str(xvalue) + ',' + str(yvalue))
        print('\n********** COSINE VALUES - END **********\n')

    # Option 3: Square Root values, x = 0 to x = 200
    elif selection == 3:
        print('********** SQRT VALUES - START **********\n')
        for xvalue in floatrange(0, 200.5, 0.5):
            yvalue = float(math.sqrt(xvalue))
            print(str(xvalue) + ',' + str(yvalue))
        print('\n********** SQRT VALUES - END **********\n')

    # Option 4: log10 values, x = 0 to x = 200
    elif selection == 4:
        print('********** LOG10 VALUES - START **********\n')
        for xvalue in floatrange(0, 200.5, 0.5):
            if xvalue != 0:
                yvalue = float(math.log10(xvalue))
                print(str(xvalue) + ',' + str(yvalue))
            else:
                yvalue = 'UNDEFINED'
                print(str(xvalue) + ',' + yvalue)
        print('\n********** LOG10 VALUES - END **********\n')

    # Option 5
    elif selection == 5:
        print('You selected 5.')
        print('Thank you for trying the Math Function Generator application.')
        print('**************************************************')
        return

    # Invalid Option
    else:
        print('You must enter 1, 2, 3, 4, or 5. Please try again.')

if __name__ == "__main__":
    main()
