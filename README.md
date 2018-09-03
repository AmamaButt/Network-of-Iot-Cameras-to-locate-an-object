# Threat Identification
# Guide To: 
Communicate a real-time image between two computers and identifying threats in the segmented images.
# Summary:
In this guide, you will learn what are the prerequisites for running this application and how you will install them. This guide includes step by step procedure for all the installations. Also, references are provided that will assist you in case you will fail to follow any step properly. 
Let’s start with a guide.
# Steps:
 1.	First, you must install python to your system.
2.	Type python in your desired browser and follow the first link that appears.
3.	Under the Downloads section, click on the latest available version of python. For now, which is python 3.6.4.
4.	Follow the link and you will see different versions under File heading. Select Windows x86-64 executable installer.
5.	After the setup has downloaded completely, install python to your system by running this setup. You can use default location or provide your own.
6.	Set environment variable. For this browse the drive where python has installed. Click python>>python36 and copy the path of directory.
7.	Go to start menu and then settings, select advance system settings. Click on environment variable tab, select path system variable, then click on edit and then new, paste the copied path here and click on OK.
8.	Open command prompt and type python. It will give you correct version of python that you have installed recently. Now python has installed successfully.
9.	Now you must download Visual Studio Code editor for python. Type editor name in your browser and click on the link https://code.visualstudio.com.
10.	Click on Download For Windows button and the arrow which is in front of Windows x64 installer as we must download suitable executable file for our system.
11.	Simply follow the setup wizard and install code editor to your system.
12.	Launch Visual Studio Code editor and install python extension and click on reload button to reload your editor.
13.	Using open folder option, you can use default directory for your python files having extension .py
14.	If you have provided customized location of python at the time of installation, you must validate path “python”. Open launch.json file which is located in .vscode directory.
15.	Go to File>>preferences>>settings. On left side, you will see DEFAULT settings and on right side, USER settings are available.
16.	Search for pythonPath here and you must copy python executable file location to USER settings.
17.	If you have problem regarding steps discussed above. See this toturial https://www.youtube.com/watch?v=dNFgRUD2w68 
18.	Now we will install OpenCV3 for python3. Prerequisites for are OpenCV3:
a.	Python
b.	Microsoft Visual C++ 2015 Redistributable.
c.	Numpy
19.	We will use a wheel package from python libraries repository in order to install opencv and numpy which is a prerequisite for opencv.
20.	Click on the <link> and search numpy, you will see different versions of Numpy. Download suitable whl file that matches to your system and with the version of python.
21.	Similarly, download appropriate whl file for opencv. Install these using pip install utility.
22.	Run command prompt as an administrator and type pip install and then name of numpy whl file. Just type the start of whl file and press tab, it will automatically complete the whl file name here. Press enter.
23.	Repeat the same process for opencv. If you have any problem regarding downloading of numpy and opencv see this https://www.youtube.com/watch?v=izN-NLpS5t8&t=181s
24.	 Now all installations are complete. Place the server-side code at your server and vice versa for client.
25.	Now make sure that your PC’s are on same local network and reach or ping. each other 
26.	Run the server code first and then client one. Connection has been established and client send the real-time captured image to server.
27.	Server will do the processing and return the threats results to client which is required.


