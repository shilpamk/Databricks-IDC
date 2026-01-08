# Databricks notebook source
events = spark.read.csv('/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv', header='true', inferSchema=True)
# Verify it's working
print(f"✅ Ready to go! Loaded {events.count():,} events")
events.show(5)
