# PySpark Practice

Hands-on exercises to learn Apache Spark with PySpark, using local mode on my laptop.

## What I'm learning

- Spark high-level architecture (Driver, Cluster Manager, Executors)
- SparkSession and SparkContext
- DataFrames: select, filter, groupBy, joins, window functions
- Spark SQL, UDFs, RDD basics, partitions

## Requirements

- Python 3.12
- Java 17
- PySpark 4.3.0

## Setup

    pip install -r requirements.txt

## How to run

    python src/ex01_session.py

## Project structure

    Pyspark_project/
    ├── src/        # one file per exercise
    ├── data/       # input files
    ├── requirements.txt
    └── README.md

## Notes

Spark runs in local mode (`local[*]`): the driver and executor threads share one JVM on my laptop.