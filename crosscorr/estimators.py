import numpy as np
import esutil


def count_pairs(ra1, dec1, ra2, dec2, theta_bins):
    """Fast pair counting routine.

    Arguments:
        ra1: RA of first sample, in degrees
        dec1: DEC of first sample, in degrees
        ra2: RA of second sample, in degrees
        dec2: DEC of second sample, in degrees
        theta_bins: np.array of theta bins

    Returns:
        pairs: Pair counts
        r1: Left side bin edges
        r2: Right side bin edges
    """
    depth = 10
    h = esutil.htm.HTM(depth)
    ntheta = len(theta_bins)
    r1, r2, pairs = h.bincount(
        min(theta_bins), max(theta_bins), ntheta, ra1, dec1,
        ra2, dec2)
    print 'Pair results: ', pairs
    return pairs, r1, r2


def define_random(spec, photo, nrand):
    """Generates a random catalog in the same range as an input catalog.

    Args: 
        spec, photo: np.recarrays
        nrand: integer that is the desired number of random points

    Returns:
        rand (ndarray): random catalog with RA, DEC
    """
    ra_min = np.min(np.array(np.min(spec['RA']), np.min(photo['RA'])))
    ra_max = np.max(np.array(np.max(spec['RA']), np.max(photo['RA'])))
    dec_min = np.min(np.array(np.min(spec['DEC']), np.min(photo['DEC'])))
    dec_max = np.max(np.array(np.max(spec['DEC']), np.max(photo['DEC'])))

    print '[+] Making a random catalog'
    rarand, decrand = coords.randsphere(
        nrand, ra_range=[ra_min, ra_max],
        dec_range=[dec_min, dec_max], system='eq')

    rand = np.recarray((nrand,), dtype=[('RA', float), ('DEC', float)])
    rand['RA'] = rarand
    rand['DEC'] = decrand
    return rand


def landy_szalay(
        dd_pairs, dr_pairs, rd_pairs, rr_pairs, rarand, gals,
        galp, r1, r2, log_theta_bins):
    """Computes Landy & Szalay (1993) estimator

    Arguments:
        dd_pairs: Data-Data pair counts
        dr_pairs: Data-Random pair counts
        rd_pairs: Random-Data pair counts
        rr_pairs: Random-Random pair counts
        rarand: RA coordinate for the random catalog
        gals: np.array
        galp: np.array
        r1: Left bin edge
        r2: Right bin edge
        log_theta_bins: Logarithmic angular bins 

    Output:
        centered_bins: Bin centers for the angular bins
        w_ls: Two point angular correlation function
    """

    print '[+] Pair counting done, computing Landy-Szalay estimator'
    normalized_dd, normalized_dr, normalized_rd, normalized_rr = [], [], [], []
    w_ls = []
    for xx in range(len(log_theta_bins)):
        if len(gals) != 0 and len(galp) != 0:
            normalized_dd.append(float(dd_pairs[xx]) / (len(galp) *
                              len(gals)))
        else:
            normalized_dd.append(0.)
        if len(galp) != 0 and len(rarand) != 0:
            normalized_dr.append(float(dr_pairs[xx]) / (len(galp) *
                              len(rarand)))
        else:
            normalized_dr.append(0.)
        if len(gals) != 0 and len(rarand) != 0:
            normalized_rd.append(float(rd_pairs[xx]) / (len(gals) *
                              len(rarand)))
        else:
            normalized_rd.append(0.)
        normalized_rr.append(float(rr_pairs[xx]) / (len(rarand) *
                              len(rarand)))
        w_ls.append((normalized_dd[xx] - normalized_dr[xx] -
            normalized_rd[xx] + normalized_rr[xx]) / normalized_rr[xx])
    centered_bins = 0.5 * (r1[:] + r2[:])
    return centered_bins, w_ls

