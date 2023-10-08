# In this step, you'll process the first 3 pages of the novel using the online processing (synchronous) API. This method is best suited for smaller documents that are stored locally. Check out the full processor list for the maximum pages and file size for each processor type.

# Use the Cloud Shell Editor or a text editor on your local machine to create a file called online_processing.py and use the code below.

# Replace YOUR_PROJECT_ID, YOUR_PROJECT_LOCATION, YOUR_PROCESSOR_ID, and the FILE_PATH with appropriate values for your environment.

from google.api_core.client_options import ClientOptions
from google.cloud import documentai

PROJECT_ID = "contract-bot-397822"
LOCATION = "eu"  # Format is 'us' or 'eu'
PROCESSOR_ID = "e557839fc2c11c48"  # that is the test OCR processor ID

# The local file in your current working directory
FILE_PATH = "https://storage.cloud.google.com/contractbotbucket1/Winnie_the_Pooh_3_Pages.pdf"
# Refer to https://cloud.google.com/document-ai/docs/file-types
# for supported file types
MIME_TYPE = "application/pdf"

# Instantiates a client
docai_client = documentai.DocumentProcessorServiceClient(
    client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
)

# The full resource name of the processor, e.g.:
# projects/project-id/locations/location/processor/processor-id
# You must create new processors in the Cloud Console first
RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

# Read the file into memory
with open(FILE_PATH, "rb") as image:
    image_content = image.read()

# Load Binary Data into Document AI RawDocument Object
raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

# Configure the process request
request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

# Use the Document AI client to process the sample form
result = docai_client.process_document(request=request)

document_object = result.document
print("Document processing complete.")
print(f"Text: {document_object.text}")
