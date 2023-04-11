import numpy as np

eig = np.linalg.eig
matrix = np.matrix
testmatrix = matrix([[0,1,1,1,0,0,0,0],
                     [1,0,0,1,1,0,0,0],
                     [1,0,0,0,0,1,1,1],
                     [1,1,0,0,1,0,0,0],
                     [0,1,0,1,0,0,0,0],
                     [0,0,1,0,0,0,1,0],
                     [0,0,1,0,0,1,0,1],
                     [0,0,1,0,0,0,1,0]]) # 매트릭스 생성

print(eig(testmatrix))
value = eig(testmatrix)  #[0] #Eigenvalue
vector = eig(testmatrix)  #[1] #Eigenvector

print('Eigenvalue :', value)
print('Eigenvector :', vector)