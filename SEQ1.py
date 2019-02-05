class  Seq:
    # A class for representing sequences
    def __init__(self, strbases):
        print("New empty sequence created")

        self.strbases= strbases

    def len(self):

        return len(self.strbases)

#THIS IS PART OF THE CONCEPT OF INHERITANCE,
#THIS ALLOW US TO REUSE THE METHODS OF PREVIOUS CLASSES

class Gene(Seq):
    pass






s1= Seq("ATTCTCT")
s2= Seq("ACCTCTCT")

l1= s1.len()
l2= s2.len()


str1= s1.strbases
str2= s2.strbases

print("")
print("The end")


print(l1,l2)



print(str1, str2)



