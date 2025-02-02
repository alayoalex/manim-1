import click
from cloup import option, option_group


global_options = option_group(
    "Global options",
    option(
        "-c",
        "--config_file",
        help="Specify the configuration file to use for render settings.",
    ),
    option(
        "--custom_folders",
        is_flag=True,
        help="Use the folders defined in the [custom_folders] section of the "
        "config file to define the output folder structure.",
    ),
    option(
        "--disable_caching",
        is_flag=True,
        help="Disable the use of the cache (still generates cache files).",
    ),
    option("--flush_cache", is_flag=True, help="Remove cached partial movie files."),
    option("--tex_template", help="Specify a custom TeX template file."),
    option(
        "-v",
        "--verbosity",
        type=click.Choice(
            ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
            case_sensitive=False,
        ),
        help="Verbosity of CLI output. Changes ffmpeg log level unless 5+.",
    ),
)
