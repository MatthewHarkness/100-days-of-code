# 100 Days Of Code - Log
Note to Self: [GitHub Markdown for losers](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

----

### Day 0: February 18, 2021
**Hello World** & **Arithmetic Master Py Edition**

**Progress:** 
HelloWorld.py got a little out of hand I experimented with
 - ``print()`` statements (naturally, it is a HelloWorld after all)
 - Variables: ``x = 5`` ``howdyPlanet = 'Howdy Planet'``
 - String concats: ``print(howdyPlanet + helloWorld)``
 - ``for:`` statements
 - random module
 - User input (ITS THAT EASY?)

ArithmeticMasterPyEd.py was more tame. All the statements mentioned above made it real easy to work out. I only have a couple issues which I could solve today but I miss the sun:
TO-DO (haha I too am a programmer):
 - ``if userAns == Ans`` doesn't recognise when both variable match?
 - Division. I'll figure out a way to make it generate numbers which can be divided evenly.
 - Perhaps give the user a way to end the while loop too.

Update: I got carried away and continued today anyway. For future reference (and to show the learning process):
 - ``x = Input()`` by defualt sets x to a String, where my random numbers were ints. I was comparing an int to a String which returns false.
 - I added an if / else to let the user decide if they want to continue with more questions :D

**Thoughts:**
After I managed to get it working on Windows, it hit me in the face just how simple Python is, I'm going to have more issues figuring out what to do with it rather than actually doing the things I want to do with it. 
I also feel I have abused ``if`` statements in ArithmeticMasterPyEd.py. I'll look at making a cleaner version 2.

**Work:**

1. [HelloWorld.py](CodeLibrary/Day0/HelloWorld.py)
2. [ArithmeticMasterPyEd.py](CodeLibrary/Day0/ArithmeticMasterPyEd.py)


----
### Day 1: February 19, 2021
**ArithmeticMasterPyEd.py (continued)** & **TimeTest.html**

**Progress:** 
All I needed to throw into ArithmeticMaster to get Division working was a modulus check which checks if the first operand (O1) can evenly divide into O2, if it cannot fit I'll just generate new numbers for them until it fits. In other words:

```python
while O2 % O1 != 0:
    #generate new numbers buddy
```

This is very much brute forcing it, but it's still quick and entirely suitable for its purpose. However it still occassionally returns O1 and O2 as the same number which is way too easy, the ``and`` statement does not work how I thought it would in python so I'll need to work that out tonight.


After watching the Perseverance Rover land this morning I thought '*wouldn't it be nice if the nasa website just told me the stream would start at 6am my time*'. So I hopped over to http://worldtimeapi.org/ to see if it actually is that hard, it wasn't really but I forgot to plan what I was going to do **and it shows**. The API works pretty flawlessly though so well done to that team.

**Thoughts:**
Building ArithmeticMaster is really showing my need to practise basic arithmetic. I'm still enjoying python and am really excited to see how ArithmeticMaster pans out. I do want to try looking at functions and that though. That would probably make things a little easier.

I recognise that worldtimeapi does the exact conversions that I need it to do without me even trying, but I am still planning on doing it a slightly more complicated way for fun anyway. I'll reset the site to only have AJAX set up and plan my process beforehand tomorrow.

**Work:**

1. [TimeTest.html](CodeLibrary/Day1/TimeTest.html) (This guy needs a web server and chromium to run )
2. [ArithmeticMasterPyEd.py](CodeLibrary/Day1/ArithmeticMasterPyEd.py)
