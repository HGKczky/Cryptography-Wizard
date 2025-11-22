import sys
import itertools

def permutationMaker(outputfile, *args):
    fp = open(outputfile, 'a')
    for r in range(1, len(args) + 1):
        for p in itertools.permutations(args, r):
            fp.write(str(p))
def main():
    if len(sys.argv) != 4 or sys.argv[1].strip('-') == "h":
        print("usage: PasswordListGenerator <pattern> <WordListDirectory> <output file> ")
        print("Example: PasswordListGenerator ?d?c?C?ix?w WordListDirectory.txt output.txt")
        exit()
    pattern = sys.argv[1] # this is gonna be a string
    wordListDirectory = sys.argv[2]
    outputfile = sys.argv[3]
    pieces = pattern[1:].split("?")
    Wordlist = [[]]
    print("Test")
    for carg in pieces:
        match carg:
            case "d":
                print("Digit")
            case "c":
                print("Lowercase letter")
            case "C":                
                print("Uppercase Character")
            case "w":
                print("WordList")
            case "s":
                print("Special Character")
            case _: # default case  
                print("Individual Character: " + carg[1:])

    
    permutationMaker(Wordlist, "a")


main()

