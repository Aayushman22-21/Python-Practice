fin =open("input.txt",'r') #file opening in read mode 
fout =open("output.txt",'w') #file opening in write mode#file is created 
for line in fin: #for loop to read each line of the file
    line = line.swapcase() #swapcase function to change uppercase to lowercase and vice versa
try:
    line = line.replace(" ", "") #replace function to remove spaces from the line
    fout.write(line) #write the modified line to the output file
except:
   print("An error occurred while processing the file.")