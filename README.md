# nzinsargps-verticallandmotion

Application producing ...
This module contains the vertical land motion module from the NZInsarGPS workflow.

> [!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Example

First, create a new directory and download the required input data for the run:
```shell
mkdir -p ./data/input
curl -sL https://zenodo.org/record/7478192/files/NZInsarGPS_verticallandmotion_preprocess_data.tgz | tar -zx -C ./data/input

#Make directory for outputs
mkdir -p ./data/output
```
