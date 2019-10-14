# Solace Codelabs
This repository is a submodule of the [site repo](https://github.com/SolaceDev/solace-dev-codelabs-site)
The site is deployed from that repo & codelab artifacts are kept here. 

There are two directories in this repo. 
* codelabs - This directory contains codelabs that will be served up on solace.dev/codelabs. You should claat export your codelab into this directory. 
* markdown - This directory contains the markdown file that the codelabs were generated from. 

## Learn About CodeLab
* CodeLabs are being created using Google Codelabs: https://github.com/googlecodelabs/tools
* A tutorial on how to create a codelab can be found here: https://solace.dev/codelabs/codelab-4-codelab
* The purpose of these codelabs is to create easily consumable, step-by-step tutorials that walk a developer how to achieve a goal.  

## How to Contribute

### Create a new CodeLab
* While Google Codelabs offers two different ways to create codelabs we ask that you stick with the _markdown_ option as our process was created to work with it. 
* Create your codelab using the markdown file option (See tutorial above if it's your first time!) 
* Be sure to update the headers in your codelab
  - Ensure the unique ID field: `id:` is present. This ID will be used in the URL so try to keep it short and human-readable. 
  - Add tags for filtering: Currently either _workshop_ for a Developer Workshop guide or _iguide_ for an Integration Guide 
  - Add a few items to `categories:` that identify technologies used such as the language, protocol, library and/or feature covered.   
* Store your codelab & referenced code (if any) in a public github repo that you reference in the codelab. 
* Clone this repo to your local machine
* Checkout the _dev_ branch
  - `git checkout dev`
* Use `claat export` to export the codelab tutorial into the codelabs directory
  - `claat export /path/to/<your-codelab.md> /path/to/solace-dev-codelabs/codelabs/`
* Copy your new codelab's markdown file under the _markdown_ directory
* Commit & Push your changes
  - `git commit -a -m 'Added a new codelab'`
  - `git push` 
* Make a Pull Request via the github UI (Allow edits so the reviewer can fix simple items) 
  - A member of the _SolaceDev_ team will review & merge the codelab or get back to you with needed updates. 

### Update an existing CodeLab
* Clone the solace-dev-codelabs repo
* Checkout the _dev_ branch
  - `git checkout dev`
* Make updates to the markdown file for your codelab in the _markdown_ directory
* Use `claat export` to export the updates into the codelabs directory
  - `claat export /path/to/<your-codelab.md> /path/to/solace-dev-codelabs/codelabs/`
* Commit & Push your changes
  - `git commit -a -m 'Added a new codelab'`
  - `git push` 
* Make a Pull Request via the github UI (Allow edits so the reviewer can fix simple items) 
  - A member of the _SolaceDev_ team will review & merge the codelab or get back to you with needed updates. 
