# Prometheus node-exporter for APT packages

Generates Prometheus metrics to a textfile (compatible with node-exporter textfile collector) about APT packages

It generate a metric called `apt_package_info` per APT packages that are configured to be monitored (via `--list` param).
Metric contains name and version of the package as labels.
Metrics are reported to stdout or textfile specified by `--output` param.

## Usage


```shell
$ python apt-node-exporter.py --output - --packages zstd libqmi-glib5
# HELP apt_package_info Metric labeled with name/version of APT package. Value is always '1'
# TYPE apt_package_info gauge
apt_package_info{name="zstd",version="1.4.8+dfsg-3build1"} 1.0
apt_package_info{name="libqmi-glib5",version="1.32.0-1ubuntu0.22.04.1"} 1.0
```

## Installation

This Python script requires `python3-apt` Debian package to be installed.
Once installed you can create a virtualenv that will have access to this system package via

```shell
virtualenv --system-site-packages venv
```

Then you can activate your virtualenv and install missing packages with `pip`

```shell
. ./venv/bin/activate
pip install -r requirements.txt
```