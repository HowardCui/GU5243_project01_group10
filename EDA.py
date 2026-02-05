#!/usr/bin/env python 3.12
# -*- coding: utf-8 -*-
# time: 2026/02/04
# name: Haowen Cui, Yuhan Guo

import sys
import time
import pandas as pd
import requests

#source page: https://data.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators/hksd-2xuw/about_data
def get_dataset():
    """
    get CDC Chronic Disease Indicators data
    :return: pandas DataFrame
    """
    #SODA2 API request
    url = r'https://data.cdc.gov/resource/hksd-2xuw.json'
    try:
        all_data=[]
        offset=0
        while True:
            params={
                "$limit": 50000,
                "$offset": offset
            }
            response=requests.get(url, params=params)
            data=response.json()

            if not data:
                break

            all_data.extend(data)
            offset+= 50000
            print(f"loaded rows: {offset}")
            time.sleep(1.5)

        df = pd.DataFrame(all_data)
        return df

    except Exception as e:
        print(f'request failed: {e}')

if __name__ == "__main__":
    # check python version
    print(f'python version: {sys.version}')
    dataset = get_dataset()
    # preview
    print(dataset.head())
    print(dataset.shape)

