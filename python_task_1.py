import pandas as pd
import numpy as np


def generate_car_matrix(dfQ1) -> pd.DataFrame:
    dfQ1 = pd.read_csv("MapUp-Data-Assessment-F/datasets/dataset-1.csv")
    dfQ1.pivot(index="id_1", columns="id_2", values="car")
    np.fill_diagonal(df, 0)
    dfQ1
    return dfQ1


def get_type_count(df) -> dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """

    df = pd.read_csv("MapUp-Data-Assessment-F/datasets/dataset-1.csv")

    def type_count(star):
        if star.car <= 15:
            return "low"
        elif (star.car >= 15) & (star.car <= 25):
            return "medium"
        else:
            return "high"


type_count = df.apply(type_count, axis=1)
df = df.assign(car_type=type_count)
df
dict = df.to_dict()
dict
return dict()


def get_bus_indexes(df) -> list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    df = pd.read_csv("MapUp-Data-Assessment-F/datasets/dataset-1.csv")
    df['bus'].mean()
    df_1 = df[['bus']][df['bus'] > 2 * (df['bus'].mean())]
    sorted_df = df_1.sort_values(by='bus')
    list = sorted_df.tolist()
    list
    return list()


def filter_routes(df) -> list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    df = pd.read_csv("MapUp-Data-Assessment-F/datasets/dataset-1.csv")
    df_1 = df[df.truck > 7]
    sorted_df = df_1.sort_values(by='route')
    list = sorted_df.tolist()
    return list()


def multiply_matrix(matrix) -> pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """

    # Write your logic here
    def multi(multiple):
        if dfQ1[dfQ1.801 >= 20].min():
            return multiple.mul(0.75)
        else
            return multiple.mul(1.25)

    multi = dfQ1.apply(multiple, axis=1)
    dfQ1 = dfQ1.assign(matrix=hottnes)

    return matrix


def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df = pd.read_csv("MapUp-Data-Assessment-F/datasets/dataset-2.csv")

    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])

    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    df['duration'] = df['end_timestamp'] - df['start_timestamp']

    grouped = df.groupby(['id', 'id_2']).apply(lambda x: (
            x['duration'].sum() >= pd.Timedelta(days=7) and
            (x['start_timestamp'].min().time() == pd.Timestamp.min.time()) and
            (x['end_timestamp'].max().time() == pd.Timestamp.max.time())
    ))

    return pd.Timestamp.max.time()
