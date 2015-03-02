#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

Run Zilany et al. (2014) model and plot a PSTH.

Unlike other examples, this script does not need any extra (unusual)
dependencies (e.g. thorns) for visualization.  It depends only on
matplotlib.  If you want to run more advanced examples, you will need
to install `thorns'.

"""

from __future__ import division, absolute_import, print_function

__author__ = "Marek Rudnicki"


import numpy as np
import matplotlib.pyplot as plt

import cochlea

def main():
    fs = 100e3
    cf = 8e3

    ### Make sound
    t = np.arange(0, 0.1, 1/fs)
    tone = np.sin(2*np.pi*t*cf)

    tone = cochlea.set_dbspl(tone, 20)

    pad = np.zeros(50e-3 * fs)
    sound = np.concatenate( (tone, pad) )



    ### Run model
    anf = cochlea.run_zilany2014(
        sound,
        fs,
        anf_num=(200,0,0),
        cf=cf,
        seed=0,
        powerlaw='approximate',
        species='human'
    )


    print(anf.head(20))


    ### Plot PSTH
    all_spikes = np.concatenate(anf.spikes)
    tmax = anf.duration.max()

    bin_size = 1e-3

    fig,ax = plt.subplots()

    ax.hist(
        all_spikes,
        bins=int(tmax/bin_size),
        range=(0,tmax),
        weights=np.ones_like(all_spikes)/bin_size/len(anf)
    )

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Rate [spikes/s]")
    ax.set_title("PSTH")

    plt.show()


if __name__ == "__main__":
    main()
