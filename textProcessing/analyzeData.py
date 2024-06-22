def summarize_data(df):
    return df.describe()

def count_unique_values(df, column_name):
    return df[column_name].value_counts()

def filter_data(df, column_name, value):
    return df[df[column_name] == value]

def group_data(df, column_name):
    return df.groupby(column_name).mean()
