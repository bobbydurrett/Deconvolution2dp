"""

https://rosettacode.org/wiki/Deconvolution/2D%2B

Working on simple 2 dimensional example using test data from the
RC task.

Python fft:

https://docs.scipy.org/doc/numpy/reference/routines.fft.html

"""

import numpy

h =  [
      [-8, 1, -7, -2, -9, 4], 
      [4, 5, -5, 2, 7, -1], 
      [-6, -3, -3, -6, 9, 5]]
f =  [
      [-5, 2, -2, -6, -7], 
      [9, 7, -6, 5, -7], 
      [1, -1, 9, 2, -7], 
      [5, 9, -9, 2, -5], 
      [-8, 5, -2, 8, 5]]
g=   [
      [40, -21, 53, 42, 105, 1, 87, 60, 39, -28], 
      [-92, -64, 19, -167, -71, -47, 128, -109, 40, -21], 
      [58, 85, -93, 37, 101, -14, 5, 37, -76, -56], 
      [-90, -135, 60, -125, 68, 53, 223, 4, -36, -48], 
      [78, 16, 7, -199, 156, -162, 29, 28, -103, -10], 
      [-62, -89, 69, -61, 66, 193, -61, 71, -8, -30], 
      [48, -6, 21, -9, -150, -22, -56, 32, 85, 25]]
       
def deconv(a, b):
    """
    
    Returns function c such that b * c = a.
    
    https://en.wikipedia.org/wiki/Deconvolution
    
    """
    
    # Convert larger polynomial using fft

    ffta = numpy.fft.fftn(a)
    
    # Get it's shape so fftn will expand
    # smaller polynomial to fit.
    
    ashape = numpy.shape(ffta)
    
    # Convert smaller polynomial with fft
    # using the shape of the larger one

    fftb = numpy.fft.fftn(b,ashape)
    
    # Divide the two in frequency domain

    fftquotient = ffta / fftb
    
    # Convert back to polynomial coefficients using ifft
    # Should give c but with some small extra components

    c = numpy.fft.ifftn(fftquotient)
    
    # Get rid of imaginary part and round up to 6 decimals
    # to get rid of small real components

    trimmedc = numpy.around(numpy.real(c),decimals=6)
    
    # Trim zeros and eliminate
    # empty rows of coefficients

    cleanc = []

    for l in trimmedc:
        newlist = list(numpy.trim_zeros(l))
        if len(newlist) > 0:
            cleanc.append(list(numpy.trim_zeros(l)))
            
    return cleanc

print(deconv(g,h))