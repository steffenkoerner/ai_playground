

def dot_product(vec_a, vec_b):
    result = 0
    for i in range(len(vec_a)):
        result += vec_a[i]*vec_b[i]
    return result

def length(vec):
    result = 0
    for i in range(len(vec)):
        result += vec[i]*vec[i]
    return result

def cosine_similarity(vec_a, vec_b):
    """Calculate the cosine similarity between two vectors."""
    top = dot_product(vec_a, vec_b)
    low_a = length(vec_a)
    low_b = length(vec_b)

    result = top/(low_a*low_b)
    return result
    