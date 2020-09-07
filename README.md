# phi-fun
Experimenting with Phi and other measures applied to EEG/brain networks

## Installation
From a command prompt...

1. Download the code from github
```
git clone https://github.com/DWonGH/phi-fun.git
```
2. Move into the new folder
```
cd phi-fun
```
3. Install the requirements 

This step is untested; we may need to add some requirements in the txt file.
```
pip install -r requirements.txt
```
## Get some data 
This will download about 100 MB from the TUEG dataset, unless you change maxSize below. 
To get a password, sign up here (or ask someone in your group): 
https://www.isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml.

```
python
import tueg_tools
ds = tueg_tools.Dataset('/pathToWhereYouWantToStoreTheDataOnYourComputer')
ds.download('https://www.isip.piconepress.com/projects/tuh_eeg/downloads/tuh_eeg_abnormal/',
            password='Your Password', maxSize=10**8)
exit()
```
## Demo script to load some data

In command prompt, enter the following command (editing the path as necessary).
```
python load_eeg.py path/to/an/edfFile.edf
```



