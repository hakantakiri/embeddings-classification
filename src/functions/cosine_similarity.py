from numpy import dot
from numpy.linalg import norm

def get_CS(list_1: list[float], list_2: list[float]):
    return dot(list_1, list_2)/(norm(list_1)*norm(list_2))