
<div align="center">
	<img src="https://devrelassets.z9.web.core.windows.net/solace-developers-logo.svg" alt="Solace Developers Logo" width="300" />
	<br/>
	<img src="https://github.com/SolaceDev/solace-dev-codelabs/actions/workflows/site-update.yml/badge.svg" alt="Update Codelabs Site" />
	<a href="https://app.netlify.com/sites/codelabs-solace/deploys">
		<img src="https://api.netlify.com/api/v1/badges/e66602c6-9a94-4095-a7c4-4e37ff2cdd41/deploy-status" alt="Netlify Status" />
	</a>
	<a href="https://github.com/SolaceDev/solace-dev-codelabs/actions/workflows/fullbrokenlink.yml">
		<img src="https://github.com/SolaceDev/solace-dev-codelabs/actions/workflows/fullbrokenlink.yml/badge.svg" alt="Weekly link checker" />
	</a>
</div>


# Solace Codelabs
The purpose of these codelabs is to create easily consumable, step-by-step tutorials that walk a developer to achieve a goal.  

This repository is included as a submodule in the main [site repo](https://github.com/SolaceDev/solace-dev-codelabs-site). The main codelabs site is deployed from that repo and codelab artifacts are kept here. 

## Directories

- codelabs - contains codelabs that will be served up on https://codelabs.solace.dev/. The raw markdown file is exported into this directory via the claat tool.  
- markdown - This directory contains the markdown file that the codelabs were generated from.     

## How to Contribute
### Prepare your repository
1. Fork this main repository by clicking on the `Fork` button on the top right  
1. From a terminal window, clone your fork of the repo `git clone git@github.com:<Your_Github_User>/solace-dev-codelabs.git`
1. Navigate to the newly cloned directory `cd solace-dev-codelabs`
1. Checkout a local branch for your new codelab `git checkout -b add-codelab-<name_of_codelab>`

### Create your own Codelab

Follow the steps found in the [Codelab to Create a Codelab](https://codelabs.solace.dev/codelabs/codelab-4-codelab/index.html?#1) codelab

## Learn About CodeLab
* CodeLabs are being created using Google Codelabs: https://github.com/googlecodelabs/tools
