def nextCube():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextCube():
    if num > 100:
        break
    print(num)
