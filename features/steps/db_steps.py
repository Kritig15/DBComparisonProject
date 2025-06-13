import logging

logging.basicConfig(
    filename='logs/db_comparison.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from behave import given, when, then
from db_utils.db_connection import connect_db

source_conn = None
target_conn = None
source_data = []
target_data = []
report_path = os.path.join(os.path.dirname(__file__), '../../reports/result_report.txt')

def write_to_report(message):
    with open(report_path, 'a') as report:
        report.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

@given('the source database "{source_db}"')
def step_given_source_db(context, source_db):
    global source_conn
    source_conn = connect_db(source_db)

@given('the target database "{target_db}"')
def step_given_target_db(context, target_db):
    global target_conn
    target_conn = connect_db(target_db)

@when('I compare the "{table_name}" table')
def step_when_compare_table(context, table_name):
    global source_data, target_data
    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()

    source_cursor.execute(f"SELECT * FROM {table_name}")
    source_data = source_cursor.fetchall()

    target_cursor.execute(f"SELECT * FROM {table_name}")
    target_data = target_cursor.fetchall()

@then('the row counts should match')
def step_then_row_counts_match(context):
    try:
        assert len(source_data) == len(target_data), f"Row count mismatch: {len(source_data)} vs {len(target_data)}"
        write_to_report("Row counts match.")
    except AssertionError as e:
        write_to_report(f"Row count mismatch: {e}")
        raise

@then('the data should match')
def step_then_data_should_match(context):
    try:
        assert source_data == target_data, f"Data mismatch:\nSource: {source_data}\nTarget: {target_data}"
        write_to_report("Data matches.")
    except AssertionError as e:
        write_to_report(f"Data mismatch: {e}")
        raise
