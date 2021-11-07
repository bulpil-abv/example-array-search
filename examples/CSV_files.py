import csv

path = "C:/Users/Smith/Desktop/output from digitizer/frame_01 70 data pts.txt"
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)


