from pyspark import SparkContext
from pyspark.sql import SQLContext
sc = SparkContext("local", "sparkdemoapp")

sqlContext = SQLContext(sc)

table_df = sqlContext.read \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="person", keyspace="ks_dave") \
    .load()

table_df.show()