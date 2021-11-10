def badnums(lower, upper, badNumbers):
    ''' the comments will run the example in the main block
    assumptions:  - lower and upper are not actual values in the list badNumbers
                  - non negative ints
    '''

    # badNumbers = [37, 7, 22, 15, 49, 60]
    badNumbers.sort()
    # badNumbers = [7, 15, 22, 37, 49, 60]
    next_good_num = lower
    current_seg = 0
    longest_seg = 0
    i = 0

    while i < len(badNumbers) and badNumbers[i] < upper:
        current_seg = badNumbers[i] - next_good_num
        
        if current_seg > longest_seg:
            longest_seg = current_seg
        next_good_num = badNumbers[i] + 1

        i += 1

    # case where upper < max(badnumbers) -> check last rightmost segment
    # note again list is sorted
    if upper < badNumbers[-1]:
        current_seg = badNumbers[-1] - upper
        if current_seg > longest_seg:
            longest_seg = current_seg
    return longest_seg
        





if __name__ == "__main__":
    n = 6
    badNumbers = [37, 7, 22, 15, 49, 60]
    lower = 3
    upper = 48

    print(badnums(lower, upper, badNumbers))