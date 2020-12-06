



def fibo(n):
    fibonacci = []
    n1, n2 = 1, 1
    count = 0
    while count<=n:
        n12 = n1+n2
        fibonacci.append(n12)
        n1 = n2
        n2 = n12
        count = n12
    return fibonacci
    
    
def get(n):
    comb = []
    n = n
    step_sizes = fibo(n)

    if n < min(step_sizes):
        return comb

    for step_size in step_sizes:
        if n == step_size:
            comb.append([step_size])
        elif n > step_size:
            child_combos = get(n - step_size)
                
            for child_combo in child_combos:
                comb.append([step_size] + child_combo)
                    
                    
    for i in range(len(comb)):
        comb[i].sort()
        
    res = [list(tupl) for tupl in {tuple(item) for item in comb}]
        
    return res
    
    
x = get(20)
print(x)
    
    

























# =============================================================================
# 
# 
# 
#  
# 
# app = Flask(__name__) 
#   
#  
# @app.route('/fib', methods = ['GET', 'POST']) 
# def fib(y): 
#     if(request.method == 'GET'): 
#   
#         def fibonacci(n):
#             fib = []
#             n1, n2 = 1,1
#             count = 0
#             while count<=n:
#                 n12 = n1+n2
#                 fib.append(n12)
#                 n1 = n2
#                 n2 = n12
#                 count = n12
#         
#         return fib
# 
# 
# 
#         def Combinations(num_steps, step_sizes):
#             comb = []
#     
#             if num_steps < min(step_sizes):
#                 return comb
#     
#             for step_size in step_sizes:
#                 if num_steps == step_size:
#                     comb.append([step_size])
#                 elif num_steps > step_size:
#                     child_combos = Combinations(num_steps - step_size, step_sizes)
#                     for child_combo in child_combos:
#                         comb.append([step_size] + child_combo)
#             return comb
#         
#         return jsonify({'fib': Combinations(y, fibonacci(y))}) 
#   
#   
#  
# if __name__ == '__main__': 
#   
#     app.debug = True
#     app.run(host = '127.0.0.1', port = 5000) 
#     fib(11)
# =============================================================================
