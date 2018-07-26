## creates preprocessed data and variables in workspace

# Dataframe
textile_data <- read.csv('rawdata/total.csv', dec = ',')

# Variables

## Densities
dens_warp <- textile_data$warp_dens
dens_weft <- textile_data$weft_dens
densities <- cbind(dens_warp, dens_weft)
