
# # import numpy as np
# # import scipy


# # def transpose(mat, tr, N):
# #     for i in range(N):
# #         for j in range(N):
# #             tr[i][j] = mat[j][i]

# # def isSymmetric(mat, N):
 
# #     tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
# #     transpose(mat, tr, N)
# #     for i in range(N):
# #         for j in range(N):
# #             if (mat[i][j] != tr[i][j]):
# #                 return False
# #     return True
 
 
# # # Driver code
# # mat = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
# # if (isSymmetric(mat, 3)):
# #     print("Yes")
# # else:
# #     print("No")


# # def check_symmetric(a, rtol=1e-05, atol=1e-08):
# #     return np.allclose(a, a.T, rtol=rtol, atol=atol)

# # def check_symmetric2(a, tol=1e-8):
# #     return np.all(np.abs(a-a.T) < tol)


# # # generate a random matrix and check to see
# # # if it has symmetric properties

# # # typehinting
# # def is_symmetric(A, tol=1e-8):
# #     return scipy.sparse.linalg.norm(A-A.T, scipy.Inf) < tol


# # A = np.random.rand(10, 10)
# # print(check_symmetric(A))






# # from scipy.sparse import csr_matrix

# # # Example: Create a sparse matrix
# # data = [1, 2, 3, 2]
# # row_indices = [0, 1, 2, 1]
# # col_indices = [0, 1, 2, 0]
# from scipy.sparse import csr_matrix

# # Example: Create a sparse matrix
# data = [1, 2, 3, 2]
# row_indices = [0, 1, 2, 1]
# col_indices = [0, 1, 2, 0]

# # Create a sparse matrix in Compressed Sparse Row format
# sparse_matrix = csr_matrix((data, (row_indices, col_indices)), shape=(3, 3))

# def is_symmetric(matrix: csr_matrix) -> bool:
#     # Check if the matrix is square
#     if matrix.shape[0] != matrix.shape[1]:
#         return False
#     # Check symmetry: A == A.T
#     return (matrix != matrix.T).nnz == 0  # Check if there are no nonzero differences

# # Check if the sparse matrix is symmetric
# print(is_symmetric(sparse_matrix))  # Output: True or False



import numpy as np

def reflect_point(point, line_point, line_direction):
    """
    Reflect a point across a line.
    :param point: Tuple (x, y) of the point to reflect
    :param line_point: A point on the line
    :param line_direction: Direction vector of the line
    :return: Reflected point as a tuple (x', y')
    """
    px, py = point
    lx, ly = line_point
    dx, dy = line_direction
    
    # Normalize the direction vector
    norm = np.sqrt(dx**2 + dy**2)
    dx /= norm
    dy /= norm
    
    # Vector from line point to the point
    vpx = px - lx
    vpy = py - ly
    
    # Projection of v onto the line direction
    proj_length = vpx * dx + vpy * dy
    
    # Reflect the point
    rx = px - 2 * (vpx - proj_length * dx)
    ry = py - 2 * (vpy - proj_length * dy)
    
    return (rx, ry)

def is_symmetric(polygon, line_point, line_direction):
    """
    Check if a polygon is symmetric about a line.
    :param polygon: List of tuples [(x1, y1), (x2, y2), ...] representing the polygon
    :param line_point: A point on the line of symmetry
    :param line_direction: Direction vector of the line of symmetry
    :return: True if symmetric, False otherwise
    """
    reflected = [reflect_point(p, line_point, line_direction) for p in polygon]
    # Check if reflected vertices match the original vertices
    return np.allclose(sorted(reflected), sorted(polygon))

# Example: Test for symmetry
polygon = [(0, 0), (2, 0), (1, np.sqrt(3))]
line_point = (1, 0)  # Point on the line
line_direction = (0, 1)  # Vertical line

print(is_symmetric(polygon, line_point, line_direction))  # Output: True or False
