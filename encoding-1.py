# -*- coding: UTF-8 -*-
#!/anaconda3/bin/python


# -----------------------------------------------------------------------------------------------------------------------
# |                                                 Import                                                              |
# -----------------------------------------------------------------------------------------------------------------------

from Encoder import Encoder
import pandas as pd
import numpy as np
import math
import exrex

# -----------------------------------------------------------------------------------------------------------------------
# |                                                 Reading preprocessed dataset                                        |
# -----------------------------------------------------------------------------------------------------------------------


bf_df = pd.read_csv('./BlackFriday_preprocessed.csv')
bf_df.head()