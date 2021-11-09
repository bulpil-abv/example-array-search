# make a mesh

def make_faces(n_vertices:int, n_sections:int) -> list:
# TODO Make the function to work with more than two sections
    """
    Make faces from the vertices in two sections.
    :param n_vertices number of vertices in a single section.
    :return: faces with indices wound counterclockwise
    """

    I = n_vertices
    faces = [(0, 0, 0)] * (I - 1)
    for i in range(0, I - 1):
        faces[i] = (i, i + 1, i + I + 1, i + I)
    return faces
