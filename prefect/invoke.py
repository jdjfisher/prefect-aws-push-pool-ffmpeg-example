
from prefect import flow
from prefect.deployments import run_deployment  


def main():
    run_deployment("example_flow/poc-example", parameters={"message": "Hello, Prefect!"})


if __name__ == "__main__":
    main()