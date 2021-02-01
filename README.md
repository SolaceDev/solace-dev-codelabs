![Update Codelabs Site Repo](https://github.com/SolaceDev/solace-dev-codelabs/workflows/Update%20Codelabs%20Site%20Repo/badge.svg)
[![Netlify Status](https://api.netlify.com/api/v1/badges/e66602c6-9a94-4095-a7c4-4e37ff2cdd41/deploy-status)](https://app.netlify.com/sites/focused-beaver-3cc79d/deploys)
![Broken Links Checker](https://github.com/SolaceDev/solace-dev-codelabs/workflows/Broken%20Links%20Checker/badge.svg)


# Solace Codelabs
The purpose of these codelabs is to create easily consumable, step-by-step tutorials that walk a developer to achieve a goal.  

This repository is included as a submodule in the main [site repo](https://github.com/SolaceDev/solace-dev-codelabs-site). The site is deployed from that repo and codelab artifacts are kept here. 

## Directories

- codelabs - contains codelabs that will be served up on https://codelabs.solace.dev/. The raw markdown file is exported into this directory via the claat tool.  
- markdown - This directory contains the markdown file that the codelabs were generated from.     

## How to Contribute
### Prepare your repository
1. Fork this main repository by clicking on the `Fork` button on the top right  
1. From a terminal window, clone your fork of the repo `git clone git@github.com:<Your_Github_User>/solace-dev-codelabs.git`
1. Navigate to the newly cloned directory `cd solace-dev-codelabs`
1. Checkout a local branch for your new codelab `git checkout -b add-codelab-<name_of_codelab>`

### Option 1 - Script
1. [Setup your environment](https://codelabs.solace.dev/codelabs/codelab-4-codelab/index.html?#1)
1. [Read the solace guidelines](https://codelabs.solace.dev/codelabs/codelab-4-codelab/index.html?#2)
1. From the root directory, run `./init.sh <name-of-codelab>` script
1. Navigate to `/markdown/name-of-codelab`
1. Run the following from terminal `npm install; npm run watch`
1. Edit your `<name-of-codelab>.md` file in your text editor of choice
1. When ready, run `export.sh`
1. Navigate to the codelabs root directory (`cd ../../`), add and commit your changes in a PR. From the root directory,    
```
cd ../../ #to navigate to the root of the codelabs dir
git add .
git commit -m "add new codelab: <name of codelab>"
git push origin add-codelab-<name_of_codelab>
```
Note: _origin_  in the command above the name of the remote repository. If your remote repository is of a different name then you will have to `git push <name_of_remote_repo> add-codelab-<name_of_codelab>`

### Option 2 - Manual

Follow the steps in this tutorial: https://codelabs.solace.dev/codelabs/codelab-4-codelab

Note: original markdown of this codelab is found under [codelabs/codelab-4-codelab](./codelabs/codelab-4-codelab)

## Learn About CodeLab
* CodeLabs are being created using Google Codelabs: https://github.com/googlecodelabs/tools