1. System requirements
- Code should be able to run in any computer capable of running the Anaconda Python Distribution
- Code was tested using the python packages described in requirements.txt in a Windows10 system

2. Installation instructions

- Make sure you have a python3 installation (Anaconda distribution recommended)
- Install python package requirements included in the requirements.txt file (using a new python environment is recommended)

3. Demo and usage Instructions:
- Use measure2kymographs.py to measure the angle of 2 kymographs:
	- script will ask the user to select one kymograph at a time
	- then it will print in the terminal the angles of both kymographs and ask the user where it should save resulting images
- Use batchanalysis.py to measure the kymographs of several cells:
	- script will ask for a folder containing cells to measure
	- folder structure should be the same as in the example folder (included in the zip file)
		- each Cell folder should be name Cell_X, with X being cell number
		- for each cell, the batch script expects the folder to contain the kymographs (kym1 and kym2) and a crop of the cell containing the lines used to generate the kymographs (kymline1 and kymline2)
	- then inside the selected folder it will save an html report containing the result of the analysis
- Both options can be used to test the code using the example data in the "example" folder
	- expected result can be seen in the file "report.html" contained in the example folder

- Code execution should take less than 1 minute for batches of less than 1000 cells

Copyright (c) 2020, Bacterial Cell Biology Lab, ITQB-NOVA
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
