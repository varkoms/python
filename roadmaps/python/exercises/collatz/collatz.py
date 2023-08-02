def collatz_sequence(n):
    collatz_list = list() # List to store the values of sequence

    while(n != 1):
        collatz_list.append(n)

        # If n is even
        if (n % 2 == 0):
            n = n // 2
        else:
            # if n is odd
            n = (3 * n) + 1
    
    collatz_list.append(1) # Print 1 at the end
    l = len(collatz_list)

    print("The length of collatz sequence is", l)
    print("The sequence is:")

    for i in range(0, l):
        print(collatz_list[i])

# Main
collatz_sequence(20)

# Output
'''
The length of collatz sequence is 15
The sequence is:
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
'''