#!/usr/bin/env python

#numpy/scipy is the scientific programming toolkit..first import it.
import numpy

#We are testing vector identities.
#This code implimented on python2.7 and ipython ver 0.12

#Three sample 3D vectors implimented as arrays.
#Change these as per how you wish as long as the dimensions match.
vector_a=numpy.array([5,6,7])
vector_b=numpy.array([7,6,5]) 
vector_c=numpy.array([1,2,3])
empty_vector=numpy.array([0,0,0])

#Identity_1-> Prove BXA=-AXB
##vector_result_first=numpy.cross(vector_a,vector_b)
##vector_result_second=numpy.cross(vector_b,vector_a)
##vector_result_second=vector_result_second*-1 #matrix multiplication by a scalar
##print vector_result_first
##print vector_result_second
##if (vector_result_first == vector_result_second).all():
##    print "Both vectors are equal,law proven BXA=-AXB"
##else:
##    print "Both vectors are unequal,law broken BXA=-AXB"

#Identity2 -> Prove distributive law AX(B+C)=AXB+AXC
##vector_result_first=numpy.cross(vector_a,(vector_b+vector_c))
##vector_result_second=(numpy.cross(vector_a,vector_b))+(numpy.cross(vector_a,vector_c))
##print vector_result_first
##print vector_result_second
##if (vector_result_first == vector_result_second).all():
##    print "Both vectors are equal,law proven AX(B+C)=AXB+AXC"
##else:
##    print "Both vectors are unequal,law broken AX(B+C)=AXB+AXC"
##    

#Identity_3 -> Prove AX(BXC)!=(AXB)XC
##vector_result_first=numpy.cross(vector_a,numpy.cross(vector_b,vector_c))
##vector_result_second=numpy.cross(numpy.cross(vector_a,vector_b),vector_c)
##print vector_result_first
##print vector_result_second
##if (vector_result_first == vector_result_second).all():
##    print "Both vectors are unequal,law broken AX(BXC)!=(AXB)XC"
##else:
##    print "Both vectors are unequal,law proven AX(BXC)!=(AXB)XC"
##    
#VECTOR TRIPLE PRODUCTS

#Proof if A or B is zero the resultant vector is zero
##vector_result_first=numpy.cross(empty_vector,vector_a)
##print empty_vector
##print vector_a
##print vector_result_first
