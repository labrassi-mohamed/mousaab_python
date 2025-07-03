def gen_fib (n):
    fibo_seq = [0,1]
    while len (fibo_seq)<n:
        next_term =fibo_seq[-1]+fibo_seq[-2]
        fibo_seq.append(next_term)
    return fibo_seq
user_input =input("Enter the lenght of fibonacci sequence : ")
num_input= int (user_input)

seq= gen_fib(user_input)
print (f"the first {num_input} terms of the Fibonacci Sequence is {seq}")