from prefect import flow, task
import subprocess
import requests


@flow(log_prints=True, timeout_seconds=60)
def trim_video(
    trim_start: int,
    trim_end: int,
    source_url: str,
    destination_url: str,
):
    if trim_start < 0 or trim_end <= trim_start:
        raise ValueError("Invalid trim start or end values")

    download_video(source_url)
    invoke_ffmpeg(trim_start, trim_end)
    upload_video(destination_url)


@task
def download_video(source_url: str):
    response = requests.get(source_url, stream=True)
    response.raise_for_status()

    with open("input_video.mp4", "wb") as file:
        file.write(response.content)

    print(f"Video downloaded")


@task
def invoke_ffmpeg(trim_start: int, trim_end: int):
    command = [
        "ffmpeg",
        "-y",  # Overwrite output file if it exists
        "-i",
        "input_video.mp4",
        "-ss",
        str(trim_start),
        "-to",
        str(trim_end),
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        "output_video.mp4",
    ]
    result = subprocess.run(
        command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    print(result.stdout.decode())

    print(f"Video trimmed from {trim_start} to {trim_end} seconds")


@task
def upload_video(destination_url: str):
    with open("output_video.mp4", "rb") as file:
        response = requests.put(destination_url, data=file)
        response.raise_for_status()

    print(f"Video uploaded")
