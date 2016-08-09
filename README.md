# Jupyter Notebook on OpenShift using the DIY cartridge

## FUATURE

* Python 3.5.2
* Jupyter Notebook
    * IPython Widgets
    * Jupyter Notebook Extensions
* Numpy
* Scipy
* Matplotlib
* Pandas
* Networkx


*****

## INSTALLATION INSTRUCTIONS

### 1. Create your application on OpenShift

- Select **Do-It-Yourself 0.1** cartridge on the Choice a type of application form.
- Don't have to enter a git repository url on the Configure the application form.

### 2. Clone your application repository

````
git clone ssh://************************@appname-namespace.rhcloud.com/~/git/appname.git/
cd appname
````

### 3. Delete template application source code

````
git rm -r README.md diy misc .openshift
git commit -m "Remove template application"
````

### 4. Pull source code from this repository

````
git remote add github https://github.com/magichan-lab/openshift-diy-jupyer.git
git fetch github
git merge --allow-unrelated-histories github/master
````

### 5. Push changes

````
git push
````

Wait for build to finish (This may take at 20 minutes)


### 6. Open Jupyter Notebook page

Open your application url in browser and verify

~~you must enter the password : openshift (default)~~

