# Make new file
f = open("mobis_1630435.txt",'w')
f.write('='*50)
f.write("\nThis file shows 1 to 10 with line changed.\n")
for i in range(1,11) :
    f.write("%d \n"%i)
f.close()