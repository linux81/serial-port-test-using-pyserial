
import serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyS0'
ser.open()


def srd():

    
	    a=ser.readline()
	    
	    b=a.replace('\n',"")
    
	
	    return int(b)
	    

	
	



