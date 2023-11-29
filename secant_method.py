particulars = """
Group Project members:

1. Tan Shieh Reine
2. Ryan Sim Junyue,
3. Natalia Tan Yu Ling
4. Tang Peng Siang
5. Shonim Shaheen"""
print(particulars)

#commented codes explain
'''
tried out codes that does not work
'''

##########
# STEP 1 #
##########

####1

def _is_function(f):
    
    #to check if f is callable 
    return callable(f)

#Test
print( _is_function( round ) )
  
    

####2

def _is_numeric(x):  
    
    #returns True if x is integer or float
    #else returns False
    return type(x) in (int, float)
    
    
#Test  
print( _is_numeric(True) )
    
    
####3   
def _is_valid_interval(x1, x2):
    
    #If-else statement, if x2 > 1, returns True, else returns False
    if (x2 > x1):
        return True
    else:
        return False
    
#Test
print( _is_valid_interval( 3, 2) ) 



####4
#added eps (a very small constant)
#to avoid issues related to floating-point arithmetic.
def _is_valid_tolerance(tol, x1, x2):
    
    eps = 1e-10
    return tol < 0.1 * (x2 - x1) + eps and abs(tol - (0.1 * (x2 - x1))) > eps
      
print( _is_valid_tolerance( 0.01, 1.0, 1.1 ) )



#################################################

### For example, to test _is_callable

def f(x):
    return 2*x

print( _is_function(f) )  ### Expected to be True, since f is a function
print( _is_function(2) )
### Expected to be False, since 2 is not a function 

#Test Cases
print( _is_numeric(True) ) # False 
print( _is_valid_interval( 3, 2) ) # False. Why?  
print( _is_valid_tolerance( 0.01 , 1.0, 1.1 ) ) # False. Why?

#Personal Test Cases
print( _is_numeric(67) )
print( _is_valid_tolerance( 0.10 , 4.0, 4.1 ) )



'''
-
'''

##########
# STEP 2 #
##########     

def _validation_checks(f,x1, x2, tol):
    
    #calling all functions
    #if all functins are true then function will return 'message':'inputs validated'
    #else it would return the message: 'message':'error in inputs'
    if(
        _is_function(f) and
        _is_numeric(x1) and 
        _is_numeric(x2) and
        _is_numeric(tol) and                        
        _is_valid_tolerance(tol, x1, x2)
      ):  
        return {'message':'inputs validated'}   
    else:
        return {'message':'error in inputs'}

#####################################

def _is_input_ok(d):
    
    #dictionary d['message'] will return True if it contains 'input validated'
    #dictionary d['message'] will return False if it contains 'error in inputs'
    #else the function would return None
    
    if d['message'] == 'inputs validated':
        return True
    elif d['message'] == 'error in inputs':
        return False
    else:
        return None

#Test Cases
def polynomial(x):
    return x*x - 3*x + 2

out = _validation_checks( polynomial, 0.5 , 1.5, 1e-2 )  
print(out) # {'message':'inputs validated'}
print( _is_input_ok(out) ) # True 


'''
-
'''

##########
# STEP 3 #
##########


def _is_same_sign(v1, v2):
    
    # + + = -, - - = +, - + = -
    #if the product of the values are negative,
    #that would mean the values are not the same sign
    return (v1 * v2) > 0
    
    '''
    if (v1 * v2 > 0):
        return True  
    elif(v1 < 0 or v2 < 0):
        return False
    '''

           
print(_is_same_sign(1, 2))
print(_is_same_sign(-1, 2))



'''
IMPLEMENT SECANT METHOD
'''

##########
# STEP 4 #
##########

def secant(f, x1, x2,tol):
    
    # given by assignment
    out = _validation_checks(f, x1, x2, tol)
   
    #algorithm step 2
    if not (_is_input_ok(out)):
        return out 
        
    #algorithm step 3
  
    f1 = f(x1)
    f2 = f(x2)
    
    if f1 * f2 > 0:
        out['message'] = 'f(x1) and f(x2) have the same sign'
        return out
       
    #step 4
    diff = abs(x2 - x1)
       
    #step 5
    iters = 0
       
    #step 6
    estimates = []
       
    #step 7
    while diff > tol:
        x3 = x2 - f2 * (x2 - x1) / (f2 - f1)
        iters += 1
        x1 = x2
        x2 = x3 
        f1 = f(x1)
        f2 = f(x2)
        estimates.append(x2)
        diff = abs(x2 - x1)
        
    #step 8
    root = (x2 + x1) / 2 
    
    #step 9.
    out.update({'root': root, 'iterations': iters, 'estimates': estimates })
    
    ###step 10
    return out
   

#test case
import math 

def ff(x):
    return 2*math.exp(-x) - x
    
result = secant(ff, 0, 2, 1e-3)
print(result)
result = secant(ff, 2, 2, 1e-3)
print(result)




