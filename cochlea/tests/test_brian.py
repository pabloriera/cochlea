# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

__author__ = "Marek Rudnicki"
__copyright__ = "Copyright 2014, Marek Rudnicki"
__license__ = "GPLv3+"


from numpy.testing import assert_equal
import pandas as pd

import cochlea



def test_make_brian_group():

    trains = pd.DataFrame([
        {'duration': 100e-3, 'spikes': [10e-3, 30e-3], 'cf': 333},
        {'duration': 100e-3, 'spikes': [40e-3, 50e-3], 'cf': 333},
        {'duration': 100e-3, 'spikes': [60e-3, 70e-3], 'cf': 333},
    ])


    group = cochlea.make_brian_group(trains)

    assert_equal(len(trains), len(group))
