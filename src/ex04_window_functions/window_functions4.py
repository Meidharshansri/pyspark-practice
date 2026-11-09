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
sales = spark.createDataFrame([("Jan", 1000), ("Feb", 1200), ("Mar", 900), ("Apr", 1500),], ["month", "revenue"])

sales = sales.withColumn("m_no", F.expr("CASE month WHEN 'Jan' THEN 1 WHEN 'Feb' THEN 2 WHEN 'Mar' THEN 3 ELSE 4 END"))
w = Window.orderBy("m_no")
(sales.withColumn("prev_month", F.lag("revenue", 1).over(w))
    .withColumn("next_month", F.lead("revenue", 1).over(w))
    .withColumn("change", F.col("revenue") - F.col("prev_month")).show())