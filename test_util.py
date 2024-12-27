import sys

def test(did_pass):
    """ Print the result of a test"""
    linenum = sys._getframe(1).f_lineno # Get the line number of the caller
    if (did_pass):
        msg = "Test at line {} passed".format(linenum)
    else:
        msg = "Test at line {} failed".format(linenum)
    print(msg)
