play="start"
while(play=="start"):
    print("Multiples of 3 represented by Fizz\nMultiples of 5 represented by Buzz\n")
    n=input("Enter number limit:")
    i=1
    while(i<=n):
        if(i%2!=0):
            if(i%3!=0 and i%5!=0):
                print "Computer: ",i
            elif(i%3==0 and i%5==0):
                print("Computer: FizzBuzz")
            elif(i%3==0):
                print("Computer: Fizz")
            elif(i%5==0):
                print("Computer: Buzz")
        else:
            j=raw_input("Player: ")
            if(i%3==0 and i%5==0 and j!="FizzBuzz"):
                print("Computer Wins!")
                break
            elif(i%5==0 and j!="Buzz"):
                print("Computer Wins!")
                break
            elif(i%3==0 and j!="Fizz"):
                print("Computer Wins!")
                break
            elif(i!=int(j)):
                print("Computer Wins!")
                break
        i=i+1
    print("Enter 'start' to start again!\n")
    play=raw_input()

