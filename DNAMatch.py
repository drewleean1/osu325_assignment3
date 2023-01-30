#Andrew Lee
#CS 325
#Assignment 3
#Due Date: January 30, 2023



def dna_match_bottomup(DNA1, DNA2):
    #function that takes two given DNA and returns the largest substring, using a bottom up approach
    m = len(DNA1)                           #var names for the DNA strings
    n = len(DNA2)
    cache = [[0 for x in range(n+1)] for x in range(m+1)]       #initialize our 2D array
    for i in range(m + 1):                                      #for loop logic from Exploration 3.3
        #starting from 0, 0 in our 2D array, aka bottom up approach
        for j in range(n + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[m][n]                                          #return the bottom right value to get our answer

def dna_match_topdown_helper(DNA1, DNA2, m, n, cache):
    if m <= 0 or n <= 0:
        return 0
    if DNA1[m-1] == DNA2[n-1]:
        if cache[m-1][n-1] > 0:
            temporary_result = 1 + cache[m-1][n-1]
        else:
            temporary_result = 1 + dna_match_topdown_helper(DNA1, DNA2, m-1, n-1, cache)
    else:
        if cache[m-1][n] > 0 and cache[m][n-1] > 0:
            temporary_result = max(cache[m-1][n], cache[m][n-1])
        elif cache[m-1][n] > 0:
            temporary_result = max(cache[m-1][n], dna_match_topdown_helper(DNA1, DNA2, m, n-1, cache))
        elif cache[m][n-1] > 0:
            temporary_result = max(dna_match_topdown_helper(DNA1, DNA2, m-1, n, cache), cache[m][n-1])
        else:
            temporary_result = max(dna_match_topdown_helper(DNA1, DNA2, m-1, n, cache), dna_match_topdown_helper(DNA1, DNA2, m, n-1, cache))

    if cache[m][n] < temporary_result:
        cache[m][n] = temporary_result

    return cache[m][n]

def dna_match_topdown(DNA1, DNA2):

    m = len(DNA1)-1
    n = len(DNA2)-1
    if m <= 0 or n<= 0:
        return 0
    cache = [[0 for x in range(n+1)] for x in range(m+1)]
    return dna_match_topdown_helper(DNA1, DNA2, m, n, cache)

print(dna_match_topdown("ace", "abcdef"))