from prefect import flow
import os

@flow(log_prints=True, timeout_seconds=60)
async def example_flow(message: str = "Hello, World!"):
    print(message)
    os.system("ffmpeg -version")
