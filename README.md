# Finance AI Suite #

This Financial AI Application Suite showcases the creation and implementation of several AI applications that support the domain of finance.

This Suite is a compilation of programs developed under the advise of Dr. Isaac Osunmakinde of Norfolk State University.

## Description ##

These AI applications are all built using Python. Additionally several libraries and packages are necessary to run this program. The Graphical User interface must be run in the command line first. Before that however its best to install all necessarry packages. This Suite sports a GUI utilizing the [tkinter](https://docs.python.org/3/library/tkinter.html) library in python. This will need to be installed on your device as well.

## Setting Up your environment ##

The best for steps to utilize this program are to:
  - Fork this repository
  - Clone this repository locally utilizing git
  - Navigate to the repository's head folder utilizing the command line

Once you have your local clone you can proceed with utilizing the program in the following steps.

Before you can fully make use of this suite, you'll need to install python on your device, as well as the following libraries:

  - pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
  - wordcloud
  - Pyttsx3
  - pandas
  - pyPDF2
  - names
  - matplotlib
  - nltk
  - wordcloud
  - beautifulSoup4
  - transformers 
  - chess 
  - textblob
    
To make this easier, I've created a [script](https://github.com/SilasVM/Finance-AI-Suite/blob/main/PackageInstaller.py), run with `python .\PackageInstaller.py`, that will install all of these for you. Upon Completion you should see output similar to this:
<img width="1397" height="668" alt="image" src="https://github.com/user-attachments/assets/423fba7a-674a-4a0e-9d71-31f47b011897" />
This script will notify you if any installations fail.

After you've successfully run that script, you can proceed to the command line of your choice and run `python .\ProgramManager.py`. This is the script that generated the graphical user interface, and connects the documentation, videos, and code for each assignment. Upon successful run you'll see this window open:

<img width="1324" height="1029" alt="image" src="https://github.com/user-attachments/assets/6ede59bf-9ddb-4e18-936e-b0efa7334da4" />

## Utilizing the GUI and Programs ##
Each Program comes equipped with documentation describing it's functionality, PEAS, and relation to the field of Finance. It also comes with the ability to run the program, which will be reflected in the terminal you begin the Program Manager in. Additionally, a video demo of each program is provided where I speak about the specifics, the implementation decisions I made, and the features I added and their relation to the industry of finance.

In the event you're interacting with one of the higher level agents such as one of the NLP Analysis that handles dynamically added files, you must place the file in the base of the repository: `\FINANCE-AI-SUITE\` for it to be detected. Additionally, any files outputted or databases created will be placed here.

## Licensing ##

This code is currently maintained under the License Contributor Covenant Licence CC-BY-NC-SA. A descriptor image is attached for convenience:

<img width="350" height="280" alt="image" src="https://github.com/user-attachments/assets/9745a593-0bdb-4a0d-99d3-940816f14191" />
