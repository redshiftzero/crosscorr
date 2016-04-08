import fitsio
import pdb



def load_fits(fits, cols):
    """
    Load fits file using fitsio

    Args: 
         fits (str): input filename
         cols: list of strings to read in
    Returns:
         numpy ndarray 
    """

    return fitsio.read(fits, columns=cols) 


def read_all_data(config):
    default_columns = ['RA', 'DEC', 'Z', 'MAG_I']
    photometric_cat = fitsio.read(config['data_p'], 
                                  cols=default_columns)
    spectroscopic_cat = fitsio.read(config['data_s'],
                                    cols=default_columns)

    return photometric_cat, spectroscopic_cat


def subsample(catalog, num):
    if num != -1 and len(catalog) > num:
        index = random.randint(0, len(catalog) - 1, 2 * num)
        index = list(set(index))  # Remove duplicates
        random.shuffle(index)
        indices = index[0:num]
        catalog = catalog[indices]
    return catalog

