"print  1 to n number"
"""def fun(i , n):
    if i > n:
        return
    print(i)
    fun(i+1 , n)
fun(1 , 20)"""



"backtracking"
def fun(i , n):
    if i > n:
        return
    fun(i + 1, n)
    print(i)
fun(1,5)
