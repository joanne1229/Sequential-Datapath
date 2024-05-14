#Name: Belal Eltemsah and Joanne Wang
#I pledge my honor that I have abided by the Stevens Honor System. 

file = open('instructions.txt', 'r', encoding='utf-8')
while True: 
    lineoutput = ""
    line = file.readline()
    if line[0] == "add":
        lineoutput += "00"
    elif line[0] == 'and':
        lineoutput += "01"
    elif line[0] == 'ldr':
        lineoutput += "10"
    elif line[0] == 'str':
        lineoutput += "11"