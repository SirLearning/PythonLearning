# TE annotation analysis
import numpy as np
import os

def checkSeqLength(fileName, length):
    with open(fileName) as seq:
        for line in seq:
            if len(line) <= length:
                print(title + line)
            title = line

fileName = os.path.join(os.getcwd(), 'teSeq.fasta')
checkSeqLength(fileName, 3)