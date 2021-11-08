# read digitized data from
# GetData graph digitizer


path = "C:/Users/Smith/Desktop/output from digitizer/frame_01 70 data pts.txt"
with open(path) as dig_file:
    lines = [line for line in dig_file]

    # collect the header - 3 lines
    header = []
    for i in range(3):
        header.append(lines[i].strip())

    # collect the z coordinate of the section
    z = lines[4]

    # collect the data, split is 3 spaces
    dataset = []
    for i in range(4, len(lines)):
        dataset.append(lines[i].strip().split("   "))

    x = [0.0] * len(dataset)
    y = [0.0] * len(dataset)
    for i in range(len(dataset)):
        row = dataset[i]
        x[i],y[i] = row[0], row[1]

    print(x)
    print(y)

# TODO modify raw file to include z coordinate and parse it in this script e.g. line[4] = z etc.
# TODO save the (x,y,z) into file to be read by the face mesh script