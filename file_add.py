# Add last of the data
f = open("mobis_1630435.txt",'a')
for i in range(11,21) :
    f.write("%d \n"%i)
f.write("This is end of this file.\n")
f.write('='*50)
f.close()
