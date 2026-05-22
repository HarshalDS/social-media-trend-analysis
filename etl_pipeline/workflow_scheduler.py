import time
from pipeline_runner import (
    extract_news_data,
    transform_news_data,
    load_processed_data
)

print("Starting Automated Workflow Scheduler...\n")

for cycle in range(3):

    print(f"\nWorkflow Execution Cycle {cycle+1}")

    # Extract
    raw_data = extract_news_data()

    # Transform
    transformed_data = transform_news_data(raw_data)

    # Load
    load_processed_data(transformed_data)

    print(f"Cycle {cycle+1} Completed Successfully!")

    print("-" * 60)

    # Wait before next cycle
    time.sleep(10)

print("\nAutomated Workflow Scheduling Completed!")