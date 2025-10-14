# nzinsargps-verticallandmotion

This module contains the vertical land motion module from the NZInsarGPS workflow of the Framework for Assessing Changes To Sea-level ([FACTS](https://github.com/radical-collaboration/facts) `v1.0`.

> [!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Example
Clone the GitHub repository:
```shell
git clone git@github.com:fact-sealevel/nzinsargps-verticallandmotion
```

Create a new directory and download the required input data for the run:
```shell
mkdir -p ./data/input
curl -sL https://zenodo.org/record/7478192/files/NZInsarGPS_verticallandmotion_preprocess_data.tgz | tar -zx -C ./data/input

#Make directory for outputs
mkdir -p ./data/output

#Add location file to input dir
echo "New_York	12	40.70	-74.01" > ./data/input/location.lst
```

Then, run the container associated with the package, passing the necessary arguments to the CLI tool:
```shell
docker run --rm \
-v ./data/input:/mnt/nz_vlm_data_in:ro \
-v ./data/output:/mnt/nz_vlm_data_out \
ghcr.io/fact-sealevel/nzinsargps-verticallandmotion:edge \
--input-fname /mnt/nz_vlm_data_in/NZ_2km.txt \
--location-file /mnt/nz_vlm_data_in/location.lst \
--output-lslr-file /mnt/nz_vlm_data_out/lslr.nc 
```

## Features 
```shell
Usage: nzinsargps-verticallandmotion [OPTIONS]

  Run the NZInsarGPS verticallandmotion module

Options:
  --min-qf INTEGER             Minimum value of data quality to use (default =
                               5)
  --use-boprates INTEGER       Use the BOP corrected rates instead of the raw
                               VLM rates (default = 1)
  --input-fname TEXT           Input .txt file  [required]
  --pyear-start INTEGER RANGE  Projection year start [default=2020]  [x>=2000]
  --pyear-end INTEGER RANGE    Projection year end [default=2100]  [x<=2300]
  --pyear-step INTEGER RANGE   Projection year step [default=10]  [x>=1]
  --baseyear INTEGER RANGE     Year to which projections are referenced
                               [default = 2000]  [2000<=x<=2300]
  --nsamps INTEGER             Number of samples to draw [default=500]
  --rngseed INTEGER            Seed for the random number generator
                               [default=1234]
  --location-file TEXT         Path to location file for postprocessing
                               [required]
  --chunksize INTEGER          Chunk size for postprocessing [default=50]
  --output-lslr-file TEXT      Path to output LSL file.  [required]
  --help                       Show this message and exit.
  ```

See this help documentation by passing the `--help` flag when running the application, for example: 


```shell
docker run --rm nzinsargps-verticallandmotion --help
```

## Building the container locally
You can build the container with Docker by running the following command from the repository root:
```shell
docker build -t nzinsargps-verticallandmotion .
```

## Results
If this module runs successfully, a single netCDF containing projections of local sea level change will appear in `./data/output`. 

## Support
Source code is available online at https://github.com/facts-org/nzinsargps-verticallandmotion. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/facts-org/nzinsargps-verticallandmotion/issues.
