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

    RETURN_TYPES = ("PROMPT",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "apply"

    OUTPUT_NODE = False

    CATEGORY = "image"

    def apply(self, image, mode, model_name):
        return CI_Inference().image_to_prompt(image, mode, model_name)


class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("PROMPT", {"multiline": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "apply"

    OUTPUT_NODE = True

    CATEGORY = "image"

    def apply(self, prompt):
        # TODO
        return