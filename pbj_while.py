#Collaboration with S. Gorman

#Lesson 2, Goal 1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly."""

#bread = 7
#jelly = 0
#pb = 6
#b = bread/2
#number = 0
#if  bread >= 2 and jelly >= 1 and pb >=1:
#    while bread >= 2 and jelly >= 1 and pb >= 1:
#        number = number+1
#        print "Making sandwich #{0}".format(number)
#        bread = bread-2
#        jelly = jelly-1
#        pb = pb-1
#else: print "Shopping time!"
    
# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

bread = 10
jelly = 5
pb = 10
b = bread/2
number = 0

if  bread >= 2 and jelly >= 1 and pb >=1:
    while bread >= 2 and jelly >= 1 and pb >= 1:
        number = number+1
        print "Making sandwich #{0}".format(number)
        bread = bread-2
        jelly = jelly-1
        pb = pb-1
        if bread < 2 and jelly < 1 and pb < 1:
            print "All done. Time to buy all three."
        elif bread < 2 and pb < 1:
            print "All done. Time to buy bread and peanut butter."
        elif pb < 1 and jelly <1 :
            print "All done. Time to buy peanut butter and jelly."
        elif jelly <1:
            print "All done. Time to buy jelly."
        elif pb <1:
            print "All done. Time to buy peanut butter."
        elif bread <1:
            print "All done. Time to buy bread."
        else: print "I have enough bread for {0} more sandwiches, enough peanut butter for {1}, enough jelly for {2} more.".format(bread, pb, jelly)
else: print "Shopping time!"

