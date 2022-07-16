# Copyright 2022 iwatake2222
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Logic functinos for calculator
"""

import calculator.logger_factory

logger = calculator.logger_factory.LoggerFactory.create(__name__)


def add(lval: int, rval: int) -> int:
    """
    Add values

    Parameters
    ----------
    lval : int
        left value
    rval : int
        right value

    Returns
    -------
    ret : int
        lval + rval

    Examples
    --------
    >>> ret = add(1, 2)
    >>> ret
    3
    """

    logger.debug('call add')
    ret = lval + rval
    return ret


def sub(lval: int, rval: int) -> int:
    """
    Subtract values

    Parameters
    ----------
    lval : int
        left value
    rval : int
        right value

    Returns
    -------
    ret : int
        lval - rval

    Examples
    --------
    >>> ret = sub(1, 2)
    >>> ret
    -1
    """

    logger.debug('call sub')
    ret = lval - rval
    return ret


def mul(lval: int, rval: int) -> int:
    """
    Multiply values

    Parameters
    ----------
    lval : int
        left value
    rval : int
        right value

    Returns
    -------
    ret : int
        lval * rval

    Examples
    --------
    >>> ret = mul(2, 3)
    >>> ret
    6
    """

    logger.debug('call mul')
    ret = lval * rval
    return ret
