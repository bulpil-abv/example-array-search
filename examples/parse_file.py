# read digitized data from
# GetData graph digitizer


# path = "D:\\blender_scripts\\blender_repo\output from digitizer\sec_01 70 data pts.txt"
def parse_file(path:str) -> list:
    """
    Parse a file with "   " - three spaces separator
    :param path: the digitized data
    :return: xyz[(x, y, z),....]
    """
    with open(path) as dig_file:
        lines = [line for line in dig_file]

        # collect the header - 3 lines
        header = []

        for i in range(3):
            header.append(lines[i].strip())

        # collect the z coordinate of the section
        z = float(lines[3].strip().split("   ")[1])

        # collect the data, split is 3 spaces
        dataset = []
        for i in range(4, len(lines)):
            dataset.append(lines[i].strip().split("   "))
        print(dataset)
        print(len(dataset))
        xyz = [0] * len(dataset)

        for i in range(len(dataset)):
            row = dataset[i]
            xyz[i] = (float(row[0]), float(row[1]), z)
        print(xyz)
    return xyz
