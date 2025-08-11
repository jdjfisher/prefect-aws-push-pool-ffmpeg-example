from prefect import flow
import subprocess

@flow(log_prints=True, timeout_seconds=60)
async def example_flow(message: str = "Hello, World!"):
    print(message)
    result = subprocess.run("ffmpeg -version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    version = result.stdout.decode('utf-8')
    print(f"FFmpeg version: {version}")