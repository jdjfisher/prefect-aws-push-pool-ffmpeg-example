from flow import example_flow
from prefect.docker import DockerImage

def main():
    example_flow.deploy(
        name="poc-example",
        work_pool_name="aws-push-pool",
        image=DockerImage(
            name="poc-example:latest",
            platform="linux/amd64",
        )
    )


if __name__ == "__main__":
    main()
