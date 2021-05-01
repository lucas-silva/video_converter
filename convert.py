import os
import glob
import subprocess

source_directory = input('enter the source directory containing the media files: ').rstrip('/').rstrip('\\')
source_format = input('enter the input format ex.: mpg, asf, mpeg: ').lstrip('.')
output_format = input('enter the output format ex.: avi, mp4: ').lstrip('.')

source_filepath_pattern = f'{source_directory}/**/*.{source_format}'
output_root_directory = f'{source_directory}/converted'

for filepath in glob.glob(source_filepath_pattern, recursive=True):
    output_directory = os.path.dirname(os.path.realpath(filepath)).replace(source_directory, output_root_directory)
    filename, _ = os.path.splitext(os.path.basename(filepath))
    output_filepath = f'{output_directory}/{filename}.{output_format}'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)

    command = [
        'ffmpeg',
        '-i', filepath,
        '-vcodec', 'copy',
        '-acodec', 'copy',
        '-y',
        '-v', 'quiet',
        output_filepath
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(f'converted {filepath} to {output_filepath}')
