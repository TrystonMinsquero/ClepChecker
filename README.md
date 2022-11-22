# Clep Checker
Just a silly script I made to parse a peterson practice clep test and compare it with a text file of answers.

~~Was just trying to procrastinate studying for the exam, so I just made this.~~

Use on any Peterson Practice Exam from the [Tests](Tests/) folder that I got from [this dropbox link](https://www.dropbox.com/sh/9o0nisu3bir1nai/AADHiiAEP0jmn-gDElRl2Q4ha?dl=0&fbclid=IwAR3lVnfdlkE9rbp3anN020uJrQJbdAvJiPQJlA-8etqCEEAR-8YQTriguGA&) from reddit. 

## How it works

**Prereq:** Make sure you have [python](https://www.python.org/downloads/) installed.

you will *probably* have to run `pip install PyPDF2` first.

Go to the current directory you downloaded this to and just run:<br> 
`py clepChecker.py -p <test_pdf> -y <your_answer_sheet>`


Get more info about other options by running:
`py clepChecker.py -h`