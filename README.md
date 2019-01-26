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


