![Codelabs Site up to date](https://github.com/SolaceDev/solace-dev-codelabs/workflows/Update%20Codelabs%20Site/badge.svg)
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
1. From the root directory, run `./init.sh <name-of-codelab>` script
1. Navigate to `/markdown/name-of-codelab`
1. Run the following from terminal `npm install; npm run watch`
1. Edit your `<name-of-codelab>.md` file in your text editor of choice
1. When ready, run `export.sh`
1. Add and commit your changes in a PR. From the root directory,    
```
git add .
git commit -m "add new codelab: <name of codelab>"
git push origin add-codelab-<name_of_codelab>
```

### Option 2 - Manual

Follow the steps in this tutorial: https://codelabs.solace.dev/codelabs/codelab-4-codelab

Note: original markdown of this codelab is found under [codelabs/codelab-4-codelab](./codelabs/codelab-4-codelab)

## Learn About CodeLab
* CodeLabs are being created using Google Codelabs: https://github.com/googlecodelabs/tools