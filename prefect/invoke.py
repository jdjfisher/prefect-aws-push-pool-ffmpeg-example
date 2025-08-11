
from prefect import flow
from prefect.deployments import run_deployment  
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python invoke.py <message>")
        sys.exit(1)

    message = sys.argv[1]

    run_deployment("example-flow/poc-example", parameters={"message": message})


if __name__ == "__main__":
    main()