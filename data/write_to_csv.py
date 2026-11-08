import csv
import os
import shutil
from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .appName("ParquetToCSV")
         .master("local[*]")
         .getOrCreate())

df = spark.read.parquet("E:/centillion/day2/userdata1.parquet")

output_path = "C:/Users/meidh/Pyspark_project/data/parquet_to_csv.csv"


if os.path.isdir(output_path):
    shutil.rmtree(output_path)

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(df.columns)
    for row in df.toLocalIterator():
        writer.writerow(row)

print("Done")
spark.stop()