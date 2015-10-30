# zclustering-public

Utilities for generating clustering redshift distributions of a photometric sample given a spectroscopic sample. 

## Simulations

The `simulations` package enables the generation of spectroscopic and photometric samples similar to the observed data in sky coverage, redshift distributions, color and magnitude distributions. A higher-resolution simulation is required to draw galaxies from. Currently DES BCC simulations are used for this. 

## Clustering

The `zclustering` package takes two galaxy samples that overlap in redshift and on the sky and computes the redshift distribution of the unknown sample. 
