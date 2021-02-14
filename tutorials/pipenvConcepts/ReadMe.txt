Create an Environment

$pipenv install packagename   # It will create an environment and install that package local to environment.

# It will create 2 files, pipfile and pipfile.lock
# pipfile contains all the packages and versions(* if no version is defined which means latest version.)
# pipfile.lock makes sure that deterministic build occurs while moving project from dev to prod as it contains actual
version of the packages installed.


$pipenv shell 		     # activates the environment.

# If we run $pipenv shell without creating an environment then new environment will be created having only Pipfile
containing all the global packages installed and No pipfile.lock will be created. So it should not be used.

$exit
# Gets out of the virtual environment.


$pipenv run python 	     # run python shell in the virtual env. If we run 

import sys
sys.executable 

# then it will give us the path to virtual env python interpreter local to the virtual env.

# using pipenv run before any command will run the command in the virtual environment without activating it.

$exit()  		# get out of python shell.


$pipenv run file.py 	# will run the file in the virtual env.

# Always use pipenv instead of pip so that the module will be installed into the virtual environment and if
 the virtual environment is not there then it gets created automatically.

--------------------- requirements.txt to pipfile-----------------------------------------------------
$pipenv install -r Location of requirements.txt		# It will create the environment with the modules defined
 in requirements.txt

# If the Environment is already there then its pipfile and pipfile.lock gets updated and appended and not 
  truncated and inserted.
 
--------------------------------- pipfile to requirements.txt------------------------------------------


$ pipenv lock -r 		# display dependencies in requirements.txt file format.

--------------- Install in dev which won't be needed in production---------------
$pipenv install datetime  --dev

$ pipenv uninstall datetime	# removes module from env

--------------# We can make changes to pipfile manually like change version of python. To do this -------------
But that version should exist on your system.

$ pipenv --python 3.6

------------------------# Removing environment and creating from scratch. ----------------------------

$pipenv --rm 		#will remove the environment completely but pipfile still remains.
$pipenv install 	#will create environment with the pipfile present in the folder.

$pipenv --venv		#path to virtual environment

$pipenv check 		# display security issues and stable versions available to resolve them.
			# edit the pip file and run the $pipenv install 	# to install correct versions.
 
$pipenv check 	# if we run this again it will show us that all issues resolved.


---------------- While moving from dev to prod use pipfile.lock instead of pipfile as it contain deterministic
versions of modules which are working on dev currently---------------------------------------------

First Run

$ pipenv lock

Move the pipfile.lock to prod and run

$ pipenv install --ignore-pipfile

It will install all the required packages.

-----------------Environment Variables Local to Project--------------------------------

create a .env file and edit it 
Format is

VARIABLE_NAME="Value"

.env file will be loaded automatically by pipenv

--------------to check value of environment variables---------------

import os
os.environ['VARIABLE_NAME']