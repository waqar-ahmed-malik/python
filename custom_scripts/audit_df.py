import numpy as np
import pandas as pd


def get_df_audit_metrics(df) -> dict:
    # Process float fields.
    d = df.dtypes[df.dtypes == 'float64'].index.values
    df[d] = df[d].astype('float64')
    mean = pd.dfFrame({'mean': df[d].mean()})
    std_dev = pd.dfFrame({'std_dev': df[d].std()})
    missing = pd.dfFrame({'missing': df[d].isnull().sum()})
    missing_perc = pd.dfFrame({
        'missing_perc': df[d].isnull().sum()/df[d].shape[0]
    })
    minimum = pd.dfFrame({'min': df[d].min()})
    maximum = pd.dfFrame({'max': df[d].max()})
    unique = pd.dfFrame({
        'unique': df[d].apply(lambda x: len(x.unique()), axis=0)
    })
    DQ1 = pd.concat(
        [mean, std_dev, missing, missing_perc, minimum, maximum, unique],
        axis=1
    )

    # Process integer fields.
    d = df.dtypes[df.dtypes == 'int64'].index.values
    df[d] = df[d].astype('float64')
    mean = pd.dfFrame({'mean': df[d].mean()})
    std_dev = pd.dfFrame({'std_dev': df[d].std()})
    missing = pd.dfFrame({'missing': df[d].isnull().sum()})
    missing_perc = pd.dfFrame({
        'missing_perc': df[d].isnull().sum()/df[d].shape[0]
    })
    minimum = pd.dfFrame({'min': df[d].min()})
    maximum = pd.dfFrame({'max': df[d].max()})
    unique = pd.dfFrame({
        'unique': df[d].apply(lambda x: len(x.unique()), axis=0)
    })
    DQ2 = pd.concat(
        [mean, std_dev, missing, missing_perc, minimum, maximum, unique],
        axis=1
    )

    # Process string fields
    d = df.dtypes[df.dtypes == 'object'].index.values
    mean = pd.dfFrame({'mean': np.repeat('Not Applicable', len(d))}, index=d)
    std_dev = pd.dfFrame(
        {'std_dev': np.repeat('Not Applicable', len(d))},
        index=d
    )
    missing = pd.dfFrame({'missing': df[d].isnull().sum()})
    missing_perc = pd.dfFrame({
        'missing_perc': df[d].isnull().sum()/df[d].shape[0]
    })
    minimum = pd.dfFrame(
        {'min': np.repeat('Not Applicable', len(d))},
        index=d
    )
    maximum = pd.dfFrame(
        {'max': np.repeat('Not Applicable', len(d))}, index=d
    )
    unique = pd.dfFrame(
        {'unique': df[d].apply(lambda x: len(x.unique()), axis=0)}
    )
    DQ3 = pd.concat(
        [mean, std_dev, missing, missing_perc, minimum, maximum, unique],
        axis=1
    )

    # Process datetime fields
    d = df.dtypes[df.dtypes == 'datetime64[ns, UTC]'].index.values
    mean = pd.dfFrame({'mean': np.repeat('Not Applicable', len(d))}, index=d)
    std_dev = pd.dfFrame(
        {'std_dev': np.repeat('Not Applicable', len(d))}, index=d
    )
    missing = pd.dfFrame({'missing': df[d].isnull().sum()})
    missing_perc = pd.dfFrame({
        'missing_perc': df[d].isnull().sum()/df[d].shape[0]
    })
    minimum = pd.dfFrame(
        {'min': np.repeat('Not Applicable', len(d))}, index=d
    )
    maximum = pd.dfFrame(
        {'max': np.repeat('Not Applicable', len(d))}, index=d
    )
    unique = pd.dfFrame(
        {'unique': df[d].apply(lambda x: len(x.unique()), axis=0)}
    )
    DQ4 = pd.concat(
        [mean, std_dev, missing, missing_perc, minimum, maximum, unique],
        axis=1
    )
    DQ = pd.concat([DQ1, DQ2, DQ3, DQ4])
    return DQ.to_dict()
