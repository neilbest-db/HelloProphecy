from scott_demo2_team_helloprophecyscala_airflowendtoendjob.utils import *

@task_wrapper(task_id = "silver_customers_orders")
def silver_customers_orders(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "silver_customers_orders",
        json = {"task_key" : "silver_customers_orders"},
        databricks_conn_id = "",
    )
