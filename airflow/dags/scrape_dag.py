from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
sys.path.append("/opt/airflow")
import app.scrape as scrape

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'scrape_dag',
    catchup=False,
    default_args=default_args,
    start_date=datetime(2026, 7, 12),
    schedule="@daily"
)

def error_handle(context):
    slack_webhook_operator_text = SlackWebhookOperator(
        task_id="slack_webhook_send_text",
        slack_webhook_conn_id="slack_error_webhook",
        message=f"Error: {str(context["exception"])}",
    )
    return slack_webhook_operator_text.execute(context)

task = PythonOperator(
    task_id="run_scraper",
    python_callable=scrape.run_scraping,
    on_failure_callback=error_handle,
    dag=dag,
)
