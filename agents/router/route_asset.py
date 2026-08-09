from agents.processors.photo_processor import process_photo
from agents.processors.pdf_processor import process_pdf
from agents.processors.blueprint_processor import process_blueprint
from agents.processors.video_processor import process_video


def route_asset(asset_type, asset_path):

    if asset_type == "photo":
        return process_photo(asset_path)

    if asset_type == "document":
        return process_pdf(asset_path)

    if asset_type == "blueprint":
        return process_blueprint(asset_path)

    if asset_type == "video":
        return process_video(asset_path)

    return {
        "status": "unsupported"
    }