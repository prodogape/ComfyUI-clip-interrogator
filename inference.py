# Reference to: https://github.com/pharmapsychotic/clip-interrogator-ext/blob/main/scripts/clip_interrogator_ext.py
import os
import json
import torch
# from PIL import Image
from clip_interrogator import Config, Interrogator
from modules import devices


class CI_Inference:
    ci_model: Interrogator
    model_name: str
    mode_list = ["best", "classic", "fast", "negative"]
    model_url_map: dict
    model_list: list

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"model_list.json")) as fp:
            self.model_url_map = json.load(fp)
        self.model_list = list(self.model_url_map.keys())

    def _download_model(self, path):
        pass

    def _load_model(self, model_name):
        if not (self.ci_model and model_name == self.ci_model.config.clip_model_name):
            config = Config(
                device=devices.get_optimal_device(),
                cache_path='models/clip-interrogator',
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
            self.__load_model(model_name)
            prompt = self.__interrogate(image.convert('RGB'), mode)
        except Exception as e:
            prompt = ""
            print(e)

        return prompt
