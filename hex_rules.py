
import numpy as np

def initializeGrid(dimX, dimY, ratio=0.5):
  # In this program, the grid configuration only works if there is even rows and even columns.
  if dimY % 2 == 1:
    raise Exception("Please have a grid with an even number of rows...")
  if dimX % 2 == 1:
    raise Exception("Please have a grid with an even number of columns...")
  M = np.zeros((dimY, dimX))
  for i in range(dimY):
    for j in range(dimX):
      M[i,j] = np.random.binomial(1, ratio)
  return M

def countAliveNeighbors(M,i,j):
  count = 0
  dimY = M.shape[0]
  dimX = M.shape[1]
  # if i is even
  if i % 2 == 0:
    if j != dimX - 1 and i != dimY - 1:
      count += M[i,j-1]
      count += M[i,j+1]
      count += M[i-1,j]
      count += M[i-1,j+1]
      count += M[i+1,j]
      count += M[i+1,j+1]
    elif j == dimX - 1 and i != dimY - 1:
      count += M[i,j-1]
      count += M[i,0]
      count += M[i-1,j]
      count += M[i-1,0]
      count += M[i+1,j]
      count += M[i+1,0]
    elif j != dimX - 1 and i == dimY - 1:
      count += M[i,j-1]
      count += M[i,j+1]
      count += M[i-1,j]
      count += M[i-1,j+1]
      count += M[0,j]
      count += M[0,j+1]
    else:
      count += M[i,j-1]
      count += M[i,0]
      count += M[i-1,j]
      count += M[i-1,0]
      count += M[0,j]
      count += M[0,0]
  # if i is odd
  else:
    if j != dimX - 1 and i != dimY - 1:
      count += M[i,j-1]
      count += M[i,j+1]
      count += M[i-1,j-1]
      count += M[i-1,j]
      count += M[i+1,j-1]
      count += M[i+1,j]
    elif j == dimX - 1 and i != dimY - 1:
      count += M[i,j-1]
      count += M[i,0]
      count += M[i-1,j-1]
      count += M[i-1,j]
      count += M[i+1,j-1]
      count += M[i+1,j]
    elif j != dimX - 1 and i == dimY - 1:
      count += M[i,j-1]
      count += M[i,j+1]
      count += M[i-1,j-1]
      count += M[i-1,j]
      count += M[0,j-1]
      count += M[0,j]
    else:
      count += M[i,j-1]
      count += M[i,0]
      count += M[i-1,j-1]
      count += M[i-1,j]
      count += M[0,j-1]
      count += M[0,j]
  return count

def rule0(M):
  dimY = M.shape[0]
  dimX = M.shape[1]
  newM = np.zeros((dimY,dimX))
  for i in range(dimY):
    for j in range(dimX):
      alive_neighbors = countAliveNeighbors(M, i, j)
      if M[i,j] == 0:
        if alive_neighbors == 0:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
      else:
        if alive_neighbors == 2 or alive_neighbors == 3:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
  print('generation changed!')
  return newM

def rule1(M):
  dimY = M.shape[0]
  dimX = M.shape[1]
  newM = np.zeros((dimY,dimX))
  for i in range(dimY):
    for j in range(dimX):
      alive_neighbors = countAliveNeighbors(M, i, j)
      if M[i,j] == 0:
        if alive_neighbors == 1:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
      else:
        if alive_neighbors == 2 or alive_neighbors == 3:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
  print('generation changed!')
  return newM

def rule2(M):
  dimY = M.shape[0]
  dimX = M.shape[1]
  newM = np.zeros((dimY,dimX))
  for i in range(dimY):
    for j in range(dimX):
      alive_neighbors = countAliveNeighbors(M, i, j)
      if M[i,j] == 0:
        if alive_neighbors == 2:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
      else:
        if alive_neighbors == 2 or alive_neighbors == 3:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
  print('generation changed!')
  return newM

def rule3(M):
  dimY = M.shape[0]
  dimX = M.shape[1]
  newM = np.zeros((dimY,dimX))
  for i in range(dimY):
    for j in range(dimX):
      alive_neighbors = countAliveNeighbors(M, i, j)
      if M[i,j] == 0:
        if alive_neighbors == 3:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
      else:
        if alive_neighbors == 2 or alive_neighbors == 3:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
  print('generation changed!')
  return newM

def rule4(M):
  dimY = M.shape[0]
  dimX = M.shape[1]
  newM = np.zeros((dimY,dimX))
  for i in range(dimY):
    for j in range(dimX):
      alive_neighbors = countAliveNeighbors(M, i, j)
      if M[i,j] == 0:
        if alive_neighbors == 1 or alive_neighbors >= 4:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
      else:
        if alive_neighbors >= 1 and alive_neighbors <= 4:
          newM[i,j] = 1
        else:
          newM[i,j] = 0
  print('generation changed!')
  return newM