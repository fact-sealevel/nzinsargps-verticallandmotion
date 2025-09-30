from nzinsargps_verticallandmotion.NZInsarGPS_verticallandmotion_preprocess import (
    NZInsarGPS_preprocess_verticallandmotion,
)
from nzinsargps_verticallandmotion.NZInsarGPS_verticallandmotion_postprocess import (
    NZInsarGPS_postprocess_verticallandmotion,
)
import click

# input args to add
# input type (in preprocess)
# locationfile
# chunksize


@click.command()
@click.option(
    "--pipeline-id",
    required=True,
    type=str,
    help="Unique identifier for this instance of the module. Used to name output files",
    envvar="NZINSARGPS_VLM_PIPELINE_ID",
)
@click.option(
    "--min-qf",
    help="Minimum value of data quality to use (default = 5)",
    default=5,
    envvar="NZINSARGPS_VLM_MIN_QF",
)
@click.option(
    "--use_boprates",
    type=int,
    default=1,
    help="Use the BOP corrected rates instead of the raw VLM rates (default = 1)",
    envvar="NZINSARGPS_VLM_USE_BOPRATES",
)
@click.option(
    "--input-fname",
    type=str,
    default="data/input/NZ_2km.txt",
    envvar="NZINSARGPS_VLM_INPUT_FNAME",
    help="input file name (??)",
)
@click.option(
    "--pyear-start",
    envvar="NZINSARGPS_VLM_PYEAR_START",
    help="Projection year start [default=2020]",
    default=2020,
    type=click.IntRange(min=2020),
)
@click.option(
    "--pyear-end",
    envvar="NZINSARGPS_VLM_PYEAR_END",
    help="Projection year end [default=2100]",
    default=2100,
    type=click.IntRange(max=2300),
)
@click.option(
    "--pyear-step",
    envvar="NZINSARGPS_VLM_PYEAR_STEP",
    help="Projection year step [default=10]",
    default=10,
    type=click.IntRange(min=1),
)
@click.option(
    "--baseyear",
    envvar="NZINSARGPS_VLM_BASEYEAR",
    help="Year to which projections are referenced [default = 2000]",
    default=2000,
)
@click.option(
    "--nsamps",
    envvar="NZINSARGPS_VLM_NSAMPS",
    help="Number of samples to draw [default=500]",
    default=500,
)
@click.option(
    "--rngseed",
    envvar="NZINSARGPS_VLM_RNGSEED",
    help="Seed for the random number generator [default=1234]",
    default=5678,
)
@click.option(
    "--location-file",
    envvar="NZINSARGPS_VLM_LOCATION_FILE",
    help="Path to location file for postprocessing",
    default="location.lst",
)
@click.option(
    "--chunksize",
    type=int,
    envvar="NZINSARGPS_VLM_CHUNKSIZE",
    help="Chunk size for postprocessing [default=50]",
    default=50,
)
@click.option(
    "--output-path",
    type=str,
    envvar="NZINSARGPS_VLM_OUTPUT_PATH",
    help="Path to output directory",
    default="output",
)
def main(
    pipeline_id,
    min_qf,
    use_boprates,
    input_fname,
    pyear_start,
    pyear_end,
    pyear_step,
    baseyear,
    nsamps,
    rngseed,
    location_file,
    chunksize,
    output_path,
):
    """Run the NZInsarGPS verticallandmotion module"""
    click.echo("Hello from nzinsargps-verticallandmotion!")

    # Run the preprocessing stage
    preprocess_dict = NZInsarGPS_preprocess_verticallandmotion(
        inputfile=input_fname, min_quality_flag=min_qf, use_boprates=use_boprates
    )

    NZInsarGPS_postprocess_verticallandmotion(
        preprocess_dict=preprocess_dict,
        nsamps=nsamps,
        rng_seed=rngseed,
        locationfilename=location_file,
        baseyear=baseyear,
        pyear_start=pyear_start,
        pyear_end=pyear_end,
        pyear_step=pyear_step,
        chunksize=chunksize,
        pipeline_id=pipeline_id,
        output_path=output_path,
    )


if __name__ == "__main__":
    main()
