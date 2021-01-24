#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:41:21 2021

@author: don
"""

import glassdoor_scraper as gs
import pandas as pd
path =  '/usr/local/bin/chromedriver'

df = gs.get_jobs('data scientist', 15, True, path, 15)