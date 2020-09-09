#!/bin/bash

export BOOST_DIR="/home/dfried/projects/boost_1_60_0//"
export EIGEN_DIR="${HOME}/projects/eigen/"
#DYNET_ROOT="${HOME}/projects/dynet_rnng/"
export MKL_DIR="/opt/intel/mkl"
export CC=`which gcc`
export CXX=`which g++`

mkdir build
cd build
cmake \
    -DEIGEN3_INCLUDE_DIR=$EIGEN_DIR \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_COMPILER=`which g++-5` \
    -DCMAKE_C_COMPILER=`which gcc-5` \
    ..
make -j4
