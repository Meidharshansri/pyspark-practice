from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("pyspark-basics")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

print("Session info")
print("Spark version :", spark.version)
print("Master      :", spark.sparkContext.master)
print("App name    :", spark.sparkContext.appName)
print("Default cores :", spark.sparkContext.defaultParallelism)