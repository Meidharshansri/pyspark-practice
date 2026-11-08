import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

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
df.show()
df.printSchema()
print("Row count:", df.count())