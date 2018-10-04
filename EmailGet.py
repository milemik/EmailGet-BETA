from tkinter import *
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

#creating window
top = Tk()
#title - of the window
top.title('EmailGet-0.1-BETA')
#window size 
top.geometry('350x200')

# on click do this:
def clicked():
    mail = 'No mail'
    #url = ''
    # if user didnt put https with website address, add it
    if 'http:' not in str(unos.get()) or 'https:' not in str(unos.get):
        url = 'https://'+unos.get()
    # if no www in the address add https://www
    if 'www' not in url:
        url = 'https://www.'+unos.get()
    # else url is ok, go on
    else:
        url = unos.get()
    #try to connect to website
    try:
        req = Request(url, headers={'User-Agent':'Hi'})
        page = urlopen(req)
        soup = bs(page, 'html.parser')
        # get all 'a' tags
        a = soup.find_all('a', href=True)
        for x in a:
            # if 'mailto' in tag that is mail!!!
            if 'mailto:' in x['href']:
                mail = x['href'].split(':')[1]
        # create a text field and enter the mail
        out = Text(master=top, heigh=10, width=40)
        out.grid(column=0, row=5)
        out.insert(END, mail+'\n\nApp by mileta99\nemail:botx99@hotmail.com')
    # if cant connect to website print error
    except :
        out = Text(master=top, heigh=10, width=40)
        out.grid(column=0, row=5)
        out.insert(END, 'Somethig went bad, probably bad url\n\nApp by: mileta99\nIn case of bugs please report to this mail:\nbotx99@hotmail.com')

# First text line in the window
text1 = Label(top, text='Hi there! Wellcome to EmailGet BETA\nIt si ongoing project\n')
text1.grid(column=0, row=1)
#Second text in the window
text2 = Label(top, text='Enter website to get email below:')
text2.grid(column=0, row=2)
# entery field
unos = Entry(top, width=43)
unos.grid(column=0, row=4)
# button on clicked
buton = Button(top, text='Kliknite ovde', command=clicked, bg='blue', fg='red')
buton.grid(column=0, row=3)
# keep window open until i hit x or ctrl+c
top.mainloop()
                              
