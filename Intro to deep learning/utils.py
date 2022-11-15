import requests
import os, hashlib, gzip, struct
import numpy as np

def createMNIST(url):

    fp = os.path.join(os.path.sep, 'tmp', hashlib.md5(url.encode('utf-8')).hexdigest())

    if not os.path.isfile(fp):
            with open(fp, 'wb') as f:
                dat = requests.get(url)
                f.write(gzip.decompress(dat.content))

    with open(fp, 'rb') as f:

            magic, size = struct.unpack('>II', f.read(8))

            #images
            if magic == 2051:

                    nrows, ncols = struct.unpack('>II', f.read(8))
                    set = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
                    set = set.reshape(size, nrows, ncols)
            #labels
            else:
                set = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
                set = set.reshape(size, 1)

    return set