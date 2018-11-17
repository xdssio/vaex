from common import *
import pytest

# @pytest.mark.skip
@pytest.mark.parametrize("dropna", [True, False])
def test_value_counts_with_pandas(ds_local, dropna):
    ds = ds_local
    df = ds.to_pandas_df()
    assert df.x.value_counts(dropna=dropna).values.tolist() == ds.x.value_counts(dropna=dropna).values.tolist()


# @pytest.mark.parametrize("dropna", [True, False])
def test_value_counts_simple():
    x = np.array([0, 1, 1, 2, 2, 2, np.nan])
    y = np.ma.array(x, mask=[True, True, False, False, False, False, False])
    ds = vaex.from_arrays(x=x, y=y)
    df = ds.to_pandas_df()

    assert ds.x.value_counts(dropna=True, ascending=True).values.tolist() == [1, 2, 3]
    assert ds.x.value_counts(dropna=False, ascending=True).values.tolist() == [1, 1, 2, 3]

    assert ds.y.value_counts(dropna=True, ascending=True).values.tolist() == [1, 3]
    assert ds.y.value_counts(dropna=False).values.tolist() == [3, 3, 1]
    assert ds.y.value_counts(dropna=False).index.tolist() == ['2', 'missing', '1']

    assert df.x.value_counts(dropna=False).values.tolist() == ds.x.value_counts(dropna=False).values.tolist()
    assert df.x.value_counts(dropna=True).values.tolist() == ds.x.value_counts(dropna=True).values.tolist()

    # do we want the index to be the same?
    # assert df.y.value_counts(dropna=False).index.tolist() == ds.y.value_counts(dropna=False).index.tolist()
    assert df.y.value_counts(dropna=False).values.tolist() == ds.y.value_counts(dropna=False).values.tolist()
    assert df.y.value_counts(dropna=True).values.tolist() == ds.y.value_counts(dropna=True).values.tolist()
