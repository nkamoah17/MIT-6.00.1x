# I can guess your secret number
low = 1
high = 99
ans = (high+ low) // 2

print("Please think of a number between 0 and 100 !")

print("Is your secret number " + str(ans) + " ?" )
userAns = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
while ans < 100 :
    if userAns == "h" :
            high = ans
            ans = ( high + low )// 2
            print("Is your secret number " + str(ans) + " ?" )
            userAns = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
            if userAns != "h" or userAns != "l" :
               print("Sorry, I did not understand your input")
               
       
    elif userAns == 'l' : 
            low = ans 
            ans = (high + low)//2
            print("Is your secret number " + str(ans) + " ?" )
            userAns = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
            if userAns != "h" or userAns != "l" :
               print("Sorry, I did not understand your input")
     
    if userAns == 'c' :
        print("Game over. Your secret number was: " + str(ans)) 
        break
    
     



