## OCR Project

##Setup Environment

1. Install python distribution or anaconda  for the project.
	* Follow the [link](https://docs.anaconda.com/anaconda/install/) for installation guide for Anaconda
2. There are 2 ways to install packages in anaconda environment 
	1. After installing anaconda, create an environment using [link](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
		* Activate the conda environment using `conda activate`
		* Install packages in `environment.yml` using pip 
	2.  After installing anaconda, import the evironment "reciept_project" directly from the environment.yml using `conda env create -f environment.yml` command
3.  Activate the corresponding environment
4.  Famalirise yourself from Django structure using [Tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
5. Run `python manage.py runserver` from OCR> web_ocr to run the server

## Responsible APIs

1. `http://127.0.0.1:8000/ocr/upload_image` 
	* method = POST
	* form-data : key : 'myfile', value : 'image' (input type = file)
	* returns : 
		* uuid (if ocr successful )
		* Message (Reupload the image with correct orientation and using black background)

2. `http://127.0.0.1:8000/ocr/get_crop_and_ocr`
	* method = POST
	* form-data : key : 'uuid', value : 'text' (input type = text)
	* returns : 
		* zip file (auto downloaded) 
		* Message (if uuid is not correct, do ocr again and copy uuid correctly)


