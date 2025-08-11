
from prefect import flow
from prefect.deployments import run_deployment  
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: python invoke.py <trim_start> <trim_end> <source_url> <destination_url>")
        sys.exit(1)

    trim_start = int(sys.argv[1])
    trim_end = int(sys.argv[2])
    source_url = sys.argv[3]
    destination_url = sys.argv[4]

    run_deployment("trim-video/poc-trim-video", parameters={
        "trim_start": trim_start,
        "trim_end": trim_end,
        "source_url": source_url,
        "destination_url": destination_url
    })


if __name__ == "__main__":
    main()