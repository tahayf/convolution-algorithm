import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Question 1
# This is my own convolution function
def convoluted(x, n, y, m):

    result = [0]*(n+m-1)

    k = 0
    for i in range(len(x)):
        tmp = k
        for j in range(len(y)):
            result[k] = result[k] + y[j]*x[i]
            k += 1
        k = tmp + 1

    
    return result


n = int(input("Enter 'n' for x(n): "))
m = int(input("Enter 'm' for y(m): "))

x = input('Enter x(n) signal: ')
x = x.split()
for i in range(len(x)):
    x[i] = int(x[i])

y = input('Enter y(m) signal: ')
y = y.split()
for i in range(len(y)):
    y[i] = int(y[i])

# Question 2
# Vectoral shown of x(n),y(m),myConv,built-in function
print("\nx(n): ")
print(x)
print("\ny(m): ")
print(y)
sum = convoluted(x,n,y,m)
print("\nHere's convoluted signal by my convolution function: ")
print(sum)

pySum = np.convolve(x,y,'full')
print("\nHere's convoluted signal by Python's built-in convolution function: ")
print(pySum)

# Graphical shown of x(n),y(m),myConv,built-in function
xInd = int(input("\nGive the index of '0' point in signal x(n): "))
yInd = int(input("Give the index of '0' point in signal y(m): "))
xHorizontal = [i-xInd for i in range(n)]
yHorizontal = [i-yInd for i in range(m)]
sumHorizontal = [2-xInd-yInd+2*i for i in range(n+m-1)]
pySumHorizontal = [2-xInd-yInd+2*i for i in range(n+m-1)]

plt.stem(xHorizontal,x)
plt.title("first signal")
plt.ylabel("x(t)")
plt.xlabel("time")
plt.show()

plt.stem(yHorizontal,y)
plt.title("second signal")
plt.ylabel("y(t)")
plt.xlabel("time")
plt.show()

plt.stem(sumHorizontal,sum)
plt.title("convoluted signal by me")
plt.xlabel("time")
plt.show()

plt.stem(pySumHorizontal,pySum)
plt.title("convoluted signal by python")
plt.xlabel("time")
plt.show()

# Question 3 - Recording audio
freq = 10000
duration = 5
sd.default.samplerate = freq # This code line allows sounddevice module to play sounds with giving frequency otherwise default is 44.1kHz
choice = int(input("Press 1 for 5 sec recording and 0 for 10 sec: "))
if(choice == 1):
    print("Start speaking.(5 sec)")
    x1 = sd.rec(int(duration*freq), samplerate = freq, channels = 1) # channels might differ according to computer, if it doesn't work please try 2
    sd.wait()
    print("End of Recording.")
    flat = np.array(x1).flatten()
elif(choice == 0):
    print("Start speaking.(10 sec)")
    x2 = sd.rec(int(2*duration*freq), samplerate = freq, channels = 1) # channels might differ according to computer, if it doesn't work please try 2
    sd.wait()
    print("End of Recording.")
    flat = np.array(x2).flatten()
else:
    print("That's not valid choice.")

# Question 4

flag = 0
while(flag == 0):
    A = 0.8
    M = int(input("Enter 'M' Value for sigma notation: "))
    h = [0]*(400*M)
    h[0] = 1
    h.append(0)
    for i in range(M):
        h[(i+1)*400] = A*(i+1) 

    choice = int(input("Press 1 for my own convulation function and 0 for built-in function: "))
    if(choice == 1):
        convolved = convoluted(flat,len(flat),h,len(h))
    elif(choice == 0):
        convolved = np.convolve(flat,h)
    else:
        print("That's not valid choice.") 

    sd.play(convolved)
    flag = int(input("To continue convolving press 0: "))





