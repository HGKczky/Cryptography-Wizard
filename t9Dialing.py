import sys
from itertools import groupby

DialNums = {
        2 : "ABC",
        3 : "DEF",
        4 : "GHI",
        5 : "JKL",
        6 : "MNO",
        7 : "PQRS",
        8 : "TUV",
        9 : "WXYZ",
        0 : "+"
}

def T9DialingDecryptor(data, space, seperator):
    cleaned = ""
    for char, group in groupby(data):
        count = len(list(group))
        if char.isdigit():
            stre = DialNums.get(int(char), "")
            if stre:
                temp = stre[(count - 1) % len(stre)]
                print(temp, end = "")
                cleaned += temp
        elif char == space:
            print(" ", end = "")
            cleaned += " "
        elif char == seperator:
            continue
        else:       
            print(char, end = "")
            cleaned += char
    print()
    return cleaned


def main():
    if len(sys.argv) != 5 or sys.argv[1].strip('-') == "h":
        print("usage: t9Dialing <character representing space> <character seperating sets of nums> <input file> <output file>")
        print("Example: t9Dialing ' ' '-' inputfile.txt outputfile.txt")
        exit(0)
    space = sys.argv[1].strip('\'"')
    seperator = sys.argv[2].strip('\'"')
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    if space == seperator:
        print("space and char seperator cannot be the same")
        exit(0)
    try:
        with open(inputfile, "r", encoding="utf-8") as infile:
            data = infile.read()
                
        cleaneddata = T9DialingDecryptor(data, space, seperator)

        with open(outputfile, "w", encoding="utf-8") as outfile:
            outfile.write(cleaneddata)
    
        print(f"Done, saved to '{outputfile}'")

    except FileNotFoundError:
        print(f"Error file '{inputfile}' not found")

main()
