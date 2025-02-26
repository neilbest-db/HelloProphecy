from scott_demo2_team_helloprophecyscala_airflowendtoendjob.utils import *

@task_wrapper(task_id = "gold_sales")
def gold_sales(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "gold_sales",
        json = {"task_key" : "gold_sales"},
        databricks_conn_id = "",
    )
