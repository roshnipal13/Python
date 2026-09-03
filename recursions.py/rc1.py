" print rose 4 time by using recursion"
"""count = 0
def function():
    global count
    if count == 4:
        return 
    print("roshni")
    count += 1
    function()
function()"""
def function(count):
    if count == 4:
        return
    print("roshni")
    function(count + 1)

function(0)
