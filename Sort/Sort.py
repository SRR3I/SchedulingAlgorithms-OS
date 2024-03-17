def as_arrival_time(matrix,Priority=False,indx=0,end=0):
   Column=1
   if Priority:
      Column=2
   if end==0:
      length = len(matrix)
   else:
      length=end
   for i in range(indx,length):
      min_index = i
      for j in range(i + 1, length):
         if matrix[j][Column] < matrix[min_index][Column]:
               min_index = j
         elif matrix[j][Column]==matrix[min_index][Column]:
            if matrix[j][0]<matrix[min_index][0]:
               min_index=j
      for k in range(5):
         matrix[i][k], matrix[min_index][k] = matrix[min_index][k], matrix[i][k]
   return matrix


def as_burst_time(matrix,indx=0,end=0):
   if end==0:
      length = len(matrix)
   else:
      length=end
   for i in range(indx,length):
      min_index = i
      for j in range(i + 1, length):
         if matrix[j][2] <  matrix[min_index][2]:
               min_index = j
         elif matrix[j][2]==matrix[min_index][2]:
            if matrix[j][1]<matrix[min_index][1]:
               min_index=j
      for k in range(5):
         matrix[i][k], matrix[min_index][k] = matrix[min_index][k], matrix[i][k]
   return matrix


def as_priority(matrix,indx=0,end=0):
   if end==0:
      length = len(matrix)
   else:
      length=end
   for i in range(indx,length):
      min_index = i
      for j in range(i + 1, length):
         if matrix[j][1] <  matrix[min_index][1]:
               min_index = j
         elif matrix[j][1]==matrix[min_index][1]:
            if matrix[j][0]<matrix[min_index][0]:
               min_index=j
      for k in range(6):
         matrix[i][k], matrix[min_index][k] = matrix[min_index][k], matrix[i][k]
   return matrix
