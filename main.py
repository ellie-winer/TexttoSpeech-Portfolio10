import PyPDF2
import boto3

polly = boto3.client('polly')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def text_to_speech_aws_polly(text, output_audio_path):
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    with open(output_audio_path, 'wb') as file:
        file.write(response['AudioStream'].read())
    print(f"Audio saved as {output_audio_path}")

def pdf_to_audiobook(pdf_path, output_audio_path):
    text = extract_text_from_pdf(pdf_path)

    if text:
        text_to_speech_aws_polly(text, output_audio_path)
    else:
        print("No text found in the PDF!")

pdf_file = 'portfolio10-testpdf.pdf'
output_audio = 'output_audio.mp3'
pdf_to_audiobook(pdf_file, output_audio)

