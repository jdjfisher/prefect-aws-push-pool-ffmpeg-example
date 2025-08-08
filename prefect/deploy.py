from flow import example_flow
from prefect.docker import DockerImage
import os

def main():
    registry = os.getenv('DOCKER_REGISTRY');

    if not registry:
        raise ValueError('Missing env var DOCKER_REGISTRY')

    example_flow.deploy(
        name="poc-example",
        work_pool_name="aws-push-pool",
        image=DockerImage(
            name=f"{registry}/prefect-flows:latest",
            dockerfile="Dockerfile",
        ),
    )


if __name__ == "__main__":
    main()
