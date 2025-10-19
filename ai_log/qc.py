
import pandas as pd
import numpy as np

def qc_basic(df, meta):
    """QC بسيط: نتحقق من القيم الغير مقبولة، ن校正 درجة الحرارة، ن校正 الكثافة."""
    # 1- نتحقق من القيم الغير مقبولة
    df = df.replace([np.inf, -np.inf], np.nan)  # نستبدل القيم الغير مقبولة
    df = df.fillna(method='bfill').fillna(method='ffill')  # ن补充 القيم الNaN

    # 2- ن校正 درجة الحرارة (مثال: GR)
    # (نحتاج إلى meta['BHT'] لهذه الخطوة)
    if 'BHT' in meta:
        df['GR'] = df['GR'] * (1 + 0.0002 * (meta['BHT'] - 150))  # ن校正 درجة الحرارة

    # 3- ن校正 الكثافة (RHOB)
    # (نحتاج إلى meta['MUDWEIGHT'] لهذه الخطوة)
    if 'MUDWEIGHT' in meta and 'RHOB' in df.columns:
        df['RHOB'] = df['RHOB'] * (1 + 0.4 * (meta['MUDWEIGHT'] - 1))

    return df
