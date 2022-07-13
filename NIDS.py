import io
import json
from unittest import result

from keras.models import load_model
import pandas as pd
import pickle
import csv
from requests import head

from project import encode_data


with open('encoding.json') as f:
    encodings = json.load(f)
    encodings[1] = encodings['1']
    encodings[2] = encodings['2']
    encodings[3] = encodings['3']
    encodings[4] = encodings['4']


model = pickle.load(open("DT_model.pkl","rb"))

def test_packet(pkt):
    data = pkt.encode('utf8')
    data = pd.read_csv(io.BytesIO(data), header=None)
    # print("CSV ", data)
    encode_data(data, cols=(1, 2, 3), encodings=encodings)
    # print("Successful encoded data ", data)
    prediction = model.predict(data)
    # print("Prediction: ", prediction)
    return prediction


import sys
count=0
pkts=sys.argv[1]
with open(pkts) as f:
    for row in f:
        result=test_packet(str(row))
        print(row)    
        print(count," ",result)
        count+=1



















# t="0,tcp,private,RSTR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,1.00,1.00,1.00,0.00,0.00,237,1,0.00,0.31,0.29,0.00,0.00,0.00,0.30,1.00"

# normal.
# 0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,9,9,1.00,0.00,0.11,0.00,0.00,0.00,0.00,0.00

# smurf.
# 0,icmp,ecr_i,SF,1032,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,107,107,0.00,0.00,0.00,0.00,1.00,0.00,0.00,255,107,0.42,0.02,0.42,0.00,0.00,0.00,0.00,0.00