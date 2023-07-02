#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        old_row = triangle[i - 1]
        
        for j in range(1, i):
            row.append(old_row[j - 1] + old_row[j])
        
        row.append(1)
        triangle.append(row)
    
    return triangle
