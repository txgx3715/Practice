d = {}
s = 0
for i in range(1,10):
    for j in range(1,i+1):
        if i== j:
            print("{}*{}={} ".format(i,j,i*j),end="\n")
        else:
            print("{}*{}={} ".format(i,j,i*j),end="\t")
