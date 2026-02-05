#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
# time: 2026/02/02
# name: Haowen Cui

import pandas as pd

df = pd.read_csv(r'C:\Users\17736\class_5243_project01\U.S._Chronic_Disease_Indicators.csv')
print(df.head())
print(df[df.columns].isnull().sum())
print(df.shape)