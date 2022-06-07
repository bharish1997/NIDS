from time import sleep
from pyspark.sql import SparkSession
import json
import csv

spark = SparkSession \
        .builder \
        .appName("Message Format as JSON") \
        .master("local[*]") \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

allfiles =  spark.read.option("header","false").json("/home/harry/Desktop/NIDS/packets/part-*.json")

allfiles.coalesce(1).write.format("json").option("header", "false").save("/home/harry/Desktop/NIDS/store")
