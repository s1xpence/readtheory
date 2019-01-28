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

Although the program might seem very barebones, it was exactly what I needed to understand how Selenium works (such as how to execute the Google Chrome Canary, use the webdriver function to open pages, and it also provided me with a fairly rudimentary understanding of what the `driver.find_elements_by_xpath` function does. This function is going to be *very* useful to us later on). 

## Coding process: Part 2 (Getting my hands dirty)

The first hurdle that I had to overcome was logging in. ![alt text](https://i.imgur.com/TAZYffg.png)

I decided to search StackOverflow for some threads on how to automatically login using Selenium. The first thread that popped up was [this one](https://stackoverflow.com/questions/21186327/fill-username-and-password-using-selenium-in-python). In this thread, the OP asks how to log in using Selenium. The solution that was provided was this:
```
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("YourUsername")
password.send_keys("Pa55worD")

driver.find_element_by_name("submit").click()
```
You can see that both the username and password variable refers to a `driver.find_element_by_id` function. But because I wanted a more accurate and reliable way to locate elements in the webpage, I did a little more digging. Eventually, I started reading about `xpath` and how it could be potentionally used to our advantage in terms of automating actions (submitting forms, clicking buttons, the likes). [According to "Selenium with Python" docs, `xpath` would be useful in the sense that:](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath)

> XPath is the language used for locating nodes in an XML document... Selenium users can leverage this powerful language to target elements in their web applications... and [it] opens up all sorts of new possibilities such as locating the third checkbox on the page... One of the main reasons for using XPath is when you don’t have a suitable id or name attribute for the element you wish to locate.

Basically, its saying that `xpath` offers a much more accurate way to target the element that you're interested in, and that includes abilities such as "locating the third checkbox on the page". This is exactly what I needed, and so I set about digging through the source code with the help of Google Chrome's "Inspect Element" function. Eventually, I found the specific line of code which corresponds to the "username" field on ReadTheory's website.

```<input id="username" type="text" name="j_username" placeholder="Username">```

(The "password" field also looks similar to this line of code above, the only difference being that you would replace the word "username" with "password" in all instances which it appears.)

Okay, so now that we know how to select an element that we're interested in, exactly how do we "type" characters into the input that we're interested in? I Googled for a bit before stumbling upon [this answer](https://stackoverflow.com/a/21186468) on StackOverflow.

The guy who posted that answer states that we could use "`WebElement.send_keys` method to simulate key typing", which is all we really need. And thus, a few lines of new code was born.

```
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('14367@students.isb.ac.th')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('mhNF2PqdfjF3W')
```
As you can see, I've implemented the `xpath` method here and have also extracted the `xpath` ID of the element we're interested in, which is both the `username` and `password` field. I honestly don't quite know how you're supposed to get the `xpath` ID manually, so I just used a feature that Google Chrome has, which can be found [here](https://stackoverflow.com/a/42194160)
You might have also noticed that I've also gone ahead and implemeted the `send_keys` method here, with a email thats about to expire in a few months and a password (specifically for ReadTheory) that I don't care too much about. 

Now for the fun part. I've got to figure out how to make it so that it "clicks" on the submit form for me. But fear not, for this is what Selenium was designed for as well. A quick search showed that I could submit just by using the `.click()` function in tandem with the `xpath` function. This hurdle was easily overcome as well. And as such, I added a new line of code to my program:

```login_click = driver.find_element_by_xpath('//*[@id="ajaxLogin"]').click()```

