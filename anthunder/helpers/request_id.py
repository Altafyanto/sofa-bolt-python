# coding=utf-8
"""
    Copyright (c) 2018-present, Ant Financial Service Group

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ------------------------------------------------------
   File Name : request_id
   Author : jiaqi.hjq
"""
import logging
from random import randint
from itertools import cycle, chain
from six.moves import range

logger = logging.getLogger(__name__)

_max = 0x7fffffff  # 4 bytes signed int
_start = randint(0, _max)
RequestId = cycle(chain(range(_start, _max + 1), range(0, _start)))
