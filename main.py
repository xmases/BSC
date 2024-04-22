import sys

cnt, argv = 0, []
while cnt != 4:
    cnt += 1
    argv.append(int(sys.argv[cnt]))

cordsa, cordsb = argv[0:2], argv[2:4]

def froute(a, b, frames):
    defc, frate = [], []
    if not isinstance(a, list) and not isinstance (b, list) :
        assert False, "An error ocurred. Program terminated"
    
    for i in range(2) :
        defc.append(b[i] - a[i])
    
    for x in defc :
        frate.append(x / frames)

    return defc, frate

froute_list = froute(cordsa, cordsb, sys.argv[5])
defc, frate, pos = froute_list[0], froute_list[1], cordsa

with open("cords.txt" "w") as f:
    for i in range(sys.argv[5]) :
        for y in range(len(pos)) :
            pos[i] += frate[i]
        f.write("cords = ["+pos[0]+", "+pos[1]+", "+i+"]")

