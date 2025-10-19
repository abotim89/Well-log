
import pytest
import pandas as pd
from ai_log.qc import qc_basic

def test_qc_basic():
    df = pd.DataFrame({
        'GR': [0, 100, 200, np.nan, 300],
        'RHOB': [1.8, 2.2, np.inf, 2.5, -1],
        'NPHI': [0.1, 0.2, 0.3, 0.4, 0.5]
    })
    meta = {'BHT': 180, 'MUDWEIGHT': 1.2}

    df_clean = qc_basic(df, meta)
    assert not df_clean['GR'].isnull().any(), "GR should not contain NaNs"
    assert (df_clean['RHOB'] > 0).all(), "RHOB should be positive"
    assert (df_clean['NPHI'] <= 1).all(), "NPHI should be <= 1"
