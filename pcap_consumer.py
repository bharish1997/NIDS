from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

kafka_topic_name = "pkttest_pcap"
kafka_bootstrap_servers = 'localhost:9092'

spark = SparkSession \
        .builder \
        .appName("PySpark Structured Streaming with Kafka and Message Format as JSON") \
        .master("local[*]") \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

pkt_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("subscribe", kafka_topic_name) \
        .option("startingOffsets", "latest") \
        .load()

pkt_df1 = pkt_df.selectExpr("CAST(value AS STRING)", "timestamp")

query = pkt_df1 \
        .writeStream \
        .trigger(processingTime='2 seconds') \
        .outputMode("update") \
        .format("console") \
        .start()

query = pkt_df1 \
       .writeStream \
       .trigger(processingTime='2 seconds') \
       .outputMode("append") \
       .format("json") \
       .option("checkpointLocation", "/home/harry/Desktop/NIDS/packets") \
       .option("path", "/home/harry/Desktop/NIDS/packets") \
       .start()

query.awaitTermination()


