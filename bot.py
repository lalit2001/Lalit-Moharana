from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
bot=ChatBot("My Bot")
convo=[
    'Hello',
    'hi their !',
    'what is your name',
    'my name is Bot , i am created by lalit',
    'how are you ?',
    'i am doing great',
    'Where are you from',
    'I''m from Internet ?'
]

trainer=ListTrainer(bot)
#to train the bot
trainer.train(convo)
# print("talk to bot")
# while True:
#     query= input()
#     if query=="exit":
#         break
#     ans=bot.get_response(query)
#     print(ans)

#GUI part
main=Tk()

main.geometry("500x650")
main.title("My chatBot")
#bot logo
img=PhotoImage("bot1.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

#frameBOT IMA

def ask_from_bot():
   query=textF.get()
   answer_from_bot=bot.get_response(query)
   msg.insert(END,"You :"+query)
   msg.insert(END,"BOT :"+str(answer_from_bot))
   textF.delete(0,END)

frame=Frame(main)
sc=Scrollbar(frame)

#listbox

msg=Listbox(frame,width=80,height=20)

sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#Creating textfill
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask From Bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()


main.mainloop()
