from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello-airflow-0519001809",
}

dag = DAG(
    "hello-airflow-0519001809",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello-airflow.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_c388e580_846f_4394_91a5_fe95d060b5da = NotebookOp(
    name="load_data",
    namespace="default",
    task_id="load_data",
    notebook="examples/pipelines/hello_world_kubeflow_pipelines/load_data.ipynb",
    cos_endpoint="https://storage.googleapis.com/storage/v1",
    cos_bucket="jcloudce-healthcare-pipelines",
    cos_directory="hello-airflow-0519001809",
    cos_dependencies_archive="load_data-c388e580-846f-4394-91a5-fe95d060b5da.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "GOOG1EQANEHW3FTKFP2HUEXULPI3RO7HHIYW6LJZ2UPKOP2D5LJFNMRP7EXSQ",
        "AWS_SECRET_ACCESS_KEY": "fgIFmjIQjteZr1TOw0Wn1WEUGI7mjTGpaGuAjqjf",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
    },
    config_file="None",
    dag=dag,
)


notebook_op_5f6565a2_1d84_4a58_a05b_3c59c6e848f8 = NotebookOp(
    name="Part_1___Data_Cleaning",
    namespace="default",
    task_id="Part_1___Data_Cleaning",
    notebook="examples/pipelines/hello_world_kubeflow_pipelines/Part 1 - Data Cleaning.ipynb",
    cos_endpoint="https://storage.googleapis.com/storage/v1",
    cos_bucket="jcloudce-healthcare-pipelines",
    cos_directory="hello-airflow-0519001809",
    cos_dependencies_archive="Part 1 - Data Cleaning-5f6565a2-1d84-4a58-a05b-3c59c6e848f8.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv"],
    pipeline_inputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "GOOG1EQANEHW3FTKFP2HUEXULPI3RO7HHIYW6LJZ2UPKOP2D5LJFNMRP7EXSQ",
        "AWS_SECRET_ACCESS_KEY": "fgIFmjIQjteZr1TOw0Wn1WEUGI7mjTGpaGuAjqjf",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_5f6565a2_1d84_4a58_a05b_3c59c6e848f8
    << notebook_op_c388e580_846f_4394_91a5_fe95d060b5da
)
