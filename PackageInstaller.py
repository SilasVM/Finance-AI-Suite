import subprocess
import sys

#Packages that will be installed
packages = [ "torch", "torchvision", "torchaudio", "wordcloud", "pyttsx3", "pandas", "PyPDF2", "names", 
            "matplotlib", "nltk", "beautifulsoup4", "transformers", "chess", "textblob"]

#Installing packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#Need to install CPU version of PyTorch
subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "torch", "torchvision", "torchaudio",
    "--index-url", "https://download.pytorch.org/whl/cpu"
])

#Installing the rest of the packages
for package in packages[3:]:  #Skipping the first 3 becausethey're included above
    try:
        install(package)
        print(f"Installed {package}")
    except Exception as e:
        print(f"Failed to install {package}: {e}")

print("All installations complete!")
