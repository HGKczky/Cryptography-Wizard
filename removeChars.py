import sys, re
def main():
    if len(sys.argv) != 5 or sys.argv[1].strip('-') == "h":
        print("usage: removeChars <chars> <replace with what in single quotes> <input file> <output file> ")
        print("Example: removeChars -+ ' ' input.txt output.txt")
        exit()
    chars = sys.argv[1]
    replace = sys.argv[2].strip('\'"')
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    
    pattern = f"[{re.escape(chars)}]"
    try:
        with open(inputfile, "r", encoding="utf-8") as infile:
            data = infile.read()
                
        cleaneddata = re.sub(pattern, replace, data)

        with open(outputfile, "w", encoding="utf-8") as outfile:
            outfile.write(cleaneddata)
    
        print(f"Done, saved to '{outputfile}'")

    except FileNotFoundError:
        print(f"Error file '{inputfile}' not found")

main()

    
    
    
