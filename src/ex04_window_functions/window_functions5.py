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
w = Window.partitionBy("dept")
(emp
    .withColumn("dept_avg", F.round(F.avg("salary").over(w), 0))
    .withColumn("dept_max",F.max("salary").over(w))
    .withColumn("dept_total", F.sum("salary").over(w))
    .withColumn("vs_avg", F.col("salary") - F.col("dept_avg")).show())