#!/usr/bin/env python
"""
Copyright 2009-2014 Marek Rudnicki

This file is part of cochlea.

cochlea is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

cochlea is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with cochlea.  If not, see <http://www.gnu.org/licenses/>.


Description
-----------

Run the external MAP model.

"""
from __future__ import division, absolute_import, print_function

__author__ = "Marek Rudnicki"


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as dsp

import thorns as th

import cochlea
from cochlea.external import run_matlab_auditory_periphery

def main():

    fs = 48e3

    ### Make sound
    tmax = 0.03
    t = np.arange(0, tmax, 1/fs)
    s = dsp.chirp(t, 80, t[-1], 16000)
    sound = cochlea.set_dbspl(s, 50)



    ### Run model
    anf = run_matlab_auditory_periphery(
        sound,
        fs,
        anf_num=(100,50,20),
        cf=(125, 16000, 80),
        seed=0,
    )



    ### Accumulate spike trains
    anf_acc = th.accumulate(anf, keep=['cf', 'duration'])
    anf_acc.sort('cf', ascending=False, inplace=True)



    ### Plot auditory nerve response
    fig, ax = plt.subplots(2, 1, sharex=True)
    th.plot_signal(
        signal=sound,
        fs=fs,
        ax=ax[0]
    )
    th.plot_neurogram(
        anf_acc,
        fs,
        ax=ax[1]
    )
    plt.show()



if __name__ == "__main__":
    main()
