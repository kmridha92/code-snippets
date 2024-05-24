# Import data from Azure Storage with Databricks notebook

# Databricks notebook source

# COMMAND ----------

#list secret scope configured in databricks

dbutils.secrets.listScopes()

# COMMAND ----------

# Mount ADLS Gen2

configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope = "<secret scope name>", key = "<key vault secret name>"),
  "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope = "<secret scope name>", key = "<key vault secret name>"),
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<tenant id>/oauth2/token",
  "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

dbutils.fs.mount(
  source="abfss://<container name>@<adls name>.dfs.core.windows.net/",
  mount_point="/mnt/<adls name>_<container name>",
  extra_configs=configs
)

# COMMAND ----------

# Mount Blob Storage Account
# blob storage should have soft delete disabled

configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope = "<secret scope name>", key = "<key vault secret name>"),
  "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope = "<secret scope name>", key = "<key vault secret name>"),
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<tenant id>/oauth2/token",
  "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

dbutils.fs.mount(
  source="abfss://<container name>@<blob storage name>.dfs.core.windows.net/",
  mount_point="/mnt/<blob storage name>_<container name>",
  extra_configs=configs
)


# COMMAND ----------

# List - ADLS

dbutils.fs.ls("/mnt/<adls name>_<container name>")

# COMMAND ----------

# List - Blob

dbutils.fs.ls("/mnt/<blob storage name>_<container name>")

# COMMAND ----------

# Unmount

dbutils.fs.unmount("/mnt/<adls name>_<container name>")
dbutils.fs.unmount("/mnt/<blob storage name>_<container name>")