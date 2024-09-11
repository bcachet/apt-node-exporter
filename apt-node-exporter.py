import argparse
import apt  # require installation of `python3-apt` package on the system
import logging
import sys
from prometheus_client import CollectorRegistry, Gauge, generate_latest

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_packages_details(pkg_names):
    cache = apt.Cache()
    return [
        {"name": pkg.name, "version": pkg.installed.version}
        for pkg in [cache[name] for name in pkg_names if name in cache]
        if pkg.is_installed
    ]


def register_gauge(gauge, pkg):
    logging.debug("Registering Gauge for package %s", pkg.get("name"))
    gauge.labels(**pkg).set(1)


def main():

    parser = argparse.ArgumentParser(
        prog="apt-node-exporter",
        description="Export metrics about APT packages as node-exporter textfile",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="filename",
        help="Write metrics to FILE",
        metavar="FILE",
        type=argparse.FileType("w"),
        default='-',
    )
    parser.add_argument(
        "-p",
        "--packages",
        dest="packages",
        help="PACKAGES to report metrics for",
        metavar="PACKAGES",
        type=str,
        nargs="+",
        required=True,
    )
    args = parser.parse_args()

    registry = CollectorRegistry()
    gauge = Gauge(
        "apt_package_info",
        "Metric labeled with name/version of APT package. Value is always '1'",
        labelnames=["name", "version"],
        registry=registry,
    )

    for pkg in get_packages_details(args.packages):
        register_gauge(gauge, pkg)

    logging.debug("Exporting metrics to textfile %s", args.filename.name)
    args.filename.write(generate_latest(registry).decode('utf-8'))


if __name__ == "__main__":
    main()
