# Copyright 2024 Advanced Micro Devices, Inc.
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from typing import Optional
import torch

from sharktank import ops
from sharktank.types import Theta
from .base import ThetaLayer


class TokenEmbeddingLayer(ThetaLayer):
    def __init__(
        self,
        theta: Theta,
        *,
        weight_name: str = "weight",
        dtype: Optional[torch.dtype] = torch.float32,
    ):
        super().__init__(theta)
        self.weight = self.theta_tensor(weight_name)
        self.dtype = dtype

    def forward(self, input: torch.Tensor):
        return ops.embedding_lookup(input, self.weight, dtype=self.dtype)
