# crosscorr

Utilities for generating clustering redshift distributions of a photometric sample given a spectroscopic sample. 

## Simulations

The code in `simulations` enables the generation of spectroscopic and photometric samples similar to the observed data in sky coverage, redshift distributions, color and magnitude distributions. A higher-resolution simulation is required to draw galaxies from. Currently DES BCC simulations are used for this. 

### Instructions for use

1. Download the DES BCC (not covered here) and place into `simulations/reference/` directory. 
2. Define the dataset to be used to match distributions with in a config YAML file. An example for DES Y1 data is located in `DES_y1_simgen.yaml`.  

## Clustering

The code in `crosscorr` takes two galaxy samples that overlap in redshift and on the sky and computes the redshift distribution of the unknown sample. 

### Instructions for use

1. Define the photometric and spectroscopic datasets to be used, as well as details of the binning that you would like to use in a configuration file. An example for DES Y1 data is located in `DES_y1_zclustering.yaml`

### Example with DES



### Example with another dataset