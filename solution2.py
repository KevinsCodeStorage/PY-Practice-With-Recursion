# Write code for algorithm 2 below
def natural_numbers(i, lowernum=1):

    if lowernum > i:
        return
    else:
        print(lowernum)
        natural_numbers(i, lowernum + 1)


natural_numbers(10)

