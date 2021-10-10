import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/")

import risktools as rt
import geopandas


def test_get_gis():

    gf = rt.data.get_gis(
        "https://www.eia.gov/maps/map_data/Petroleum_Refineries_US_EIA.zip"
    )

    assert isinstance(
        gf, geopandas.GeoDataFrame
    ), "get_gis failed to return geopandas dataframe"

