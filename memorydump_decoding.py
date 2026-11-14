import base64
import zlib
import sys

RESULT_FILENAME = "Payload_Readable.txt"


def extract_text(encoded_data):
    """Convert an encoded and compressed payload into readable text."""
    binary_data = base64.b64decode(encoded_data)
    uncompressed_data = zlib.decompress(binary_data)

    readable_text = uncompressed_data.decode("utf-8", errors="ignore")
    readable_text = readable_text.replace("\x00", "")

    return readable_text


def write_result(content):
    """Store the extracted content in a text file."""
    with open(RESULT_FILENAME, "w", encoding="utf-8") as result_file:
        result_file.write(content)


def run(arguments):
    """Process a payload supplied as an argument or entered manually."""
    if len(arguments) > 1:
        encoded_data = arguments[1]
    else:
        try:
            encoded_data = input("Insert the compressed payload: ")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user")
            return

    extracted_content = extract_text(encoded_data)

    write_result(extracted_content)
    print(extracted_content)


if __name__ == "__main__":
    try:
        run(sys.argv)
    except Exception as failure:
        print(failure)