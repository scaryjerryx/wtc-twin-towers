WTC EVIDENCE ENGINE
ARCHITECTURE

========================================
DISCOVERY LAYER
========================================

agents/discovery/

discover.py
    Create discovery jobs from targets.

build_searches.py
    Generate source search URLs.

build_real_searches.py
    Generate real source-specific searches.

promote_searches.py
    Promote candidates to discoveries.

queue_discoveries.py
    Push discoveries into discovery_queue.

export_discoveries.py
    Reporting and diagnostics.


========================================
INGESTION LAYER
========================================

agents/downloader/

main.py
    Download discovered assets.

Responsibilities:

- Download files
- Store in R2
- Create asset records
- Create metadata jobs


========================================
CLASSIFICATION LAYER
========================================

agents/classification/

asset_classifier.py

Responsibilities:

- Determine asset type
- Assign confidence score

Supported Types:

- photo
- blueprint
- floorplan
- pdf
- report
- document
- video
- audio
- newspaper
- map


========================================
ROUTING LAYER
========================================

agents/router/

route_asset.py

Responsibilities:

Route assets to correct processor.

photo
  -> photo_processor

pdf
  -> pdf_processor

blueprint
  -> blueprint_processor

video
  -> video_processor


========================================
PROCESSING LAYER
========================================

agents/processors/

photo_processor.py

Responsibilities:

- Visual analysis
- Location detection
- Object detection
- Tag extraction

----------------------------------------

pdf_processor.py

Responsibilities:

- PDF handling
- OCR triggering
- Text extraction

----------------------------------------

pdf_text_extractor.py

Responsibilities:

- Extract PDF text
- Prepare chunks

----------------------------------------

blueprint_processor.py

Responsibilities:

- Floor detection
- Tower detection
- Drawing type detection
- Structural feature extraction

----------------------------------------

video_processor.py

Responsibilities:

- Extract keyframes
- Generate video metadata
- Timeline segmentation


========================================
METADATA LAYER
========================================

agents/metadata/

vision_analyze.py

Responsibilities:

- Process metadata queue
- Download asset from R2
- Send to analysis layer

----------------------------------------

vision_client.py

Responsibilities:

- Abstract AI providers
- Return descriptions
- Return tags
- Return confidence

----------------------------------------

r2_download.py

Responsibilities:

- Download assets from R2


========================================
KNOWLEDGE LAYER
========================================

agents/knowledge/

knowledge_extractor.py

Responsibilities:

- Extract entities
- Extract facts
- Extract years
- Extract relationships

----------------------------------------

entity_loader.py

Responsibilities:

- Store entities

----------------------------------------

fact_loader.py

Responsibilities:

- Store facts

----------------------------------------

knowledge_pipeline.py

Responsibilities:

Convert analysis into:

Entities
Facts
Citations


========================================
VERIFICATION LAYER
========================================

agents/verification/

fact_verifier.py

Responsibilities:

- Compare evidence
- Count citations
- Calculate confidence
- Mark verified facts

Rules:

1 source = claim
2 sources = likely
3+ sources = verified


========================================
SEARCH LAYER
========================================

agents/search