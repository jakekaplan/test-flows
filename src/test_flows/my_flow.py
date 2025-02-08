from prefect import flow
from test_flows.constant import CONSTANT

@flow(log_prints=True)
def my_flow():
    print(CONSTANT)

if __name__ == "__main__":
    my_flow()