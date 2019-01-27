f = open("./mike.txt","a")

while True:
   my_input = input('Enter text to append to file [or EXIT to quit] :')
   if my_input.lower() == 'exit':
       break
   f.write(my_input + '\n')
   print (my_input)
   #f.flush()

#f.seek(0)
#all_lines = f.readlines()
f.close

count = 0
f = open("./mike.txt","r")
for line in f.readlines():
	count += 1
f.close()

f = open("./mike.txt","a")
f.write ("Closing File with " + str(count) + " lines and Exiting...\n")