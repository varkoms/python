# TESTS HERE
import time
from test_util import test
from methods import col_clashes, load_words_from_file, remove_adjacent_dups, is_multiple, is_factor, binary_search, f2c, hours_in, to_secs, day_add, day_name, turn_clockwise, merge_sorted_lists

def test_suite():
    # # """ Turn Clockwise tests """
    # test(turn_clockwise("N") == "E")
    # test(turn_clockwise("E") == "S")
    # test(turn_clockwise("S") == "W")
    # test(turn_clockwise("W") == "N")
    # test(turn_clockwise(42) == None)
    # test(turn_clockwise("Rubbish") == None)

    # # """ Day Name tests """
    # test(day_name(3) == "Wednesday")
    # test(day_name(6) == "Saturday")
    # test(day_name(2) == "Tuesday")

    # """ Day Add tests """
    # test(day_add("Monday", 4) == "Friday")
    # test(day_add("Tuesday", 0) == "Tuesday")
    # test(day_add("Tuesday", 14) == "Tuesday")
    # test(day_add("Sunday", 100) == "Tuesday")
    # test(day_add("Sunday", -1) == "Saturday")
    # test(day_add("Sunday", -7) == "Sunday")
    # test(day_add("Tuesday", -100) == "Sunday")

    # # """ To Secs tests """
    # test(to_secs(2, 30, 10) == 9010)
    # test(to_secs(2, 0, 0) == 7200)
    # test(to_secs(0, 2, 0) == 120)
    # test(to_secs(0, 0, 42) == 42)
    # test(to_secs(0, -10, 10) == -590)

    # # """ Hours In tests """
    # test(hours_in(9010) == 2)

    # """ F2C tests """
    # test(f2c(212) == 100)     # Boiling point of water
    # test(f2c(32) == 0)        # Freezing point of water
    # test(f2c(-40) == -40)     # Wow, what an interesting case
    # test(f2c(36) == 2)        # Body temperature
    # test(f2c(37) == 3)        # Body temperature
    # test(f2c(38) == 3)        # Body temperature
    # test(f2c(39) == 4)        # Body temperature

    # """ Binary Search tests """
    # test(binary_search([2, 4, 6, 8, 23, 45, 46, 47, 56, 78, 90, 100, 102, 154], 154) == "Item found in pos: 13")
    # test(binary_search([2, 4, 6, 8, 1, 3, 9, 47, 56, 78, 90, 100, 102, 88], 100) == "List is not sorted")
    # test(binary_search([2, 4, 6, 8, 1, 3, 9, 47, 56, 78, 90, 100, 102, 88], 44) == None)

    # """ Is Factor tests """
    # test(is_factor(3, 12))
    # test(not is_factor(5, 12))
    # test(is_factor(7, 14))
    # test(not is_factor(7, 15))
    # test(is_factor(1, 15))
    # test(is_factor(15, 15))
    # test(not is_factor(25, 15))

    # """ Is Multiple tests """
    # # Reutilizamos el metodo is_factor
    # test(is_multiple(12, 3))
    # test(is_multiple(12, 4))
    # test(not is_multiple(12, 5))
    # test(is_multiple(12, 6))
    # test(not is_multiple(12, 7))

    # """ Remove Adjacent Duplicates tests """
    # test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
    # test(remove_adjacent_dups([]) == [])
    # test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) == ["a", "big", "bite", "dog"])

    # """merge sorted lists tests"""
    # test(merge_sorted_lists([1,2,3,4],[5,6,7,8]) == [1,2,3,4,5,6,7,8])

    """Chessboard tests"""
    test(not col_clashes([6,4,2,0,5], 4))
    test(not col_clashes([6,4,2,0,5,7,1,3], 7))
    test(col_clashes([0,1], 1))
    test(col_clashes([5,6], 1))
    test(col_clashes([6,5], 1))
    test(col_clashes([0,6,4,3], 3))
    test(col_clashes([5,0,7], 2))
    test(not col_clashes([2,0,1,3], 1))
    test(col_clashes([2,0,1,3], 2))


# END OF TESTS
test_suite()
