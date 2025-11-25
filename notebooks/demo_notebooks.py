# Demo notebook for quickstart
dbutils.widgets.text("input", "world", "demo input")
input_val = dbutils.widgets.get("input")
print(f"Hello from Databricks Asset Bundles! input={input_val}")
