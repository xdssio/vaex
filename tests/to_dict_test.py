import vaex


def test_to_dict():
    df = vaex.from_csv('https://s3-eu-west-1.amazonaws.com/xdss-public-datasets/demos/titanic.csv')
    df['Embarked'] = df.Embarked.fillna("NA")
    df['Age'] = df.Age.fillna(df.Age.mean())
    df['Sex'] = df.Sex.fillna(0)
    assert len(df[:1].to_dict()) == len(df.get_column_names())
