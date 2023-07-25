# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:08:00 2023

@author: Sergey Zhuravlev
"""

import os
import pandas as pd
import numpy as np
from phoenixScrapp import pScrapp


# setting an initial folder
prb = pScrapp('./testData')
# setting an indicator of valuable file
prb.findFiles('Change model')
# data scrapping
prb.scrapp('Model', 'class="model-name l-delta-text">', '<')
prb.scrapp('Price', 'class="real-price t-gamma-text l-quote-text">\n', '\n')
