"""

"""

from modules.dataframes import textiles

warps = textiles['warp_nominal']
wefts = textiles['weft_nominal']
min_warp = min(warps)
max_warp = max(warps)
min_weft = min(wefts)
max_weft = max(wefts)
range_warp = round(max_warp - min_warp, 3)
range_weft = round(max_weft - min_weft, 3)
mean_warp = round(warps.mean(), 3)
mean_weft = round(wefts.mean(), 3)
mode_warp = warps.mode()[0]
mode_weft = wefts.mode()[0]
median_warp = warps.median()
median_weft = wefts.median()

warps_unique = warps.unique()
print(len(warps_unique))

wefts_unique = wefts.unique()
print(len(wefts_unique))
