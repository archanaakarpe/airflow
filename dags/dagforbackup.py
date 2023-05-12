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
dag = DAG(dag_id='Mongodb_backup',
          default_args=default_args,
          schedule_interval='0,10,20,30,40,50 * * * *',
          dagrun_timeout=timedelta(seconds=120))

# Step 1 - Copy shell script to server
t1_bash= """ 
scp -o StrictHostKeyChecking=No -i /opt/airflow/dags/ssh_keys/3-mar-2023-N.Virginia.pem /opt/airflow/dags/dbbackup.sh ubuntu@107.23.137.161:/home/ubuntu
"""
task1 = BashOperator(
    #ssh_conn_id='ssh_conn',
    task_id='scp_to_server',
    bash_command=t1_bash,
    dag=dag
)

# Step 2 - run shell script on server
t2_bash = """
echo 'Running shell script'
whoami
sh -x /home/ubuntu/dbbackup.sh
""" 

t1 = SSHOperator(
    ssh_conn_id='ssh_conn',
    task_id='run_script',
    command=t2_bash,
    dag=dag
)

task1 >> t1