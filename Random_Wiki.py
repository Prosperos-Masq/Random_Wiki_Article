import random
import webbrowser

question = input('Would you like to read a random wiki article (y/n)?: ')
if question == 'y' or 'yes':
    read = input('We found one for you, would you like to read it (y/n)?: ')
    if read == 'y' or 'yes':
        webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Special:Random')
        while True:
            again = input('Would you like to read another (y/n)?: ')
            if again == 'y' or 'yes':
                webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Special:Random')
        else:
            print('Read on!')
            break
    
else:
    print('Nevermind')
    