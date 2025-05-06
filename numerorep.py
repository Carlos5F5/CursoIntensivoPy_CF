def mas_repetido(nums):

    cont = {}
    for num in nums:
        if num in cont:
            cont[num] +=1 

        else: 
            cont[num] = 1
    
    max_num = 0
    max_rep = 0

    for num, rep in cont.items():
        if rep > max_rep:
            max_rep = rep
            max_num = num
    return max_num, max_rep

nums = [12, 23, 34, 5, 6, 7, 9, 9,9,9,9,5,5,5,5,5,5,5,3,3,3,33]

numero, repeticiones = mas_repetido(nums)
print(f"El numero que mas se repite es {numero} y se repite {repeticiones} veces")
