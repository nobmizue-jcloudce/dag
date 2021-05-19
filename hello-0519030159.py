from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello-0519030159",
}

dag = DAG(
    "hello-0519030159",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d34fda99_7a52_40d2_ae8f_9775d8d58a8d = NotebookOp(
    name="hello",
    namespace="default",
    task_id="hello",
    notebook="hello.ipynb",
    cos_endpoint="https://storage.googleapis.com/storage/v1",
    cos_bucket="jcloudce-healthcare-pipelines",
    cos_directory="hello-0519030159",
    cos_dependencies_archive="hello-d34fda99-7a52-40d2-ae8f-9775d8d58a8d.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="continuumio/anaconda3:2020.07",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "GOOG1EQANEHW3FTKFP2HUEXULPI3RO7HHIYW6LJZ2UPKOP2D5LJFNMRP7EXSQ",
        "AWS_SECRET_ACCESS_KEY": "fgIFmjIQjteZr1TOw0Wn1WEUGI7mjTGpaGuAjqjf",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)
