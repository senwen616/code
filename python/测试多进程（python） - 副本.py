#!/usr/bin/python
# -* - coding: UTF-8 -* -

import multiprocessing

def run(num):

    print 'process %d start'%num
if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=5)
    for i in range(1,6):
        pool.apply_async(func=run,args=(i,))
    pool.close()
    pool.join()


