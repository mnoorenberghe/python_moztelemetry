#!/usr/bin/env python
# encoding: utf-8

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import division


def mann_whitney_u(sample1, sample2):
    """
    Computes the Mann-Whitney rank test on both samples.

    Each sample is expected to be of the form::

        {1: 5, 2: 20, 3: 12, ...}

    Returns the U statistic, equal to min(U for sample1, U for sample2).

    """
    # Merge dictionaries, adding values if keys match.
    sample = sample1.copy()
    for k, v in sample2.items():
        sample[k] = sample.get(k, 0) + v

    # Create a ranking dictionary using same keys for lookups.
    rank = 1
    ranks = {}
    for k in sorted(sample.keys()):
        n = sample[k]
        ranks[k] = rank + (n - 1) / 2
        rank += n

    # Calculate Mann-Whitney U for both samples.
    sum_of_ranks1 = sum([sample1[k] * ranks[k] for k, v in sample1.items()])
    sum_of_ranks2 = sum([sample2[k] * ranks[k] for k, v in sample2.items()])

    size1 = sum(sample1.values())
    size2 = sum(sample2.values())

    U1 = sum_of_ranks1 - (size1 * (size1 + 1) / 2)
    U2 = sum_of_ranks2 - (size2 * (size2 + 1) / 2)

    return min(U1, U2)
