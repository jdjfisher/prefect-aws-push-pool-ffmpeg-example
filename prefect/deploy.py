from flow import trim_video
from prefect.docker import DockerImage
import os
import subprocess

def main():
    registry = os.getenv('DOCKER_REGISTRY');

    if not registry:
        raise ValueError('Missing env var DOCKER_REGISTRY')

    image = f"{registry}/prefect-flows:latest"

    # Manually running buildx for amd64 
    subprocess.run(
        ["docker", "buildx", "build", '--platform', "linux/amd64", "-t", image, ".", '--push'],
        check=True,
    )

    trim_video.deploy(
        name="poc-trim-video",
        work_pool_name="aws-push-pool",
        image=DockerImage(
            name=image,
            dockerfile="Dockerfile",
        ),
        build=False,
    )


if __name__ == "__main__":
    main()
