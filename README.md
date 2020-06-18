# Solace Codelabs
The purpose of these codelabs is to create easily consumable, step-by-step tutorials that walk a developer to achieve a goal.  

This repository is included as a submodule in the main [site repo](https://github.com/SolaceDev/solace-dev-codelabs-site). The site is deployed from that repo and codelab artifacts are kept here. 

## Directories

- codelabs - contains codelabs that will be served up on https://codelabs.solace.dev/. The raw markdown file is exported into this directory via the claat tool.  
- markdown - This directory contains the markdown file that the codelabs were generated from.     

## How to Contribute
### Option 1 - Script
1. From the root directory, run `./init.sh <name-of-codelab>` script
1. Navigate to `/markdown/name-of-codelab`
1. Run the following from terminal `npm install; npm run watch`
1. Edit your `<name-of-codelab>.md` file in your text editor of choice
1. When ready, run `export.sh`
1. Add and commit your changes in a PR

### Option 2 - Manual

Follow the steps in this tutorial: https://codelabs.solace.dev/codelabs/codelab-4-codelab

Note: original markdown of this codelab is found under [codelabs/codelab-4-codelab](./codelabs/codelab-4-codelab)

## Learn About CodeLab
* CodeLabs are being created using Google Codelabs: https://github.com/googlecodelabs/tools