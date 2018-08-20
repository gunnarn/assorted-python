import math

def hztosemi(hz, ref=16.352):
    '''
        Converts hz to semitones based on the formula found here:
        http://www2.ling.su.se/staff/hartmut/bark.htm
    '''
    try:
	    value = 12*math.log(hz/ref,2)
    except TypeError:
    	value = 12*math.log(float(hz)/ref,2)
    return(value)


if __name__=='__main__':
	
	while True:
	    r = raw_input('Enter Hz (or two values to get the slope): ')
	    r = r.split()

	    if len(r) == 2:
	    	s = hztosemi(r[1], 1) - hztosemi(r[0], 1)

	    elif len(r) == 1:

	    	s = hztosemi(r[0], 1)


	    print(str(s)+'\n')
