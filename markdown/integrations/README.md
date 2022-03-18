# Integration Guides
Solace has a list of integration guides that can be found here https://docs.solace.com/Developer-Tools/Integration-Guides/Integration-Guides.htm

The original sourcecode of the guides can be found here https://github.com/SolaceLabs/solace-integration-guides


## Contribution 

Following the instructions in the [main read me](../../README.md), make sure you ave the following prerequisites on your machine
1. GoLang
2. Claat  
1. Node


### Create a new codelab
To author a new codelab, simply run the init.sh script with the name of the integration guide as follows
```
./init.sh <name_of_integration_guide>
```

### Run codelabs locally
After creating the codelab template, 
1. Navigate to the directory `cd <name_of_codelab>`
1. Install dependencies `npm install`
1. Run the local claat server `npm run watch`

Then you can modify the `<name_of_codelab>.md` file and watch the changes in your browser

### Publish
When ready:
1. Export your codelab by running the `./export.sh` script
1. Open up a PR on github with your new integration guide
