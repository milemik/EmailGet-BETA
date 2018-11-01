#!/usr/bin/python3

from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re


def search_mail_from_text(url):
    req = Request(url, headers={'User-Agent':'Mozila 5.0'}) # request for url
    try:
        page = urlopen(req) # open url
    except:
        # if could not open website
        print('Error opening the website')
    soup = bs(page, 'html.parser') # use bs to read page
    web_text = soup.findAll(text=True) # get all text from url
    for text in web_text:
        mail = re.search('\w+@\w+[.]\w+', text) # try to find email
        if mail is not None:
            return mail.group() # if found return mail 
        # else it will return None
        
def search_mail_in_contacts(url):
    req = Request(url, headers={'User-Agent':'Mozila 5.0'})
    try:
        page = urlopen(req)
    except:
        print('Error opening the website')
    soup = bs(page, 'html.parser')
    a = soup.findAll('a', href=True)
    for link in a:
        if 'contact' in link.text.lower(): # find and get contact url link
            return link['href']
def main(u):
    # try to find email from first website
    m = search_mail_from_text(u)
    if m is not None:
        return m
    else:
        # if no email on website first page (first url entered)
        # search for contact link
        contact_link = search_mail_in_contacts(u)
        if 'http' not in contact_link: # if http not in contact link, add u to it
            new_link = u+contact_link
        else:
            new_link = contact_link # else continue
        m = search_mail_from_text(new_link) # search for mail in contact link
        if m is not None:
            return m # if email found return it
        else:
            return 'No email found' # else print No email...
