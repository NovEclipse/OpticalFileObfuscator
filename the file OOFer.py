hexmap = {
    '0': '\u200B', '1': '\u200C', '2': '\u200D', '3': '\u200E',
    '4': '\u200F', '5': '\uFEFF', '6': '\u00AD', '7': '\u200A',
    '8': '\u2009', '9': '\u00A0', 'a': '\u180E', 'b': '\u2060',
    'c': '\u2064', 'd': '\u2065', 'e': '\u2066', 'f': '\u2067',
}
sep = '\u2068'

try:
    filein = str(input("Enter your file name without extension(e.g., for `doc.txt` enter `doc): "))
    with open((filein + ".txt"), "r", encoding = "latin-1") as infile:
        with open((filein + ".oof"), "w", encoding = "utf-8") as outfile:
            while True:
                char = infile.read(1)
                if not char:
                    break
                if char == "\n":
                    outfile.write("\n")
            
                else:
                    hexed = format(ord(char), '02x')
                    outfile.write(hexmap[hexed[0]])
                    outfile.write(hexmap[hexed[1]])
                    outfile.write(sep)
        
    print("encode done.")

except Exception as e:
    print(f"Error occurred: {e}")

