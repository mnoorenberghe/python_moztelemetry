#!/usr/bin/env python
# encoding: utf-8

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
This module implements test coverage for the stats functions in stats.py.
"""
from moztelemetry import stats


def test_mann_whitney_u():
    SAMPLE1 = {1: 5, 2: 1, 3: 4, 4: 2, 5: 3}
    SAMPLE2 = {1: 1, 2: 5, 3: 2, 4: 4, 5: 3}

    # Basic test.
    assert stats.mann_whitney_u(SAMPLE1, SAMPLE2) == 94.5

    # Test min(U1, U2).
    assert stats.mann_whitney_u(SAMPLE2, SAMPLE1) == 94.5

    # Test exact same samples.
    assert stats.mann_whitney_u(SAMPLE1, SAMPLE1) == 112.5

    # Test varying sample sizes.
    assert stats.mann_whitney_u(SAMPLE1, {1: 1, 5: 5}) == 20
