import base64
import os


def detect_asset_type(image_path):

    extension = os.path.splitext(
        image_path
    )[1].lower()

    if extension in [".jpg", ".jpeg", ".png", ".webp"]:

        return {
            "asset_type": "photo",
            "confidence": 60
        }

    if extension == ".pdf":

        return {
            "asset_type": "document",
            "confidence": 90
        }

    return {
        "asset_type": "unknown",
        "confidence": 10
    }


def analyze_image(image_path):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    image_base64 = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    asset_type = detect_asset_type(
        image_path
    )

    return {
        "asset_type": asset_type["asset_type"],
        "asset_type_confidence":
            asset_type["confidence"],

        "description":
            "Asset classified successfully.",

        "tags":
            "classified,pending-ai",

        "confidence":
            25
    }