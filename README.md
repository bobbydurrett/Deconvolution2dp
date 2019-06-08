# Deconvolution2dp
Rosetta Code Deconvolution/2D+ task for Python

https://rosettacode.org/wiki/Deconvolution/2D%2B

https://en.wikipedia.org/wiki/Deconvolution

https://docs.scipy.org/doc/numpy/reference/routines.fft.html

https://rosettacode.org/wiki/Deconvolution/1D

Trying to figure out what this means:

h: [
      [-8, 1, -7, -2, -9, 4], 
      [4, 5, -5, 2, 7, -1], 
      [-6, -3, -3, -6, 9, 5]]
      
Is this

h(x,y) = -8x^5+x^4-7x3-2x^2-9x+4 +
         4x^5y+5x4y-5x^3y+2x^2y+7xy-y +
         -6x^5y^2-3x^4y^2-3x^3y^2-6x^2y^2+9xy^2 +5y^2
         
Number of lists indicates y degree
First list is y^0 = 1
second y
third y^2
etc.

I guess 2 d FFT would give the function's value at enough
points to determine the function.

I guess 18 points in this case.

Would be nice to use n dimensional numpy fft
so I don't have to manually convert this to
1d fft.

Then it would just be like the 1d case.

Works except can't divide by zero in frequency domain in some
cases

https://math.stackexchange.com/questions/380720/is-deconvolution-simply-division-in-frequency-domain

