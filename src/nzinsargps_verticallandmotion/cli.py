from nzinsargps_verticallandmotion.NZInsarGPS_verticallandmotion_preprocess import (
    NZInsarGPS_preprocess_verticallandmotion,
)
from nzinsargps_verticallandmotion.NZInsarGPS_verticallandmotion_postprocess import (
    NZInsarGPS_postprocess_verticallandmotion,
)
import click

@click.command()
@click.option(
    "--min-qf",
    help="Minimum value of data quality to use (default = 5)",
    default=5,
    envvar="NZINSARGPS_VLM_MIN_QF",
)
@click.option(
    "--use-boprates",
    type=int,
    default=1,
    help="Use the BOP corrected rates instead of the raw VLM rates (default = 1)",
    envvar="NZINSARGPS_VLM_USE_BOPRATES",
)
@click.option(
    "--input-fname",
    type=str,
    required=True,
    envvar="NZINSARGPS_VLM_INPUT_FNAME",
    help="Input .txt file",
)
@click.option(
    "--pyear-start",
    envvar="NZINSARGPS_VLM_PYEAR_START",
    help="Projection year start [default=2020]",
    default=2020,
    type=click.IntRange(min=2000),
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
    type=click.IntRange(min=2000, max=2300),
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
    required=True,
    type=str,
)
@click.option(
    "--chunksize",
    type=int,
    envvar="NZINSARGPS_VLM_CHUNKSIZE",
    help="Chunk size for postprocessing [default=50]",
    default=50,
)
@click.option(
    "--output-lslr-file",
    type=str,
    envvar="NZINSARGPS_VLM_OUTPUT_LSLR_FILE",
    help="Path to output LSL file.",
    required=True,
)
def main(
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
    output_file,
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
        output_file=output_file,
    )


if __name__ == "__main__":
    main()
