from .inference import CI_Inference

class ComfyUIClipInterrogator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mode": (CI_Inference().mode_list, ),
                "model_name": (CI_Inference().model_list, ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "apply"

    # OUTPUT_NODE = False

    CATEGORY = "image"

    def apply(self, image, mode, model_name):
        CI_Inference().image_to_prompt(image, mode, model_name)
