#!/usr/bin/python3
"""Import multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrixes."""
    return (np.matmul(m_a, m_b))
