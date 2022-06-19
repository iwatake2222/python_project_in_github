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
Test calculator module
"""

import calculator


def test_add():
    """Test calculator.add
    """
    assert calculator.add(1, 2) == 3


def test_sub():
    """Test calculator.sub
    """
    assert calculator.sub(3, 4) == -1


def test_mul():
    """Test calculator.mul
    """
    assert calculator.mul(5, 6) == 30
