What does this program do?
This program parses the file "mbox-short.txt" and looks for each line that starts with the text "From" and when it finds a '@' in that line, it stops parsing and retrieves the name from that string

How to run the program?
1. type the following: 
   python SPLITemail.py
2. Program will print the output of the line parsed and just the name of the email without '@' and domain name. Similar to this example

['From', 'sam.murm@htps.us', 'Sat', 'Jan', '5', '09:14:16', '2008']
sam.murm

