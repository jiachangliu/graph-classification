# Adjust accordingly
# ROOTDIR=/home/hopan/MLGkernel
ROOTDIR=/data/jl888/Research/baselines/graph-classification/MLGkernel
# include ../../Makefile.base
include /data/jl888/Research/baselines/graph-classification/MLGkernel/Makefile.base

# CC=g++
CC=/data/jl888/anaconda3/envs/gcc/bin/x86_64-conda_cos6-linux-gnu-cc
CFLAGS= -std=c++11 -I $(INCLUDEDIR) -I $(UTILITYDIR) -I $(FILETYPESDIR) -I $(MATRIXDIR) 

MKLVARS+= -lmkl_rt
# MLGDIR=/home/hopan/MLGkernel/MLGkernel
MLGDIR=/data/jl888/Research/baselines/graph-classification/MLGkernel/MLGkernel
ALLOBJECTS=  $(MATRIXDIR)/*.o  $(MLGDIR)/*.o $(UTILITYDIR)/*.o

# These need to be set according to your python location/distribution
# PYINCLUDE= -I/software/python-3.4-2015q1-el6-x86_64/include/python3.4m \
# -I/software/python-3.4-2015q1-el6-x86_64/lib/python3.4/site-packages/numpy/core/include
# PYLIBS= -L/Library/Frameworks/Python.framework/Versions/3.4/lib -ldl -framework CoreFoundation -lpython3.4m

PYINCLUDE= -I/data/jl888/anaconda3/envs/gcc/include/python3.6m \
-I/data/jl888/anaconda3/envs/gcc/lib/python3.6/site-packages/numpy/core/include
PYLIBS= -L/data/jl888/anaconda3/envs/gcc/lib -ldl -framework CoreFoundation -lpython3.6m

MLGK_wrap.cxx: MLGK.i $(MLGDIR)/*.hpp $(MATRIXDIR)/*.hpp $(UTILITYDIR)/*.hpp
	swig -python -shadow -c++ MLGK.i

_MLGK.so: MLGK_wrap.cxx MLGK.cpp
	$(CC) -fPIC -shared MLGK_wrap.cxx MLGK.cpp  \
-o _MLGK.so $(CFLAGS) $(PYINCLUDE) $(ALLOBJECTS) -I $(INCLUDEDIR)

all: MLGK_wrap.cxx _MLGK.so

clean: 
	rm -f $(OBJECTS)  MLGK_wrap.cxx _MLGK.so

anew: clean all
