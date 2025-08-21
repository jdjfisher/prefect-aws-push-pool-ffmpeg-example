from flow import trim_video
from prefect.docker import DockerImage
import os

def main():
    registry = os.getenv('DOCKER_REGISTRY');

    if not registry:
        raise ValueError('Missing env var DOCKER_REGISTRY')

    image = f"{registry}/prefect-flows:latest"

    trim_video.deploy(
        name="poc-trim-video",
        work_pool_name="aws-push-pool",
        build=True,
        image=DockerImage(
            name=image,
            dockerfile="Dockerfile",
            platform="linux/arm64"
        ),
    )


if __name__ == "__main__":
    main()
