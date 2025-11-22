import sys
import sympy

def RSADecrypt(evalue, nvalue, data):
    factors = sympy.primefactors(nvalue)
    print("The prime factors of N:" + str(factors))
    phi = (factors[0] - 1) * (factors[1] - 1)
    dvalue = pow(evalue, -1, phi)
    datalist = data.split()
    cleaneddata = []
    returnstring = ""
    for value in datalist:
        cleaneddata.append(chr(pow(int(value), dvalue,  nvalue)))
        returnstring = ''.join(cleaneddata)
    return(returnstring)
    
def main(): 
    if len(sys.argv) != 5 or sys.argv[1].strip('-') == "h":
        print("usage: RSA <n value> <e value> <input file> <output file> ")
        print("Example: RSA 1079 43 input.txt output.txt")
        exit()      
    nvalue = int(sys.argv[1])
    evalue = int(sys.argv[2])
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    
    try:
        with open(inputfile, "r", encoding="utf-8") as infile:
            data = infile.read()
                
        cleaneddata = RSADecrypt(evalue, nvalue, data)

        with open(outputfile, "w", encoding="utf-8") as outfile:
            outfile.write(cleaneddata)
        
        print(cleaneddata)

        print(f"Done, saved to '{outputfile}'")

    except FileNotFoundError:
        print(f"Error file '{inputfile}' not found")

main()           
