#THIS IS THE FIRST EXAMPLE OF PROGRAMMING DIRECTLY IN PYCHARM

def count_a(seq):

    result= 0

    for b in seq:
        if b =='A':
            result += 1

    return result


s= input("ENTER THE SEQUENCE: ")

na= count_a(s)
print("THE NUMBER OF A'S IS: ", na)



#Calculate the total sequence length

tl= "A"

perc= round(100.0* na/ tl, 1)

print("THE TOTAL LENGTH IS : {}".format(tl))
print("THE percentage IS : {}".format(perc))


