"print 1 to 10 numbers by using recursion"
def function(count):
    if count == 21:
        return
    print(count*2)
    function(count + 1)
function(1)