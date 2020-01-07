# Solace Codelabs
This repository is a submodule of the [site repo](https://github.com/SolaceDev/solace-dev-codelabs-site)
The site is deployed from that repo & codelab artifacts are kept here. 

There are two directories in this repo. 
* codelabs - This directory contains codelabs that will be served up on codelabs.solace.dev. You should claat export your codelab into this directory. 
* markdown - This directory contains the markdown file that the codelabs were generated from. 

## Learn About CodeLab
* CodeLabs are being created using Google Codelabs: https://github.com/googlecodelabs/tools
* **A tutorial on how to create a codelab can be found here: https://codelabs.solace.dev/codelabs/codelab-4-codelab**
* The purpose of these codelabs is to create easily consumable, step-by-step tutorials that walk a developer how to achieve a goal.  

## How to Contribute

### Create a new CodeLab
* While Google Codelabs offers two different ways to create codelabs we ask that you stick with the _markdown_ option as our process was created to work with it. 
* Create your codelab using the markdown file option (See tutorial above if it's your first time!) 
* Be sure to update the headers in your codelab
  - Ensure the unique ID field: `id:` is present. This ID will be used in the URL so try to keep it short and human-readable. 
  - Add tags for filtering: Currently either _workshop_ for a Developer Workshop guide or _iguide_ for an Integration Guide 
  - Add a few items to `categories:` that identify technologies used such as the language, protocol, library and/or feature covered. **List the main technology first as right now that is the only item that is filterable on codelabs.solace.dev
  - Add analytics account: UA-3921398-10
* Store your codelab & referenced code (if any) in a public github repo that you reference in the codelab. 
* Clone this repo to your local machine
* Checkout a new branch for your codelab with a name that makes sense
  - `git checkout -b add-my-codelab`
* Create a directory under the _markdown_ directory with your unique codelab id
  - `mkdir /path/to/solace-dev-codelabs/markdown/<unique_id> 
* Copy your new codelab's markdown file under the _markdown/<unique_id>_ directory
* If applicable, copy your _img_, _images_, or other files necessary for your codelab into the _markdown/<unique_id>_ directory as well
* Use `claat export` to export the codelab tutorial & then move it into the codelabs directory
  - `cd /path/to/solace-dev-codelabs/markdown/<unique_id>`
  - `claat export <unique_id>.md`
  - `mv <unique_id> ../../codelabs/`
* Serve & Review your codelab in **Incognito** mode to ensure your changes look good
  - `cd ../../codelabs`
  - `claat serve`
  - Open `localhost:9090` in your browser in **Incognito** mode
  - Verify all looks good; if not then make changes and redo the export & verification.  
* Commit & Push your changes
  - `git commit -a -m 'Added a new codelab <unique_id>'`
  - `git push --set-upstream origin add-my-codelab` 
* Make a Pull Request via the github UI (Allow edits so the reviewer can fix simple items) 
  - A member of the _SolaceDev_ team will review & merge the codelab or get back to you with needed updates. 

### Update an existing CodeLab
* Clone the solace-dev-codelabs repo
* Checkout a new branch for your changes with a name that makes sense
  - `git checkout -b update-codelab-foo-bar`
* Make updates to the markdown file for your codelab in the _markdown/<unique_id>_ directory
* Use `claat export` to export the updates and move them into the codelabs directory
  - `cd /path/to/solace-dev-codelabs/markdown/<unique_id>`
  - `claat export <unique_id>.md`
  - `mv <unique_id> ../../codelabs/`
* Serve & Review your codelab in **Incognito** mode to ensure your changes look good
  - `cd ../../codelabs`
  - `claat serve`
  - Open `localhost:9090` in your browser in **Incognito** mode
  - Verify all looks good; if not then make changes and redo the export & verification.  
* Commit & Push your changes
  - `git commit -a -m 'Added a new codelab'`
  - `git push --set-upstream origin update-codelab-foo-bar` 
* Make a Pull Request via the github UI (Allow edits so the reviewer can fix simple items) 
  - A member of the _SolaceDev_ team will review & merge the codelab or get back to you with needed updates. 
