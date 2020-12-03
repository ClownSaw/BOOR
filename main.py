#!/usr/local/bin/python3      #
#coding: utf-8                #
#web: https://www.clownsaw.tk #
#ClownSaw [x]                 #
###############################

from requests import get
from fuzzywuzzy import fuzz
from googlesearch import search
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
import os, sys

# colorama
init()

blue = Fore.BLUE
red = Fore.RED 
yellow = Fore.YELLOW 
green = Fore.GREEN 
cyan = Fore.CYAN
magenta = Fore.MAGENTA 
reset = Fore.RESET 

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

def ClownLogo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

.----.  .----.  .----. .----.            
| {}  }/  {}  \/  {}  \| {}  }           
| {}  }\      /\      /| .-. \           
`----'  `----'  `----' `-' `-'           
          .----.  .----..-..-. .-. .---. 
         /  {}  \{ {__  | ||  `| |{_   _}
         \      /.-._} }| || |\  |  | |  
          `----' `----' `-'`-' `-'  `-'  
                             Autor: ClownSaw
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

ClownLogo()

query   = input(f'{cyan}SAW ~#{magenta} ')
results = 100


print(f'{red}[{green}+{red}] {green}Searching {cyan}{query}{reset}')
for url in search(query, stop = results):
	print(f'\n{green}[{cyan}+{green}] {yellow}Url detected:{cyan} ' + url)
	try:
		text = get(url, timeout = 1).text
	except:
		continue
	soup = BeautifulSoup(text, "html.parser")
	links_detected = []
	try:
		print(f' {blue}|\n {red}¤{blue}---{yellow}[{cyan}?{yellow}] {green}Title:{magenta} ' + soup.title.text.replace('\n', ''))
	except:
		print(f' {blue}|\n {red}¤{blue}---{yellow}[{cyan}?{yellow}] {green}Title: {red}null{reset}')
	# Find by <a> tags
	try:
		for link in soup.findAll('a'):
			href = link['href']
			if not href in links_detected:
				if href.startswith('http'):
					# Filter
					if url.split('/')[2] in href:
						links_detected.append(href)
					# If requested data found in url
					elif query.lower() in href.lower():
						print(f'   {blue}   |\n      {yellow}¤{blue}--- {green}Requested data found at link :{cyan} ' + href)
						links_detected.append(href)
					# If text in link and link location is similar
					elif fuzz.ratio(link.text, href) >= 60:
						print(f'   {blue}   |\n      {yellow}¤{blue}--- {green}Text and link are similar :{cyan} ' + href)
						links_detected.append(href)
	except:
		continue
	if links_detected == []:
		print(f'      {blue}|\n      {green}¤{blue}--- {red}No data found{reset}')



	
#for s in links_detected: print(s)
