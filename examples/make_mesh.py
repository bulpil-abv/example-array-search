# make a mesh

def make_faces(section0: list, section1: list) -> list:
    """
    Make faces from the vertices in the sections.
    :param section0: list of consecutive vertices
    :param section1: list of consecutive vertices
    :return: faces wound counterclockwise
    """

    I = len(section1)
    faces = [(0, 0, 0)] * (I - 1)
    for i in range(0, I - 1):
        faces[i] = (i, i + 1, i + I + 1, i + I)
    return faces
