from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

sys.path.append("/opt/airflow")
import app.scrape as scrape

def error_handle(context):
    slack_webhook_operator_text = SlackWebhookOperator(
        task_id="slack_webhook_send_text",
        slack_webhook_conn_id="slack_error_webhook",
        message=f"Error: {str(context["exception"])}",
    )
    return slack_webhook_operator_text.execute(context)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'scrape_dag',
    catchup=False,
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily"
) as dag:
    
    task = PythonOperator(
    task_id="run_scraper",
    python_callable=scrape.run_scraping,
    on_failure_callback=error_handle,
    dag=dag,
)
    
    dbt_task = DockerOperator(
    task_id="dbt_run",
    image="ghcr.io/dbt-labs/dbt-postgres",
    working_dir="/usr/app",
    mounts=[
        Mount(source="/Users/vanshkhetarpal/Code/Repos/frag-track-in/dbt/fragtracker",
               target="/usr/app",
               type="bind"),
        Mount(source="/Users/vanshkhetarpal/Code/Repos/frag-track-in/dbt/fragtracker/profiles.yml",
               target="/root/.dbt/profiles.yml",
               type="bind"),
    ],
    network_mode="frag-track-in_my_network",
    docker_url="unix://var/run/docker.sock",
    command="run",
    auto_remove="success"
)
    
    task >> dbt_task





