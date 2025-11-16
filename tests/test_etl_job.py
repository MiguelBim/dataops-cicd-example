import pandas as pd
from pipeline.etl_job import transform

def test_transform_adds_total_when_columns_present():
    df = pd.DataFrame({"quantity":[2,3], "price":[10.0, 5.0]})
    out = transform(df)
    assert "total" in out.columns
    assert list(out["total"]) == [20.0, 15.0]

def test_transform_drops_nulls():
    df = pd.DataFrame({"quantity":[1, None], "price":[2.0, 3.0]})
    out = transform(df)
    assert len(out) == 1
