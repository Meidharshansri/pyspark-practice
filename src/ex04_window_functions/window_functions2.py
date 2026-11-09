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
    ("Arun","Sales", 50000),
    ("Bala","Sales", 60000),
    ("Chitra","Sales", 60000),
    ("Divya","IT",80000),
    ("Elan", "IT",70000),
    ("Farah","IT",90000),
    ("Gopal","HR", 45000),
    ("Hema","HR", 55000),
]
emp = spark.createDataFrame(data, ["name", "dept", "salary"])
w = Window.partitionBy("dept").orderBy(F.col("salary").desc())

(emp.filter(F.col("dept") == "Sales")
    .withColumn("row_number", F.row_number().over(w))
    .withColumn("rank",       F.rank().over(w))
    .withColumn("dense_rank", F.dense_rank().over(w))
    .show())