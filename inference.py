# Reference to: https://github.com/pharmapsychotic/clip-interrogator-ext/blob/main/scripts/clip_interrogator_ext.py
import os
import yaml
import torch
from PIL import Image
from clip_interrogator import Config, Interrogator


class CI_Inference:
    ci_model: Interrogator = None
    model_name: str
    mode_list = ["best", "classic", "fast", "negative"]
    cache_dir: str
    model_names: dict
    model_list: list

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"model_config.yaml")) as fp:
            model_config = yaml.load(fp, Loader=yaml.FullLoader)
        self.cache_dir = model_config["cache_dir"]
        self.model_names = model_config["model_names"]
        self.model_list = list(self.model_names.keys())

    def _load_model(self, model_name):
        if not (self.ci_model and model_name == self.ci_model.config.clip_model_name):
            config = Config(
                # device="cuda",
                clip_model_path=self.cache_dir,
                clip_model_name=model_name,
            )
            self.ci_model = Interrogator(config)

    def _interrogate(self, image, mode, caption=None):
        if mode == 'best':
            prompt = self.ci_model.interrogate(image, caption=caption)
        elif mode == 'classic':
            prompt = self.ci_model.interrogate_classic(image, caption=caption)
        elif mode == 'fast':
            prompt = self.ci_model.interrogate_fast(image, caption=caption)
        elif mode == 'negative':
            prompt = self.ci_model.interrogate_negative(image)
        else:
            raise Exception(f"Unknown mode {mode}")
        return prompt

    def image_to_prompt(self, image, mode, model_name):
        try:
            self._load_model(model_name)
            # image.convert('RGB')
            pil_image = Image.fromarray(image.squeeze(0).numpy())  # TODO
            prompt = self._interrogate(pil_image, mode)
        except Exception as e:
            prompt = ""
            print(e)

        return prompt


if __name__ == '__main__':
    print(CI_Inference().model_list)
