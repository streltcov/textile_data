"""

"""

import pandas
from textiles.dataframes import textiles

########################################################################################################################

# warps and wefts values Series objects;
warps = textiles['warp_nominal']
wefts = textiles['weft_nominal']

########################################################################################################################

# minimal and maximal values;
warp_min = min(warps)
warp_max = max(warps)
weft_min = min(wefts)
weft_max = max(wefts)

########################################################################################################################

# range for warps and wefts;
warp_range = round(warp_max - warp_min, 3)
weft_range = round(weft_max - weft_min, 3)

# mean values for warps and wefts;
warp_mean = round(warps.mean(), 3)
weft_mean = round(wefts.mean(), 3)

# mode values for warps and wefts;
warp_mode = warps.mode()[0]
weft_mode = wefts.mode()[0]

# medina values for warps and wefts;
warp_median = warps.median()
weft_median = wefts.median()

########################################################################################################################

# unique values for warps and wefts;
warps_unique = warps.unique()
wefts_unique = wefts.unique()

# 1st and 3rd quartiles for warps;
warps_q1, warps_q3 = textiles.warp_nominal.quantile([0.25, 0.75])

# 1st and 3rd quartiles for wefts;
wefts_q1, wefts_q3 = textiles.weft_nominal.quantile([0.25, 0.75])

########################################################################################################################

# outliers borders for warps;
warps_outliers_lower_border = round(warps_q1 - 1.5 * (warps_q3 - warps_q1), 3)
warps_outliers_upper_border = round(warps_q1 + 1.5 * (warps_q3 - warps_q1), 3)

# outliers borders for wefts;
wefts_outliers_lower_border = round(wefts_q1 - 1.5 * (wefts_q3 - wefts_q1), 3)
wefts_outliers_upper_border = round(wefts_q1 + 1.5 * (wefts_q3 - wefts_q1), 3)

########################################################################################################################

# dataframe - outliers on warp_thicks;
warps_cleared = textiles[textiles.warp_nominal > warps_outliers_lower_border]
warps_cleared = textiles[textiles.warp_nominal < warps_outliers_upper_border]

# dataframe - outliers on weft thicks;
wefts_cleared = textiles[textiles.weft_nominal > wefts_outliers_lower_border]
wefts_cleared = textiles[textiles.weft_nominal < wefts_outliers_upper_border]

########################################################################################################################

# dataframe cleared from all outliers;
cleared = textiles[textiles.warp_nominal > warps_outliers_lower_border]
cleared = textiles[textiles.warp_nominal < warps_outliers_upper_border]
cleared = textiles[textiles.weft_nominal > wefts_outliers_lower_border]
cleared = textiles[textiles.weft_nominal < wefts_outliers_upper_border]

outliers_percent = round(((len(textiles) - len(cleared)) / len(textiles)) * 100, 3)

########################################################################################################################

outliers = pandas.concat([textiles, cleared]).drop_duplicates(keep=False)
# wefts_outliers = pandas.merge()

########################################################################################################################

cleared_warps = cleared.warp_nominal
cleared_wefts = cleared.weft_nominal

########################################################################################################################

# cleared dataframe -> warps -> central tendency;
cleared_warps_mean = round(cleared_warps.mean(), 3)
cleared_warps_median = round(cleared_warps.median(), 3)
cleared_warps_mode = round(cleared_warps.mode()[0], 3)
cleared_warps_min = round(cleared_warps.min(), 3)
cleared_warps_max = round(cleared_warps.max(), 3)
cleared_warps_range = round(cleared_warps_max - cleared_warps_min, 3)
cleared_Warps_q1, cleared_warps_q3 = cleared.warp_nominal.quantile([0.25, 0.75])

########################################################################################################################

# cleared dataframe -> wefts -> central tendency;
cleared_wefts_mean = round(cleared_wefts.mean(), 3)
cleared_wefts_median = round(cleared_wefts.median(), 3)
cleared_wefts_mode = round(cleared_wefts.mode()[0], 3)
cleared_wefts_min = round(cleared_wefts.min(), 3)
cleared_wefts_max = round(cleared_wefts.max(), 3)
cleared_wefts_range = round(cleared_wefts_max - cleared_wefts_min, 3)
cleared_wefts_q1, cleared_wefts_q3 = cleared.weft_nominal.quantile([0.25, 0.75])

########################################################################################################################
