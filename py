import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Extracting data
Extractingdata_node1723343702984 = glueContext.create_dynamic_frame.from_catalog(database="ghg methane db", table_name="raw_data", transformation_ctx="Extractingdata_node1723343702984")

# Script generated for node Change Schema
ChangeSchema_node1723343714761 = ApplyMapping.apply(frame=Extractingdata_node1723343702984, mappings=[("entity", "string", "entity", "string"), ("year", "long", "year", "long"), ("ghg", "double", "ghg", "double"), ("methane", "double", "methane", "double")], transformation_ctx="ChangeSchema_node1723343714761")

# Script generated for node Load Processed data
LoadProcesseddata_node1723343731694 = glueContext.getSink(path="s3://ghg-methane/processed_data/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="LoadProcesseddata_node1723343731694")
LoadProcesseddata_node1723343731694.setCatalogInfo(catalogDatabase="ghg methane db",catalogTableName="ghg glue table")
LoadProcesseddata_node1723343731694.setFormat("csv")
LoadProcesseddata_node1723343731694.writeFrame(ChangeSchema_node1723343714761)
job.commit()