# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/vectorToCsv.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.utils.consts import VALID_INPUT_TYPES


def vectorToCsv(mask: Matrix):
    """
     This builtin function  convert vector into csv string such as [1 0 0 1 1 0 1] = "1,4,5,7"
     Related to [SYSTEMDS-2662] dependency function for cleaning pipelines
    
    
    
    :param mask: Data vector (having 0 for excluded indexes)
    :return: indexes
    """

    params_dict = {'mask': mask}
    return Matrix(mask.sds_context,
        'vectorToCsv',
        named_input_nodes=params_dict)
