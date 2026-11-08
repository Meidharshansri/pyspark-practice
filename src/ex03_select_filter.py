import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ex02").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employees = [
    (1, "Arun",  "IT",      60000, 28),
    (2, "Priya", "HR",      45000, 32),
    (3, "Karan", "IT",      75000, 35),
    (4, "Divya", "Finance", 52000, 30),
    (5, "Ravi",  "Finance", None,  41),
    (6, "Meena", "HR",      48000, 26),
]
df = spark.createDataFrame(employees, ["id", "name", "dept", "salary", "age"])
df.select("name", "salary").show()
df.filter(F.col("salary") > 50000).show()
df.withColumn(  "bonus", F.col("salary") * 0.10).show()