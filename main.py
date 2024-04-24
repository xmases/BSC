import sys

cnt, argv = 0, []
while cnt != 4:
    cnt += 1
    argv.append(int(sys.argv[cnt]))

cordsa, cordsb, frames = argv[0:2], argv[2:4], int(sys.argv[5])

def froute(a, b, frames):
    defc, frate = [], []
    if not isinstance(a, list) and not isinstance (b, list) :
        assert False, "An error ocurred. Program terminated"
    
    for i in range(2) :
        defc.append(b[i] - a[i])
    
    frate.append(defc[0] / frames)
    frate.append(defc[1] / (frames * 2))

    return defc, frate

froute_list = froute(cordsa, cordsb, frames)
defc, frate, pos = froute_list[0], froute_list[1], cordsa

with open("cords.txt", "w") as f:
    for i in range(frames) :
        pos[1] += frate[1]
        if i % 2 == 0 :
            pos[0] += frate[0]
        f.write("cords = ["+str(pos[0])+", "+str(pos[1])+", "+str(i+1)+"] \n")

