#Nested functions: Nonlocal variables

#1
#In this case it will return 'This is Nested' and
# 'This is Enclosed'

def enclosed():
    var = 'This is Enclosed'
    def nested():
        # nonlocal var
        var = 'This is Nested'
        print(var)
    nested()
    print(var)
enclosed()

#But, if we declare the variable var as nonlocal inside the
#Nested function, then both print() statement will output
# 'This is nested and modified'

def enclosed():
    var = 'This is Enclosed'
    def nested():
        nonlocal var
        var = 'This is Nested'
        print(var)
    nested()
    print(var)
enclosed()
