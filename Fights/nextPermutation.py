def nextPermutation(permutation):                                                          
                                                                                           
    for i in range(len(permutation) - 2, -1, -1):                                          
        if permutation[i] < permutation[i + 1]:                                            
            index = i + 1                                                                  
            tmp = permutation[i]                                                           
            suffix = []                                                                    
            for j in range(i + 1, len(permutation)):                                       
                if permutation[j] > permutation[i] and permutation[j] < permutation[index]:
                    index = j                                                              
            permutation[i] = permutation[index]                                            
            permutation[index] = tmp                                                       
            suffix = permutation[i + 1:]                                                   
            suffix.reverse()                                                               
            permutation = permutation[0:i + 1] + suffix                                    
            return permutation                                                             
                                                                                           
    permutation.sort()                                                                     
    return permutation                                                                     
