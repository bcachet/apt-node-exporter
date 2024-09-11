# Prometheus node-exporter for APT packages

Generates Prometheus metrics to a textfile (compatible with node-exporter textfile collector) about APT packages

It generate a metric called `apt_package_info` per APT packages to be monitored.
Metric contains name and version of the package as labels.