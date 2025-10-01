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

After you've cloned the repo and downloaded the necessary data, from the root directory, create a docker container:
```shell
docker build -t nzinsargps-verticallandmotion .
```

Then, run the container, mounting a volume in the container to the location of the repo on your machine, the location of the input data and where the output data will be written. Execute the application and pass the necessary arguments to the CLI tool:
```shell
 docker run --rm \                                                          
  -v path/to/nzinsargps-verticallandmotion:/opt/nzinsargps_vlm \
  -v ./data/input:/input:ro \
  -v ./data/output:/output \
  -w /opt/nzinsargps_vlm \
  nzinsargps-verticallandmotion \
  --input-fname /input/NZ_2km.txt \
  --location-file /input/location.lst \
  --output-lslr-file /output/lslr.nc \
  --rngseed 5678
```

## Features 
```shell
Usage: nzinsargps-verticallandmotion [OPTIONS]

  Run the NZInsarGPS verticallandmotion module

Options:
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
  --output-lslr-file TEXT      Path to output lslr netCDF file
  --help                       Show this message and exit.
  ```

See this help documentation by passing the `--help` flag when running the application in any of the options above. For example: 


```shell
docker run --rm nzinsargps-verticallandmotion --help
```

## Results
If this module runs successfully, a single netCDF containing projections of local sea level change will appear in ./data/output. 

## Support
Source code is available online at https://github.com/stcaf-org/nzinsargps-verticallandmotion. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/stcaf-org/nzinsargps-verticallandmotion/issues.
