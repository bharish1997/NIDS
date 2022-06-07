from scapy.all import * 
import os
from time import sleep
import json
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

print("Created Producer\n")

while(True):
    os.system('sudo tcpdump -w /home/harry/Desktop/NIDS/sniff.pcap -i wlp2s0 -c 10 ip')
    os.system('tshark -r /home/harry/Desktop/NIDS/sniff.pcap -T json > /home/harry/Desktop/NIDS/pcap.json')
    # a = rdpcap("sniff.pcap")
    f = open('pcap.json')
    data = json.load(f)
  
    for i in data:
        print(i)
        producer.send('pkttest_pcap', i)
        sleep(2)


    f.close()
    sleep(2)