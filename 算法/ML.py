#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import os
import pandas as pd
def util():
    dir1 = '../input'
    train_dir = os.path.join(dir1,'train_images/')
    base_path = os.path.join(dir1,'train.csv')
    df = pd.read_csv(base_path)
    df['path'] = df['id_code'].map(lambda x:os.path.join(train_dir,'{}.png'.format(x)))
    df = df.drop(columns=['id_code'])


if __name__ == '__main__':
    a = []
    b = []
    for i in range(10):
        a.append(i)
        print '{}.jpg'.format(i)
    a = map(lambda x:'{}.jpg'.format(x),a)
    print a