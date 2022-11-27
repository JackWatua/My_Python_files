from recap import searches
numbers= [a+1 for a in range(10)]
result = searches()
res= result.linear_search(numbers, 12)
result.verify_result(res)
