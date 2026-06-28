
import numpy as np


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Calculate the cosine similarity between two vectors."""
    a, b = np.array(vec_a), np.array(vec_b)
    norm = np.linalg.norm(a) * np.linalg.norm(b)
    if norm == 0:
        return 0.0
    return float(np.dot(a, b) / norm)
