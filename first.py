from numba import cuda
import numpy as np
import numpy

@cuda.jit('void(int32[:], int32[:])')
def foo(aryA, aryB):
    ...

griddim = 1, 2
blockdim = 3, 4

aryA = numpy.arange(10, dtype=np.int32)
aryB = numpy.arange(10, dtype=np.float32)
foo[griddim, blockdim](aryA, aryB)