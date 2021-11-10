# read digitized data from
# GetData graph digitizer




def parse_file(file_paths:list) -> list:
    """
    Parse a file with "   " - three spaces separator
    :param file_paths: paths to the files with the digitized data
    :return: list_vertices[(x, y, z),....]
    """
    list_vertices = []
    for path in file_paths:
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

            xyz = [0] * len(dataset)

            for i in range(len(dataset)):
                row = dataset[i]
                xyz[i] = [float(row[0]), float(row[1]), z]

        list_vertices += xyz

    return list_vertices
