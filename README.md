# Prometheus node-exporter for APT packages

Generates Prometheus metrics to a textfile (compatible with node-exporter textfile collector) about APT packages

It generate a metric called `apt_package_info` per APT packages to be monitored.
Metric contains name and version of the package as labels.

## Usage


```shell
$ python apt-node-exporter.py --output - --packages zstd libqmi-glib5
# HELP apt_package_info Metric labeled with name/version of APT package. Value is always '1'
# TYPE apt_package_info gauge
apt_package_info{name="zstd",version="1.4.8+dfsg-3build1"} 1.0
apt_package_info{name="libqmi-glib5",version="1.32.0-1ubuntu0.22.04.1"} 1.0
```