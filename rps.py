from tkinter import *
import random
window=Tk(className=' Rock Paper Scissors - Best of 5')

#Logic

def checkWinner():
    if playerScore.cget("text") == "5" or cpuScore.cget("text") == "5":
        if playerScore.cget("text") == "5":
            winnerLbl["text"]="Player Wins"
        else:
            winnerLbl["text"]="CPU Wins"
        rockBtn["state"]="disabled"
        paperBtn["state"]="disabled"
        scissorsBtn["state"]="disabled"

def battle(order):
    choices=["Rock","Paper","Scissors"]
    cpuChoice=random.choice(choices)
    index=order.index(cpuChoice)
    cpuActionLbl["text"]="CPU chooses "+cpuChoice
    if(index>1):
        cpuScore["text"]=str(int(cpuScore.cget("text"))+1)
    elif(index<1):
        playerScore["text"]=str(int(playerScore.cget("text"))+1)
    checkWinner()


def rock_command():
    orderofPower=["Scissors","Rock","Paper"]
    battle(orderofPower)
def paper_command():
    orderofPower=["Rock","Paper","Scissors"]
    battle(orderofPower)
def scissors_command():
    orderofPower=["Paper","Scissors","Rock"]
    battle(orderofPower)

def restart_game():
    cpuScore["text"]="0"
    playerScore["text"]="0"
    rockBtn["state"]="normal"
    paperBtn["state"]="normal"
    scissorsBtn["state"]="normal"
    winnerLbl["text"]=""
    cpuActionLbl["text"]=""

#First Row

blankLbl=Label(window,text="",width=10)
blankLbl.grid(row=0,column=0)

rockBtn=Button(window,text="Rock",width=10,command=rock_command)
rockBtn.grid(row=0,column=1)

winnerLbl=Label(window,text="")
winnerLbl.grid(row=0,column=5)

restartBtn=Button(window,text="Restart Game",width=10,command=restart_game)
restartBtn.grid(row=0,column=9)

#Second Row

blankLbl2=Label(window,text="",width=10)
blankLbl2.grid(row=1,column=0)

paperBtn=Button(window,text="Paper",width=10,command=paper_command)
paperBtn.grid(row=1,column=1)

blankLblFiller=Label(window,text="",width=10)
blankLblFiller.grid(row=1,column=2)

playerLbl=Label(window,text="Player: ")
playerLbl.grid(row=1,column=3)

playerScore=Label(window,text="0")
playerScore.grid(row=1,column=4)

versusLbl=Label(window,text="VS")
versusLbl.grid(row=1,column=5)

cpuLbl=Label(window,text="CPU: ")
cpuLbl.grid(row=1,column=6)

cpuScore=Label(window,text="0")
cpuScore.grid(row=1,column=7)

blankLblFiller2=Label(window,text="",width=10)
blankLblFiller2.grid(row=1,column=8)


closeBtn=Button(window,text="Close",width=10,command=window.destroy)
closeBtn.grid(row=1,column=9)

#Third Row

blankLbl3=Label(window,text="",width=10)
blankLbl3.grid(row=2,column=0)

scissorsBtn=Button(window,text="Scissor",width=10,command=scissors_command)
scissorsBtn.grid(row=2,column=1)

cpuActionLbl=Label(window,text="")
cpuActionLbl.grid(row=2,column=5)


window.mainloop()