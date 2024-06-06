line = "From samvith.muramula@gmail.com Sat Jan 5 09:14:16 2008"
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): 
        continue
    words = line.split()
    print(words)
    email = words[1]
    pieces = email.split("@")
    name = pieces[0]
    print(name)
fhand.close()