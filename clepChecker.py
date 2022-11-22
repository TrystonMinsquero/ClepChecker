import PyPDF2
import sys, getopt

class Answer:

    def __init__(self, number : int, choice : str):
        self.number = number
        self.choice = choice

    def __eq__(self, __o: object) -> bool:
        return __o.number == self.number and __o.choice == self.choice

    def __ne__(self, __o: object) -> bool:
        return not self == __o

    def __str__(self) -> str:
        return (f'{self.number}: {self.choice}')

    def __lt__(self, other):
        return self.number < other.number


def read_answers(testpdfName : str) -> list[Answer]:
    pdfReader = PyPDF2.PdfFileReader(open(testpdfName, 'rb'))
    
    answers = []
    for i in range(pdfReader.numPages):
        page = pdfReader.getPage(i).extractText()
        if "The correct answer is" in page:
            lines = page.splitlines()
            for line in lines:
                if "The correct answer is" in line:
                    words = line.split('.')
                    number = int(words[0].split(' ')[-1])
                    choice = str(words[1][-1])
                    answers.append(Answer(number, choice))

    return answers

def read_your_answers(fileName : str) -> list[Answer]:
    text = open(fileName, 'r')
    answers = []
    i = 1
    for line in text.readlines():
        answers.append(Answer(i, line.strip()))
        i += 1
    return answers
        


def compare_answers(real_answers : list[Answer], your_answers : list[Answer], show_all=False):
    output = ""
    real_answers = sorted(real_answers)
    your_answers = sorted(your_answers)
    total_wrong = 0
    for (correct, maybe) in zip(real_answers, your_answers):
        if correct != maybe:
            output += f'❌ {maybe} -> {correct.choice}\n'
            total_wrong += 1
        elif show_all:
            output += f'✔️ {maybe}\n'
    total = len(real_answers)
    percent = ((total - total_wrong)/total)*100
    output += f'\n {total - total_wrong}/{total} ({round(percent,4)})\n'
    return output

def print_help():
    print('clepChecker.py [-p | -petersonfile=] <peterson pdf> [-y | -yourfile=] <your answers> | [-a | -all=<bool>]')

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hp:y:ao:", ["petersonfile=", "yourfile=", "all=", "output="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    testpdf, yourAns, output_file = "", "", ""
    show_all = False

    for opt, arg in opts:
        if opt == '-h': 
            print_help()
            sys.exit()
        elif opt == '-p' or opt == '--petersonfile':
            testpdf = arg
        elif opt == '-y' or opt == '--yourfile':
            yourAns = arg
        elif opt == '-a' or opt == "--all":
            show_all = arg.lower() != 'false'
        elif opt == '-o' or opt == "--output":
            output_file = arg

    if testpdf == "" and len(args) > 0:
        testpdf = args[0]
    if yourAns == "" and len(args) > 1:
        yourAns = args[1]
    if output_file == "" and len(args) > 2:
        output_file = args[2]

    if testpdf == "" or yourAns == "":
        print_help()
        sys.exit()
    real_answers = read_answers(testpdf)
    your_answers = read_your_answers(yourAns)
    results = compare_answers(real_answers, your_answers, show_all)
    if output_file != "":
        try:
            open(output_file, 'w', encoding='utf-8').write(results)
        except Exception as e:
            print(e)
            print(results)
    else:
        print(results)

if __name__ == '__main__':
    main(sys.argv[1:])



