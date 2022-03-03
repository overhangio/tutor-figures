from glob import glob
import os
import pkg_resources

from .__about__ import __version__


templates = pkg_resources.resource_filename("tutorfigures", "templates")

config = {
    "defaults": {
        "VERSION": __version__,
        "DEVSITE_DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}overhangio/openedx-figures:{{ FIGURES_VERSION }}",
        "RELEASE_VERSION": "bbrsofiane/maple-upgrade",
    }
}

hooks = {
    "build-image": {"figures": "{{ FIGURES_DEVSITE_DOCKER_IMAGE }}"},
    "remote-image": {"figures": "{{ FIGURES_DEVSITE_DOCKER_IMAGE }}"},
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename("tutorfigures", "patches")
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
