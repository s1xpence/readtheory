# Automating Readtheory using Python in conjunction with Selenium (OSX)

Trust me guys, it's not as boring as it sounds. Here's to hoping that I don't lose anyone in the following section because this is my first writeup of any kind :)

## why u do dis??

Well, my English teacher assigned our class to do 50+ Readtheory quizzes if we wanted the highest grade possible. She said that she didn't really care too much about the answers being correct (and even said so herself that it was "a numbers game") so I took it upon myself to reach that goal in the laziest way possible. What was supposed to be a quick and easy coding session (with minimal effort involved) turned into a unexpectedly fun and frustrating coding project. 

## john lenin, pls help for i do not know what i need
Sure. You're going to need to install the following dependencies. I'm going to link the instructions, but feel free to contact me if you've got any questions.
* Python
* [Homebrew](https://brew.sh/). You'll need this to install everything else
* Chromedriver and Chrome Canary. Code to install it with brew is as is (using terminal): ```brew install chromedriver && brew install Caskroom/versions/google-chrome-canary```
* Selenium for Python. You can install it using `sudo pip selenium`. If you don't have `pip` then follow the [instructions here](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x/18947390#18947390)
 
## Coding process: Part 1 (inspirations)
I had previously heard of Selenium from [codingmak](https://github.com/codingmak). He had shown me how he was using Selenium on a certain website, and I remember thinking that it was pretty cool, but never really gave it much thought until recently when I was looking for ways to automate my reading quizzes. I looked into a bit, and decided that I was going to stick and run with this. I chose Python because I'd heard that it was a nice language to use when it came to automation purposes. Plus, it's easy to learn it on the go. You don't really need to know all the specific syntaxes of Python. All you really need is a rudimentary understanding of how the flow of control works and to be willing to google whatever it is that you're unfamiliar with (tip: googling a specific issue with the word "solved" in it helps a lot. for example, instead of "how to fix water" you'd google "how to fix water solved" and so on.)

I did a quick google search since I wanted to see what other people had come up with already and so that I had a general idea of how people use Selenium in Python. I was eventually led to [this link] (https://medium.com/@stevennatera/web-scraping-with-selenium-and-chrome-canary-on-macos-fc2eff723f9e) which detailed the basics of what you would be able to do with Selenium in Python. 
Here's the code that I drew most of my inspirations from:
```
# reddit.py
from selenium import webdriver
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://reddit.com')
topLinks = driver.find_elements_by_xpath("//div/p/a[contains(@class, 'title')]")
for link in topLinks:
  print 'Title: ', link.text
driver.quit()
```
As you can see, it's actually quite simple. Because I want to make this as accessible as possible, I'll give a brief description of what's going on here. 
The program is importing a Selenium module that has the `webdriver` attribute first, and after that, it opens Google Chrome in "headless" mode (which basically means that Chrome is operating without a window). The program then instructs Chrome to navigate to reddit and to grab all of the titles on the front page of reddit, which the program would then print out in the terminal window. 

Although the program may seem very barebones, it was exactly what I needed to understand how Selenium works (such as how to execute the Google Chrome Canary, use the webdriver function to open pages, and it also provided me with a fairly rudimentary understanding of what the `driver.find_elements_by_xpath` function does. This function is going to be *very* useful to us later on). 




*The program is importing the Selenium module (it's importing the `webdriver` attribute in particular), the `time` module, and a attribute to catch a error that the program faces often with (`ElementNotVisibleException`)
What this program is going to do

