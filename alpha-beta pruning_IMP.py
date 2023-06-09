#alpha beta pruning
MAX, MIN = 1000, -1000
def ABprune(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = MIN
 
        # Recur for left and right children
        for i in range(0, 2):
             
            val = ABprune(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = MAX
        for i in range(0, 2):
          
            val = ABprune(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
      

values = [2, 4, 6, 8, 1, 2, 10, 12] 
print("The optimal value is :", ABprune(0, 0, True, values, MIN, MAX))
