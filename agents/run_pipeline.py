import subprocess

print("Running Downloader...")
subprocess.run(
    ["python", "agents/downloader/main.py"]
)

print("Running Metadata...")
subprocess.run(
    ["python", "agents/metadata/mock_analyze.py"]
)

print("Pipeline Complete")