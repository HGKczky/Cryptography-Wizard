import sys, re
def main():
    if len(sys.argv) != 5 or :sys.argv[1].strip('-') == "h":
        print("usage: removeQuotes <quote or double (-q/d)> <replace with what in single quotes> <input file> <output file> ")
        print("Example: removeQuotes -d ' ' input.txt output.txt")
        exit()
    
    type2 = sys.argv[1].strip('-')
    replace = sys.argv[2].strip('\'"')
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    
    try:
        with open(inputfile, "r", encoding="utf-8") as infile:
            data = infile.read()
        if type2 == 'd':
            cleaneddata = re.sub(r"[\"]", replace, data)
        elif type2 == 'q':
            cleaneddata = re.sub(r"[\']", replace, data)
        else:
            print("usage: RemoveQuotes <quote or double (-q/d)> <replace with what in single quotes> <input file> <output file> ")
            print("Example: RemoveQuotes -d ' ' input.txt output.txt")
            exit()

    
        with open(outputfile, "w", encoding="utf-8") as outfile:
            outfile.write(cleaneddata)
    
        print(f"Done, saved to '{outputfile}'")

    except FileNotFoundError:
        print(f"Error file '{inputfile}' not found")

main()

    
    
    
