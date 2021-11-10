def make_faces(n_vertices: int, n_sections: int) -> list:
    """
    Make faces from the vertices in two sections.
    :param n_sections number of sections
    :param n_vertices number of vertices in a single section.
    :return: faces with indices wound counterclockwise
    """

    faces = [(0, 0, 0)] * (n_vertices - 1) * (n_sections - 1)
    for sec in range(0, n_sections-1):
        for i in range(sec * n_vertices, (sec + 1) * n_vertices - 1):
            faces[i-sec] = (i, i + 1, i + n_vertices + 1, i + n_vertices)

    return faces
