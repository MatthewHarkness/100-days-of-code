# 100 Days Of Code - Log
Note to Self: [GitHub Markdown for losers](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

----

### Day 0: February 18, 2021
**Hello World** & **Arithmetic Master Py Edition**

**Progress:** 

Created HelloWorld.py as a means to test basic expressions. This includes
 - ``print()`` statements (naturally, it is a HelloWorld after all)
 - Variables: ``x = 5`` ``howdyPlanet = 'Howdy Planet'``
 - String concats: ``print(howdyPlanet + helloWorld)``
 - ``for:`` loop
 - ``if ... : else:`` statement
 - random module ``random.randrange(1, 100)``
 - User input (ITS THAT EASY?) ``x = input('Please Input: ')``

Created ArithmeticMasterPyEd.py which was more tame and focused. It generates simple maths questions for users to answer:
 - Used a `while` loop to let the user answer multiple questions
 - User can answer addition, multiplication, or subtraction
 - used `random.randrange` to generate random numbers for operands

TO-DO (haha I too am a programmer):
 - ``if userAns == Ans`` doesn't recognise when both variable match?
 - Division. I'll figure out a way to make it generate numbers which can be divided evenly.
 - Perhaps give the user a way to end the while loop too.

Update: I got carried away and continued ArithmeticMaster anyway:
 - Fixed previously mentioned variable match issue. ``userAns = Input()`` by defualt sets answer to a string, where my random numbers were ints. I was comparing an int to a String which returns false.
 - I added an if / else to let the user decide if they want to continue with more questions as opposed to automatically continuing

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
 - Changed the variable name of operands for ``operandx`` to ``Ox`` where x is a number
 - Added the Division system to ArithmetricMaster, I somehow entirely missed the modulus check which made comparing two generated Operands trivial. it resulted in the following code

```python
while O2 % O1 != 0:
    O2 = random.randrange(1-100)
    O1 = random.randrange(1-100)
```
This is very much brute forcing it, but it's still quick and entirely suitable for its purpose. 
 - Division occassionally returns both operands as the same number which is way too easy, I tried using ``and`` operator but it seems to function different to how I expected
 - In the meantime, an ``if`` statement which catch when operands match
 - Seperated code blocks to improve readability 

Watching the Perserverance Mars Rover land this morning, I though '*wouldn't it be nice if the NASA site just told me that the stream would start at 6am AEST as opposed to giving me the time EST and telling me to figure it out*'. I set off to see if it was that hard to make:
 - Created TimeTest.html, added a ``<script>`` header in the ``<head>`` so I can play with JavaScript.
 - AJAX is a simple progress, I have it in multiple functions for readability.
 - I needed an API which can get me the time and date in UTC and the current time zone. I initially planned on using [Google Time Zone API](https://developers.google.com/maps/documentation/timezone/overview), but I got a little scared when I saw that it had a cost (in retrospect I, a single person, probably would not have used it enough to evoke a billing). I instead opted for [World Time API](http://worldtimeapi.org/).
 - Plans derailed, instead of building a time-zone converter I started looking through all the different ways you can get data from this API, unfortunately I've left the code incomplete.

**Thoughts:**

I am not sure of where my end point for Arithmetic Master is. I could continue to add more operators like powers, I could add a GUI and handle all possible exceptions. I'll keep working on it in the meantime.

I never planned what I was doing with TimeTest and it shows. [World Time API](http://worldtimeapi.org/) gives all the data required to do an easy conversion however I fell into a hole of looking at all the different parts of time, ultimately getting nothing complete. I also was thinking of a dozen different ways to convert the time as opposed to just picking one and sticking with it. My process needs work, and I need to research what I can get from an API before I implement it into my code.

**Work:**

1. [TimeTest.html](CodeLibrary/Day1/TimeTest.html) (This guy needs a web server and chromium to run )
2. [ArithmeticMasterPyEd.py](CodeLibrary/Day1/ArithmeticMasterPyEd.py)

----
### Day 2: February 20, 2021
**classtest.py** and **ArithmeticMasterPyEd.py (continued)**

**Progress:** 
classtest.py is a script which explains Object Orientated Programming in Python.
 - Drew up a (very) simple UML Class Diagram to represent what I want to do. It's very java and I need to find correct UML conventions for Python.
 - Implemented classes `Car` and `Owner`. Guess how they interact.
 - I am discovering the incredible world of underscores in Python. Particularly ``__init__()`` and ``__str__()`` which after a [quick search](https://medium.com/python-features/naming-conventions-with-underscores-in-python-791251ac7097) shows that they are "Dunder Methods", that is methods with underscores so that it doesn't conflict with user methods of the same name. 

Neat.

- To expand on the last point. Python conventions are very different from that which established in Java. [I am leaving this here](https://www.python.org/dev/peps/pep-0008/) for future reference.

Arithmetic Master needed some cleaning before I was happy to leave it until I start GUI:
- Arithmetic Master now uses actual `True` `False` booleans as opposed to numbers.
- Duplicate Operands no longer occur, I moved the modulus operator into an `if` statement alongside an expression which checks if the operands are equal, when those conditions are not met, a boolean `questionValid` is set to `True`. This statement is inside a `while` loop which continues when `questionValid = false`
```Python
#Check numbers can be divided evenly
questionValid = False
while not questionValid:
    if O2 % O1 != 0 or O1 == O2:
        O2 = random.randrange(2, 150)
        O1 = random.randrange(2, 100)
        print('O1 = ', O1, ', O2 = ', O2)
    else:
        questionValid = True
```
- Set the minimum num for an operand to 2, there is no situation in which 1 would be a useful operand.
- Increased the maximum operand for O2 in division to 150, as to introduce more variety of questions.
- Answers in Arithmetic Master are now presented as ints instead of Doubles:.

Old Answers (Ugly, uncomfortable gross): ``Correct Answer is 7.0``

New Answers (Cool, sexy, ambitious): ``Correct Answer is 7``

**Thoughts:**

OOP seems to work the same throughout most of Python as it does to Java, learning the correct grammar and conventions would be useful but ultimately I don't feel I will learn anything new from this route. I'll finish classtest.py before finding a different direction. w3schools has a machine learning tutorial for Python. It might be wise to follow that instead.

Similarly, ArithmeticMasterPyEd.py does most of what I want it to. I was planning on experimenting with Tkinter GUI, but I might hold that so I can instead focus on features where Python might be more useful.

**Work:**
1. [classtest.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day2/classtest.py)
2. [classtest.jpg (UML Class Diagram)](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day2/classtest.jpg)
3. [ArithmeticMasterPyEd.py (final terminal version for now)](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day2/ArithmeticMasterPyEd.py)

---
### Day 3: February 21, 2021
**SecQuestionGenerator.py**

**Progress:**
 - Created SecQuestionGenerator.py as means to play with `list` and have a laugh while doing so.
 
**Thoughts:**
I hope I can justify this incredibly simple program with the excuse of 'Today was a work day and I spent all my free time studying for that exam I have tomorrow'. The list system doesn't work too differently from Java arrays, but once again falls into that void of 'I already know what I am doing with this'. I need to find a way to push myself into doing more complicated and ambitious projects.

**Work:**
1. [SecQuestionGenerator.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day3/SecQuestionGenerator.py)

---
### Day 4: February 22, 2021
**Function.py** and **classtest.py (continued)**

**Progress:**

Function.py was a means to comprehend what exactly functions are in Python with basic maths functions:
 - Created Function.py with increment, decrement and squared functions to create a value from `i = 0`
```Python
def incrementFunct(i):
    i += 1
    return i

def decrementFunct(i):
    i -= 1
    return i

def squared(i):
    i *= i
    return i
```
Arent they cute?

classtest.py
 - Added `Class Garage:`, including a list `garageList = []`
 - Found unique ways to add `Car` objects to garageList from outside the class, I was impressed that Python allowed `print(garage.getGarageList()[1])`
 - Used a unique `for` loop to access list items: `for x in garage.getGarageList():`

**Thoughts:**
I desperately need to plan what I am doing for #100DaysOfCode over the next few weeks. 4 days in and I am already feeling a little lost, with worthwhile progress drastically dwindling.  Regardless, understand Objects, funictions and Lists feels like a vital aspect of Python, I just feel that that should have been done as part of a larger more ambitious project.

**Work:**
1. [function.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day4/Function.py)
2. [classtest.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day4/classtest.py)

---
### Day 5: February 23, 2021
**piptest.py, numpyarrays.py** and **numpyanalysis.py**


**(Learning) Progress:**
This bit is going to be a little less 'log' and a little more explaining what I have figured out.
 - Figured out how packages work in python. (its super simple)

```
C:\\>py -m pip install numpy
Collecting numpty...
```
Its that easy.
- I can activate any package or module in a .py file by simply importing it ``import numpy``
- [NumPy](https://github.com/numpy/numpy) is a useful package for Arrays.
- Python features an `as` statement which functions like how it does in SQL. Instead of having to type out 5 whole characters `numpy.function()` in the code, I can set it with ``import numpy as np`` and I can refer to numpy as np `np.function()` in code. Brilliant!
- np allows the creation of actual arrays. 
- 2D and 3D arrays are very literally 'an array inside an array' in the np syntax (and I love it).
- np has the means (pun intended) to analyse arrays. I should look at [SciPy](https://www.scipy.org/) to expand that functionality.

What I have learnt is more detailed in my actual programs. Check them out for specifics.

**Thoughts:**

Modules and Functions bring even more to Python. I am beginning my Machine learning process but that starts with relearning high school maths, and honestly I am okay with this. Figuring out a Standard Deviation is actually fun when there is no pressure. This will also fit very nicely alongside my current uni subjects. I'll absolutely continue down the path of [w3schools machine learning tutorial](https://www.w3schools.com/python/python_ml_getting_started.asp). It does look relatively simple but w3 always manage to be an incredible path for beginning.

**Work:**
1. [piptest.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day5/piptest.py)
2. [numpyarrays.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day5/numpyarrays.py)
3. [numpanalysis.py](https://github.com/MatthewHarkness/100-days-of-code/blob/master/CodeLibrary/Day5/numpyanalysis.py)

I will likely take my first break from #100DaysOfCode tomorrow so I can complete a fun fast food shift at work, and focus on my uni assignment.
