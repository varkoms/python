# TESTS HERE
from test_util import test
from methods import turn_clockwise, day_name, day_add, to_secs, hours_in, f2c, binary_search

def test_suite():
    # """ Turn Clockwise tests """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("E") == "S")
    test(turn_clockwise("S") == "W")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("Rubbish") == None)

    # """ Day Name tests """
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(2) == "Tuesday")

    """ Day Add tests """
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    # """ To Secs tests """
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

    # """ Hours In tests """
    test(hours_in(9010) == 2)

    """ F2C tests """
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case
    test(f2c(36) == 2)        # Body temperature
    test(f2c(37) == 3)        # Body temperature
    test(f2c(38) == 3)        # Body temperature
    test(f2c(39) == 4)        # Body temperature

    """ Binary Search tests """
    test(binary_search([2, 4, 6, 8, 23, 45, 46, 47, 56, 78, 90, 100, 102, 154], 154) == "Item found in pos: 13")
    test(binary_search([2, 4, 6, 8, 1, 3, 9, 47, 56, 78, 90, 100, 102, 88], 100) == "List is not sorted")
    test(binary_search([2, 4, 6, 8, 1, 3, 9, 47, 56, 78, 90, 100, 102, 88], 44) == None)
# END OF TESTS

test_suite()
