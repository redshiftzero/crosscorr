import numpy as np
from matplotlib import pyplot as plt


import compute

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def make_sky_dist(catalog, inform):
    plt.scatter(catalog['RA'], catalog['DEC'], linewidths=4, s=1, edgecolors='none')
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel('RA')
    plt.ylabel('DEC')
    plt.savefig('skyflatplotzoom_{}.png'.format(inform))
    plt.clf()
    plt.close('all')
    return None


def make_mag_dist(magnitude_p, magnitude_s, inform, band='i'):
    """
    Compare magnitude histograms of two datasets. 

    Args:
        magnitude_p (list, ndarray): photometric magnitudes
        magnitude_s (list, ndarray): spectroscopic magnitudes
        band (str): which magnitude band
        inform (optional [str]): timestamp referring to the run time 

    Returns:
        None
    """
    plt.figure()
    bins = np.linspace(10, 30, 50)
    plt.hist(magnitude_p, bins, normed=1, facecolor='red',
             alpha=0.5, label='Photometric')
    plt.hist(magnitude_s, bins, normed=1, facecolor='blue',
             alpha=0.5, label='Spectroscopic')
    plt.xlabel('{}-band magnitude'.format(band))
    plt.ylabel('dn/dm')
    plt.legend(loc='upper left')
    plt.savefig('magdist_{}.png'.format(inform))
    plt.close('all')
    return None
