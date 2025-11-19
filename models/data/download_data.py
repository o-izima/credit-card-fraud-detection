import os
import zipfile
import subprocess
'''
This script:

✔ Checks that Kaggle API is installed
✔ Validates your Kaggle credentials
✔ Downloads the dataset
✔ Unzips it into a data/ folder
✔ Works in GitHub Codespaces, Colab, and local environments
'''

DATASET = "mlg-ulb/creditcardfraud"
OUTPUT_DIR = "data"
ZIP_PATH = os.path.join(OUTPUT_DIR, "creditcardfraud.zip")

def ensure_kaggle_api():
    """Ensure Kaggle API is installed."""
    try:
        import kaggle  # noqa
    except ImportError:
        print("Kaggle package not found. Installing...")
        subprocess.check_call(["pip", "install", "kaggle"])

def ensure_kaggle_credentials():
    """Ensure the user has Kaggle credentials configured."""
    kaggle_dir = os.path.expanduser("~/.kaggle")
    kaggle_json = os.path.join(kaggle_dir, "kaggle.json")

    if not os.path.exists(kaggle_json):
        raise FileNotFoundError(
            "❌ Kaggle API credentials not found!\n"
            "You must upload your kaggle.json file to ~/.kaggle/kaggle.json\n"
            "Steps:\n"
            "1. Go to https://www.kaggle.com/account\n"
            "2. Click 'Create New API Token'\n"
            "3. Place kaggle.json inside ~/.kaggle/\n"
            "4. Run again."
        )
    else:
        os.chmod(kaggle_json, 0o600)

def download_dataset():
    """Download dataset using Kaggle API."""
    print("Downloading dataset from Kaggle...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    subprocess.check_call([
        "kaggle", "datasets", "download",
        "-d", DATASET,
        "-p", OUTPUT_DIR
    ])

    print("Download complete.")

def unzip_dataset():
    """Unzip the downloaded dataset."""
    if os.path.exists(ZIP_PATH):
        print("Extracting dataset...")
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(OUTPUT_DIR)
        print(f"Files extracted to: {OUTPUT_DIR}")
    else:
        print("❌ Zip file not found, extraction skipped.")

def main():
    ensure_kaggle_api()
    ensure_kaggle_credentials()
    download_dataset()
    unzip_dataset()
    print("\n✅ Dataset download and extraction complete!")

if __name__ == "__main__":
    main()
