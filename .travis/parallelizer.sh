#!/bin/bash

MOLECULE_CONF="../molecule.yml"
OS="$1"

if [ "$OS" == "" ]; then
	exit 1
fi
DISTRO="$(echo ${OS} | awk -F ':' '{print $1}')"
VERSION="$(echo ${OS} | awk -F ':' '{print $2}')"

docker pull "paulfantom/$DISTRO-molecule:$VERSION"

mv "${MOLECULE_CONF}" "${MOLECULE_CONF}.tmp"
sed -n '/  containers:/q;p' "${MOLECULE_CONF}.tmp" > "${MOLECULE_CONF}"

cat <<EOF >> "${MOLECULE_CONF}"
  containers:
    - name: $DISTRO
      image: paulfantom/$DISTRO-molecule
      image_version: $VERSION
      privileged: true
      volume_mounts:
        - /sys/fs/cgroup:/sys/fs/cgroup:ro
EOF
