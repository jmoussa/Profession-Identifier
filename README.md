# Profession Identifier 

This is a simple image recognition model that is trained on the training set in the `idenprof/` folder (you have to unzip it).
I think I'm going to try and make a fun little app out of it "Which profession do you look like" or something like that.

I included the model as the `.h5` file so you don't have to train the models yourself.

Essentially, you will input a picture of a person and it will guess the profession of said person.

## Requirements
- [Anaconda](https://docs.anaconda.com/anaconda/install/) (this project uses `conda` commands for maintaining viritual environments)
- python 3.7+

## Setup
In the root directory of the repository run the following commands:

```Shell
>> conda env create -f environment.yml  
>> conda deactivate
>> conda activate profession_identifier 
```

Get the training zip file [here](https://github.com/OlafenwaMoses/IdenProf/releases/download/v1.0/idenprof-jpg.zip) and unzip it in a folder outside this current directory named `files`.
Get an already trained model (79% accuracy) [here](https://github.com/OlafenwaMoses/IdenProf/releases/download/v1.0/idenprof_061-0.7933.h5) and store it in the directory outside of this repo called `files`.

---

## Run 

```Shell
>> python test.py <path_to_image_file>
```
