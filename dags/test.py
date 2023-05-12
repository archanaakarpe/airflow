from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(dag_id='testing_stuff',
          default_args=default_args,
          schedule_interval='0,10,20,30,40,50 * * * *',
          dagrun_timeout=timedelta(seconds=120))
# Step 1 - Dump data from postgres databases
t1_bash = """
ls -lthr > /tmp/dag-output
"""
t1 = SSHOperator(
    ssh_conn_id='ssh_conn',
    task_id='test_ssh_operator',
    command=t1_bash,
    dag=dag
)

task1 = BashOperator(
    task_id='run_remote_script',
    bash_command='Ex01.sh',
    dag=dag
)

t1 >> task1