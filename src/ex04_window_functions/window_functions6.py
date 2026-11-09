import os, sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = (SparkSession
         .builder
         .appName("windows")
         .master("local[*]")
         .getOrCreate())

data = [
    ("Arun", "Sales", 50000),
    ("Bala", "Sales", 60000),
    ("Chitra", "Sales", 60000),
    ("Divya", "IT", 80000),
    ("Elan", "IT", 70000),
    ("Farah", "IT", 90000),
    ("Gopal", "HR", 45000),
    ("Hema", "HR", 55000),
]
daily = spark.createDataFrame([(1, 100), (2, 200), (3, 150), (4, 300), (5, 250),], ["day", "sales"])

running= Window.orderBy("day").rowsBetween(Window.unboundedPreceding, Window.currentRow)
moving= Window.orderBy("day").rowsBetween(-1, 0)

(daily.withColumn("running_total", F.sum("sales").over(running))
    .withColumn("moving_avg_2",  F.avg("sales").over(moving)).show())