# dvc-ML-AIOps
# STEPS:
## STEP 01: Create a empty remote repository


## STEP 02: intialize a git local repository and connect to remote repository

* open and project folder in VS code then follow below command -

```bash
echo "# dvc-ML-AIOps" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/USER_NAME/REPO_NAME.git
git push -u origin main
```

```bash
touch .gitignore
```
content of the gitignore can be found from reference repository


## STEP 03: create and activate conda environment

```bash
conda create -n dvc python=3.7 -y
conda activate dvc
```

```bash
pip install -r requirements.txt
```

```bash
dvc init
mkdir -p src/utils
touch src/__init__.py
touch src/utils/__init__.py
touch params.yaml dvc.yaml
mkdir config
touch config/config.yaml
touch src/stage_01_load_save.py
touch src/utils/all_utils.py
touch setup.py
```

```
touch artifacts/.gitignore
dvc repro
```

