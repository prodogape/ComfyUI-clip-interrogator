from .node_mappings import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# Reference to: https://github.com/pharmapsychotic/clip-interrogator-ext/blob/main/install.py

# Install clip_interrogator
CI_VERSION = "0.6.0"
needs_install = False
try:
    import clip_interrogator
    if clip_interrogator.__version__ != CI_VERSION:
        needs_install = True
except ImportError:
    needs_install = True

if needs_install:
    import os
    import sys
    os.system(f"{sys.executable} -m pip install clip-interrogator=={CI_VERSION}")


# Create model_config.yaml to make model paths explicit;
# To change remote url, please check: path/to/site-packages/open_clip/pretrained.py
import yaml
import open_clip
model_config = {
    "cache_dir": os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "models", "clip")
}
model_names = {}
open_clip_pretrained_model_list = open_clip.list_pretrained()
for open_clip_pretrained_model in open_clip_pretrained_model_list:
    clip_model_name, clip_pretrained_name = open_clip_pretrained_model
    model_names[f"{clip_model_name}/{clip_pretrained_name}"] = {
        "clip_model_name": clip_model_name,
        "clip_pretrained_name": clip_pretrained_name,
    }
model_config["model_names"] = model_names

yaml.dump(model_config, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_config.yaml"), 'w'), indent=4)
