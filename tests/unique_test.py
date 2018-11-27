from common import *

def test_unique():
    
    ds = vaex.from_arrays(colors=['red', 'green', 'blue', 'green'])
    with small_buffer(ds, 2):
        assert set(ds.unique(ds.colors).astype('U').tolist()) == {'red', 'green', 'blue'}
        values, index = ds.unique(ds.colors, return_inverse=True)
        assert values[index].tolist() == ds.colors.values.tolist()

    ds = vaex.from_arrays(x=['a', 'b', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'a'])
    with small_buffer(ds, 2):
        assert set(ds.unique(ds.x).astype('U').tolist()) == {'a', 'b'}
        values, index = ds.unique(ds.x, return_inverse=True)
        assert values[index].tolist() == ds.x.values.tolist()
