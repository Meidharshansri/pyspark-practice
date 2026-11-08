from pyspark.sql import SparkSession
spark = (SparkSession.builder
         .appName("ReadParquet")
         .master("local[*]")
         .getOrCreate())
df= spark.read.parquet("E:/centillion/day2/userdata1.parquet")
df.show(10)
print(df.count())
spark.stop()