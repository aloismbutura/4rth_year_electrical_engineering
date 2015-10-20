#Creative Commons ShareAlike 4.0 International. The code is beerware; 
#if you see me at a party or bar and you've found my code helpful, 
#please buy me a round! :)

#Check your system python path
#!/usr/bin/python 
##!/usr/local/bin/python

#Original_Author Alois Mbutura Kiogora 
registration_number="F17/39168/2011"


#Demo code made on matplotlib version 1.1.1rc
#Demo code made with numpy version 1.10.1
#Use print numpy.__version__ to check numpy version
#Use print matplotlib.__version__ to check matplotlib version
#Do not change stuff marked with #ADVANCED

import numpy
import matplotlib.pylab as plt




##Parameters

f=10e4 #modulating frequency
#m=1.0 #modulation_index
m=0.2  #modulation_index
A=10.0 #This would give 10V p-p
A=A/2  #ADVANCED#Peak Amplitude of the carrier frequency waveform.
 
#This plots an array holding the indipendent time variables 
#Starts from t=0 and reaches 10e-4 with a spacing of 1e-8 per plot point
#The period of the highest frequency signal(carrier at90khz) is ~0.0000111... S
#So we can be sure to plot approximately 10 carrier frequency periods
t=numpy.arange(0,20e-4,1e-8) #ADVANCED

#x = numpy.linspace(0, 8 * numpy.pi, 3200) #Not used yet..mod this to have x as
#radians but not necessary.

##waveforms or functions
#The numpy cosine function only accepts stuff in radians so...
carrier_degrees_in_radians=numpy.radians(2*numpy.pi*9*f*t)
carrier_frequency=(A*numpy.cos(carrier_degrees_in_radians))

LSB_degrees_in_radians=numpy.radians(2*numpy.pi*8*f*t)
lower_sideband=(A*(m/2)*numpy.cos(LSB_degrees_in_radians))

USB_degrees_in_radians=numpy.radians(2*numpy.pi*10*f*t)
upper_sideband=(A*(m/2)*numpy.cos(USB_degrees_in_radians))

modulated_waveform=carrier_frequency-lower_sideband+upper_sideband

###Due to the difficulty in locating whether the carrier wave is being frequency\
###modulated, we shall carry out this method numerically as it cant work
###by inspection
##
###Due to the wave being periodic we shall trace along a horizontal line and
###obtain the time largest distances in between 2 half waves and store them in 
###an array
###We shall then test if the values are periodically related within a minimal
###degree of error due to interpolation.
###If yes,the wave has been frequency modulated.




plt.title('NARROW-BAND-FM-MODULATION FOURIER- %s'%registration_number)
plt.plot(t, carrier_frequency,label="Carrier-frequency-waveform")
plt.plot(t, lower_sideband, label= "Lower-Side-band-waveform")
plt.plot(t, upper_sideband, label= "Upper-side-band-waveform")
line2d=plt.plot(t, modulated_waveform,'r--',linewidth=2.0,
         label= "Output-modulated-waveform")
##xvalues = line2d[0].get_xdata()
##yvalues = line2d[0].get_ydata()
##abs_arr = numpy.abs(yvalues-0)
##print abs_arr
##sorted_abs_arr=numpy.sort(abs_arr)
##print sorted_abs_arr

#sorted_x_values=numpy.sort(xvalues)

plt.xlabel('time(Seconds)')
plt.ylabel('amplitude(Volts)')
plt.legend(bbox_to_anchor=(0., 1.035, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()
