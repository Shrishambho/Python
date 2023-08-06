import random

def win(user,com):
    if(user==com):
        return "draw";
    elif(user=="rock" and com=="scissors") or (user=="paper" and com=="rock") or(user=="scissors" and com=="paper"):
        return "user";
    else:
        return "com";






def userInput():
    userWins=0;
    computerWins=0;
    Draw=0;
    while True:
        uChoice=input("Enter user choice\n1.rock\n2.paper\n3.scissor\n4.quite\n");
        print(f"User choice is {uChoice}");
        if(uChoice=="quite"):
            
            break;
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computers choice is {computer_choice}");
        res=win(uChoice,computer_choice);
        if(res=="draw"):
            Draw+=1;
            print("This round draw");
        elif(res=="user"):
            userWins+=1;
            print("This round won by user");
        elif(res=="com"):
            computerWins+=1;
            print("This round won by com");
        
        print(f"user Wins {userWins} round-computer wins{computerWins} round-total {Draw} matches are drawn");
  
    print("Thanks for playing game");









if __name__ == "__main__":
 userInput();
