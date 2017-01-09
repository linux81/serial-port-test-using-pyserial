import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyS0'
ser.open()


def srd():

    
	    a=ser.readline()
	    
	    b=a.replace('\n',"")
    
	
	    return long(b)


f = open('rngosc8.txt', 'w')


for i in range(10000):
	 a=srd()
	 
	 z=str(a)
	 f.write(z)
	 f.write('\n')
	 
	 

f.close()
ser.close()

print("zrobione")

a=np.loadtxt("rngosc8.txt")
a=np.reshape(a,(100,100))
a=np.mod(a,1000)

plt.imshow(a,cmap='hot')
plt.savefig("rngosc8.png")


#plt.savefig("alg"+str(i)+"_"+str(i+1)+".png")
#c=signal.convolve2d(a,b,mode='same')


