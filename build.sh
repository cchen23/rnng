#!/bin/bash

export BOOST_DIR="/home/cathychen/packages/boost_1_73_0"
export EIGEN_DIR="/home/cathychen/packages/eigen-3.3.7"
export MKL_DIR="/opt/intel/mkl"
export CC=`which gcc`
export CXX=`which g++`

mkdir build
cd build
echo ${EIGEN_DIR}
cmake \
    -DEIGEN3_INCLUDE_DIR=$EIGEN_DIR \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_COMPILER=`which g++-5` \
    -DCMAKE_C_COMPILER=`which gcc-5` \
    ..
make -j4

