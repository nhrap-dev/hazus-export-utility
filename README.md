# Hazus Export Tool

The Hazus Export Tool summarizes Hazus risk assessment results stored on your desktop Hazus database in a handful of text files, shapefiles, and a one-page graphic report. Launch the tool by double-clicking the "hazus-export-tool.py" file in the download folder.

The Hazus Export Tool is developed using the Hazus Python Package, HazPy. HazPy tools automatically check for updates each time they are opened. Hazus Python Package documentation is found here: https://github.com/nhrap-hazus/hazus

## Requirements

The Hazus Export tool requires Hazus, ArcGIS Desktop, and conda to be installed on your computer. Conda is a free software package manager that automatically manages all Python packages required to run Hazus open source tools - including the Hazus Python package: https://fema-nhrap.s3.amazonaws.com/Hazus/Python/build/html/index.html - conda can be installed with Miniforge. Miniforge can be installed with the following steps:

1. Download the repository from: https://github.com/nhrap-dev/Environment-Setup

2. Unzip the downloaded folder and run the python script install-miniforge.py


## Documentation

For information about the fields, values and units found in exported Hazus results data, please refer to the guide sheets in the data-dictionaries folder: "EQDataDictionary", "TSDataDictionary", "FLDataDictionary", and "HUDataDictionary". https://github.com/nhrap-hazus/export/tree/master/data-dictionaries 

## Contact

Issues can be reported through the repository on Github (https://github.com/nhrap-hazus/export)

For questions contact fema-hazus-support@fema.dhs.gov

## To Use

Follow the steps below to run Export. To ensure .py files run when double-clicked, right-click the .py file and go to Properties. Under the "General" tab next to "Opens With", make sure "python.exe" is selected. If not, click "Change" and select "python.exe" from your Python installation directory.

**1. Download zip folder from GitHub, unzip.**

![Download Export](Images/Step1.png "Download Export")

**2. Double-click "hazus-export-tool.py". If you don't have the Hazus Python Library installed, follow the prompt to install, then double-click "hazus-export-tool.py" again**

![Open Export](Images/Step2.png "Open Export")

**3. Select a study region to export from those stored in your dekstop Hazus database, as shown in the drop-down menu.**

![Select Study Region](Images/Step3.png "Select Study Region")

**4. Provide a Report Title and type notes about your selected Hazus analysis (model inputs, date, settings, version, etc.). Metadata are required to share your model results with FEMA!**

![Analysis Information](Images/Step4.png "Analysis Information")

**5. Select summary information to export and a folder destination for exported files.**

![Summary Information and Destination](Images/Step6.png "Summary Information and Destination")

**6. Click "Run".**

![Run and Review](Images/Step7.png "Run and Review")
