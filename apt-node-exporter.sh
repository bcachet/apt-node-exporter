#!/usr/bin/env bash
set -e

PACKAGES=${@:1}

echo "# HELP apt_package_info Metric labeled with name/version of APT package. Value is always '1'"
echo "# TYPE apt_package_info gauge"
if [ ! -z "$PACKAGES" ]; then
    dpkg-query --showformat='apt_package_info{name=\"${Package}\",version=\"${Version}\",state=\"${db:Status-Abbrev}\"} 1.0\n' --show $PACKAGES
fi
