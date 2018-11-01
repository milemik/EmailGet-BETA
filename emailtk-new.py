from tkinter import *
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from textemail import main

# creating window top
top = Tk()

top.title('EmailGet-0.2-BETA') # window title
top.geometry('350x200') # window size

# on button click:
def clicked():
    mail = 'No mail' # input default
    #url = ''
    if 'http:' not in str(unos.get()) or 'https:' not in str(unos.get):
        url = 'https://'+unos.get() # if user didnt enter https: add it
    if 'www' not in url:
        url = 'https://www.'+unos.get() # if user didnt enter www add it
    else:
        url = unos.get() # if user enter good url continue
    #url = unos.get()
    try:
        mail = main(url) # search email
        out = Text(master=top, heigh=10, width=40) # text box size
        out.grid(column=0, row=5) # text position
        out.insert(END, mail+'\n\nApp by mileta99\nemail:botx99@hotmail.com') # outupt at the end mail, and app by...
    except :
        # if something went wrong:
        out = Text(master=top, heigh=10, width=40)
        out.grid(column=0, row=5)
        out.insert(END, 'Somethig went bad, probably bad url\n\nApp by: mileta99\nIn case of bugs please report to this mail:\nbotx99@hotmail.com')

# text label one
text1 = Label(top, text='Hi there! Wellcome to EmailGet BETA\nIt si ongoing project\n')
text1.grid(column=0, row=1) # text label one position

text2 = Label(top, text='Enter website to get email below:')# text label 2
text2.grid(column=0, row=2) # text label 2 position

unos = Entry(top, width=43) # enter text box
unos.grid(column=0, row=4) # enter text box position

buton = Button(top, text='Kliknite ovde', command=clicked, bg='blue', fg='red')# create a button
buton.grid(column=0, row=3) # button position

top.mainloop() # run window until user close it
