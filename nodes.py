from .inference import ci

class ComfyUIClipInterrogator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mode": (ci.mode_list, ),
                "model_name": (ci.model_list, ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "apply"

    OUTPUT_NODE = False

    CATEGORY = "image"

    def apply(self, image, mode, model_name):
        prompt = ci.image_to_prompt(image, mode, model_name)
        return (prompt, )


# class ShowText:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 "prompt": ("CONDITIONING", ),
#                 "text": ("STRING", {"multiline": True})
#             },
#         }
#
#     RETURN_TYPES = ()
#     FUNCTION = "apply"
#
#     OUTPUT_NODE = True
#
#     CATEGORY = "image"
#
#     def apply(self, prompt, text):
#         for p in prompt:
#             print(p)  # debug
#
#         # return