export _VERSION_=3.8
echo[$(data)]: "START"
echo[$(data)]: "Creting conda env with python 3.8"
conda create --prefix ./env python=3.8 -y
echo[$(data)]: "Activating environment"
source activate ./env
echo[$(date)]: "Installing the requirements"
pip install -r requirements_dev.txt
echo[$(data)]: "END"