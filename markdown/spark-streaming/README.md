# Streaming between Solace and Databricks

> **🚧 Under construction.** This codelab is being rewritten for connector 3.1.7 and Databricks. The step content is in place, but the screenshots are still placeholders, see the alt text on each image in `spark-streaming.md` for what to capture before this goes live.

Source markdown for the [Streaming between Solace and Databricks](https://codelabs.solace.dev/codelabs/spark-streaming/index.html) codelab, built with [claat](https://github.com/googlecodelabs/tools/tree/master/claat).

Runnable companions (a Databricks notebook, a self-managed `spark-submit` project, a sample publisher, and a `docker-compose.yml`) live in [`code/`](code/).

## Build and run locally

### 1. Install Go

```bash
brew install go
```

Other platforms: [golang.org/dl](https://golang.org/dl/).

### 2. Set up Go environment variables

```bash
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

See the [Go install docs](https://golang.org/doc/install) for other OS options.

### 3. Install claat

```bash
go install github.com/googlecodelabs/tools/claat@latest
```

Confirm it installed:

```bash
claat
```

### 4. Install Node dependencies

```bash
npm install
```

### 5. Watch and serve

```bash
npm run watch
```

This exports `spark-streaming.md` with claat, starts a local claat server, and opens the rendered codelab in your browser. Every time you save `spark-streaming.md`, it rebuilds and refreshes automatically.

### 6. Export for the site

Once you're happy with the content, export the final HTML and copy it into `codelabs/spark-streaming/` so it can be picked up by the deployed site:

```bash
claat export spark-streaming.md
rm -rf ../../codelabs/spark-streaming
cp -r spark-streaming ../../codelabs/spark-streaming
rm -rf spark-streaming
```
