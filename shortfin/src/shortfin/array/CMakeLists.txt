# Copyright 2024 Advanced Micro Devices, Inc.
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

shortfin_cc_component(
  NAME
    shortfin_array
  HDRS
    array.h
    api.h
    dims.h
    dtype.h
    dtypes.inl
    storage.h
  SRCS
    array.cc
    dtype.cc
    storage.cc
    xtensor_bridge.cc
  COMPONENTS
    shortfin_local
    shortfin_support
  DEPS
    xtensor
)

shortfin_gtest_test(
  NAME shortfin_array_test
  SRCS
    array_test.cc
    dims_test.cc
    dtype_test.cc
)
