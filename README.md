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

#Add location file to input dir
echo "New_York	12	40.70	-74.01" > ./data/input/location.lst

```

Now, run the CLI app: (note, haven't setup docker yet so this is a stand-in):

replace the abs paths with machine-specific paths to the specified files. To run without cloning & creating project on local machine:

```shell
uv run nzinsargps-verticallandmotion --pipeline-id 'nzinsargps.vlm.nzinsargpsvlm.NZInsarGPS.verticallandmotion' --input-fname path/to/data/input/NZ_2km.txt --location-file path/to/data/input/location.lst --output-path path/to/data/output --rngseed 5678
```

or: 
```shell
uvx --from git+https://github.com/e-marshall/nzinsargps-verticallandmotion.git@package nzinsargps-verticallandmotion --pipeline-id 'nzinsargps.vlm.nzinsargpsvlm.NZInsarGPS.verticallandmotion' --input-fname path/to/data/input/NZ_2km.txt --location-file path/to/data/input/location.lst --output-path path/to/data/output --rngseed 5678
 
```
**NOTE**: Seed currently set to 5678 to match `v.1`

## Features 
```shell
Usage: nzinsargps-verticallandmotion [OPTIONS]

  Run the NZInsarGPS verticallandmotion module

Options:
  --pipeline-id TEXT           Unique identifier for this instance of the
                               module. Used to name output files  [required]
  --min_qf INTEGER             Minimum value of data quality to use (default =
                               5)
  --use_boprates INTEGER       Use the BOP corrected rates instead of the raw
                               VLM rates (default = 1)
  --input-fname TEXT           input file name (??)
  --pyear-start INTEGER RANGE  Projection year start [default=2020]  [x>=2020]
  --pyear-end INTEGER RANGE    Projection year end [default=2100]  [x<=2300]
  --pyear-step INTEGER RANGE   Projection year step [default=10]  [x>=1]
  --baseyear INTEGER           Year to which projections are referenced
                               [default = 2000]
  --nsamps INTEGER             Number of samples to draw [default=500]
  --rngseed INTEGER            Seed for the random number generator
                               [default=1234]
  --location-file TEXT         Path to location file for postprocessing
  --chunksize INTEGER          Chunk size for postprocessing [default=50]
  --output-path TEXT           Path to output directory
  --help                       Show this message and exit.
  ```
See this help documentation by running:
```shell
uv run nzinsargps-verticallandmotion --help 
```   
## Results
If this module runs successfully, a single netCDF containing projections of local sea level change will appear in ./data/output. 

## Support
Source code is available online at https://github.com/stcaf-org/nzinsargps-verticallandmotion. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/stcaf-org/nzinsargps-verticallandmotion/issues.