import argparse

import yaml
import sys
sys.path.append('../src/')

from loguru import logger
from pyspark.sql import SparkSession

from fifa_players.config import ProjectConfig
from fifa_players.data_processor import DataProcessor
from marvelous.logging import setup_logging
from marvelous.timer import Timer

config_path = f"../project_config.yml"

config = ProjectConfig.from_yaml(config_path=config_path, env="dev")

print(f"/Volumes/{config.catalog_name}/{config.schema_name}/logs/marvelous-1.log")
setup_logging(log_file=f"/Volumes/{config.catalog_name}/{config.schema_name}/logs/marvelous-1.log")

logger.info("Configuration loaded:")
logger.info(yaml.dump(config, default_flow_style=False))

# Load the fifa players dataset
spark = SparkSession.builder.getOrCreate()

df = spark.read.csv(
    f"/Volumes/{config.catalog_name}/{config.schema_name}/data/fifa_players.csv", header=True, inferSchema=True
).toPandas()

# Preprocess the data
with Timer() as preprocess_timer:
    data_processor = DataProcessor(df, config, spark)
    data_processor.preprocess()

logger.info(f"Data preprocessing: {preprocess_timer}")

# Split the data
X_train, X_test = data_processor.split_data()
logger.info("Training set shape: %s", X_train.shape)
logger.info("Test set shape: %s", X_test.shape)

# Save to catalog
logger.info("Saving data to catalog")
data_processor.save_to_catalog(X_train, X_test)