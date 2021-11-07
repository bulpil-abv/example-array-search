# read digitized data


path = "C:/Users/Smith/Desktop/output from digitizer/frame_01 70 data pts.txt"
with open(path) as dig_file:
    lines = [line for line in dig_file]

    # collect the header
    header = []
    for i in range(4):
        header.append(lines[i].strip())

    # collect the data
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