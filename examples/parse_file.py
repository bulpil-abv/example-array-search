# read digitized data


path = "C:/Users/Smith/Desktop/output from digitizer/frame_01 70 data pts.txt"
with open(path) as dig_file:
    lines = [line for line in dig_file]

    # collect the header
    header= []
    for i in range(4):
        header.append(lines[i].strip())
    print(header)


