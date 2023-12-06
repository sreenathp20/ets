#!/usr/bin/env python
# coding: utf-8

# In[8]:


# downloading the required athena driver
get_ipython().system('pip install PyAthena[SQLAlchemy]')


# In[9]:


get_ipython().system('aws configure get region')


# In[19]:


from sqlalchemy import create_engine
import pandas as pd

# This s3 path will be used by athena. 
s3_staging_dir = "s3://ets-aws-plalab-dii-prod-analyticsbucket-1ktrlhzbrcbkb/athena_query_results/"

# Connecting to athena
connection_string = f"awsathena+rest://:@athena.us-east-1.amazonaws.com:443/labsprodeventsdatabase-x806vjuzpbrd?s3_staging_dir={s3_staging_dir}"

engine = create_engine(connection_string)


# In[24]:


# get complete history of test ready events. This includes data across all environments. 
query1 = "SELECT * FROM processed_events where application_id='aecbd362-7e1f-48e8-af2d-f8b989c3615f'"
test_ready_full_df = pd.read_sql(query1, engine)
test_ready_full_df


# In[25]:


# Please use below s3 paths based on the type of output files. 
# s3://ets-aws-plalab-dii-prod-analyticsbucket-1ktrlhzbrcbkb/sagemaker/test_ready/

# to store any adhoc files required by transformations, can be placed in this s3 path.
s3_adhoc_files = "s3://ets-aws-plalab-dii-prod-analyticsbucket-1ktrlhzbrcbkb/sagemaker/test_ready/adhoc_files/"

# to store the intermediate outputs while running the transformations. 
s3_intermediate_files = "s3://ets-aws-plalab-dii-prod-analyticsbucket-1ktrlhzbrcbkb/sagemaker/test_ready/intermediate_files/"

# to store the final version of the files required by tableau dashboards.
s3_final_tableau_data_files = "s3://ets-aws-plalab-dii-prod-analyticsbucket-1ktrlhzbrcbkb/sagemaker/test_ready/final_tableau_data_files/"


# In[ ]:




