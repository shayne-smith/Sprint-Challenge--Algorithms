#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    n = 2                       # runs 2 times
    while (a < n * n * n):      # a < 8
      a = a + n * n             # a = 4, a = 8 
    
    n = 3                       # runs 3 times
    while (a < n * n * n):      # a < 27
      a = a + n * n             # a = 9, a = 18, a = 27 

    n = 4                       # runs 4 times
    while (a < n * n * n):      # a < 64
      a = a + n * n             # a = 16, a = 32, a = 48, a = 64

               Time Complexity: # O(n) linear time because the code snippet 
                                # runs n times given an input size of n

b)  sum = 0
    n = 5
    for i in range(n):          # runs 5 times # O(n)
        j = 1

                                # while loops runs 3 times
        while j < n:            # j < 5 
        j *= 2                  # j = 2, j = 4, j = 6
        sum += 1                # sum = 1, sum = 2, sum = 3

    sum = 0
    n = 10
    for i in range(n):          # runs 10 times # O(n)
        j = 1

                                # while loops runs 5 times
        while j < n:            # j < 10
        j *= 2                  # j = 2, j = 4, j = 6, j = 8, j = 10
        sum += 1                # sum = 1, sum = 2, sum = 3, sum = 4, sum = 5

               Time Complexity: # O((1/2)*n^2) simplifies to O(n^2) quadratic time
                                # because of the nested for and while loops


c)  def bunnyEars(bunnies):              # bunnies = 4 
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1)  # 2 + bunnyEars(3), 2 + bunnyEars(2), 2 + bunnyEars(1), 2 + bunnyEars(0)
                                         # returns 8 and runs 4 times

                        Time Complexity: # O(n) because the code recursively runs n times before 
                                         # a base case is triggered, thereby ending the call stack

## Exercise II
# To minimize the number of broken eggs, floor f should be set to the top floor of the n-story building.
# This way, eggs only break when thrown from the top floor of the building. Throwing eggs from all other n-1 floors
# below the top floor does not result in broken eggs, thereby minimizing the number of broken eggs.
# 
# A doubly-linked list is an appropriate data structure to store floor information because there is a tail and head
# attribute. This allows us to access the tail node and set floor f to the tail node with O(1) runtime complexity. 
# This proposed algorithm assumes floor 1 (ground level) is stored at the head node of the doubly-linked list.

# Runtime complexity: O(1)                                               

