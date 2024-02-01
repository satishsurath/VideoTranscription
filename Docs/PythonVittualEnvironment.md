# Using Conda

## Create Virtual Envrionment using Conda

```bash
conda create --name VideoTranscription python=3.11
```


Succesful creation of virtual environment will show the following message:

```bash
#
# To activate this environment, use
#
#     $ conda activate VideoTranscription
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```


## Activate Virtual Environment
```bash
conda activate VideoTranscription
```


## Deactivate Virtual Environment
```bash
conda deactivate
```
## Remove Virtual Environment
```bash
conda remove --name VideoTranscription --all
```


# Using Virtualenv

## Create Virtual Envrionment using Virtualenv
```bash
pip install virtualenv
```
## Create Virtual Environment
```bash
virtualenv VideoTranscription
```
## Activate Virtual Environment
```bash
source VideoTranscription/bin/activate
```
## Deactivate Virtual Environment
```bash
deactivate
```
## Remove Virtual Environment
```bash
rm -rf VideoTranscription
```