# TE annotation analysis
import os
import pandas as pd

def checkSeqLength(fileName, length):
    with open(fileName) as seq:
        for line in seq:
            if len(line) <= length:
                print(title + line)
            title = line

# fileName = os.path.join(os.getcwd(), 'teSeq.fasta')
# checkSeqLength(fileName, 3)
data = pd.read_csv("new.txt", sep = '\t')
length_counts = data.groupby("length").size().reset_pwdindex(name='count')