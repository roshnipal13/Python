"recursion using parameter"
def function(x , n):
    if n == 0:
        return
    print(x)
    function(x ,n-1)

function(15,5)
