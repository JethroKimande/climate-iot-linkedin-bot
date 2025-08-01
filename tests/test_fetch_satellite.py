import os
import sys
import pytest

MODULE_PATH = os.path.join(os.path.dirname(__file__), "..", "scripts", "fetch_satellite_data.py")


def test_build_wms_url_basic():
    with open(MODULE_PATH, "r", encoding="utf-8") as f:
        code_lines = [line for line in f.readlines() if "sys.stdout" not in line]
    fsd_globals = {}
    exec("".join(code_lines), fsd_globals)

    build_wms_url = fsd_globals["build_wms_url"]
    LAYER = fsd_globals["LAYER"]
    REGION = fsd_globals["REGION"]

    sample_date = "2025-07-01"
    params = build_wms_url(sample_date)

    expected = {
        "SERVICE": "WMS",
        "REQUEST": "GetMap",
        "VERSION": "1.3.0",
        "LAYERS": LAYER,
        "CRS": "EPSG:4326",
        "BBOX": REGION,
        "WIDTH": "1024",
        "HEIGHT": "1024",
        "FORMAT": "image/png",
        "TIME": sample_date,
    }

    assert params == expected

