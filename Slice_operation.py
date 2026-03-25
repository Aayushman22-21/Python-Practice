sample_string="Hello, World!"
#Demonstrate different slicing operations 
print("Original String:", sample_string)

#Extract a substring using positive indices
print("Substring(0:5), sample_string[0:5]")

#Extract a substring using negative indices
print("Substring (-6:-1):", sample_string[-6:-1])

#Using step values 
print("Every Second character (0:len:2):",
sample_string[0:len(sample_string):2])

#Omitting start and end indices
print("From start to index 5 (:5):", sample_string[:5])
print("From index 7 to end (7:):", sample_string[7:])

#Reversing the string using slicing
print("Reversed String (::-1):", sample_string[::-7])
