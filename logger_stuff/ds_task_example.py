'''
===================================================
data science script範本，使用logger來進行紀錄
===================================================
EXPLANATION:
	data science script範本，使用logger來進行紀錄，
    會同時stream到console上以及debug.log中
    並且將training config放在變數cfg取用
INPUTS:

OPTIONAL INPUT:

OUTPUT:

EXAMPLE:

REVISION HISTORY:
'''
import logging
import pandas as pd
import time
import load_configs
from load_configs import cfg


logger = logging.getLogger(__file__)

for _ in range(10):
    try:
        time.sleep(1)
        logger.debug(f"Loading data from {cfg.base.path.data}")
        df = pd.read_csv(cfg.base.path.data)
    except Exception as e:
        logger.error(e)
    finally:
        1 == 1
