# Dataset Management Toolkit

This project provides a comprehensive set of Python tools for managing and processing datasets, particularly suitable for preprocessing, organizing, and optimizing machine learning datasets.

## Project Structure

```
project_root/
├── core/
│   └── run.py                             # Main menu program
│
├── file_utils/
│   ├── create_nested_folders.py           # Create nested folders
│   ├── move_files.py                      # Move files to parent folder
│   ├── sequential_file_renamer.py         # Sequential file renaming
│   └── split_files_into_folders.py        # Split files into multiple folders
│
├── image_utils/
│   ├── classification/
│   │   ├── classify_images_by_orientation.py  # Classify images by orientation
│   │   └── fractional_image_extractor.py      # Extract random subset of images
│   │
│   ├── cropping/
│   │   ├── aspect_ratio_cropper.py        # Crop to specific aspect ratio
│   │   ├── center_crop.py                 # Center crop images
│   │   └── remove_black_borders.py        # Remove black borders from images
│   │
│   ├── optimization/
│   │   ├── batch_image_compression.py     # Compress images to specified size
│   │   └── PhotoOptimizer.py              # Batch optimize images (remove white borders)
│   │
│   └── sampling/
│       └── image_sampler.py               # Image sampler
│
├── text_utils/
│   ├── add_prefix_to_txt_files.py         # Add trigger words to txt files
│   ├── append_comma.py                    # Append characters to end of files
│   ├── delete_empty_txt_and_jpg.py        # Delete empty txt files and corresponding images
│   ├── delete_txt_files.py                # Delete all txt files
│   └── remove_string.py                   # Remove specific strings from txt files
│
├── video_utils/
│   └── video_frame_extractor.py           # Extract frames from videos
│
└── docs/
    ├── LICENSE                            # License file
    ├── README.md                          # English documentation
    └── README.zh.md                       # Chinese documentation
```

## Tool Descriptions

### Text File Processing Tools

- `add_prefix_to_txt_files.py`: Add prefixes or trigger words to txt files, supporting multiple comma-separated terms
- `append_comma.py`: Append any specified character to the end of txt file content
- `delete_empty_txt_and_jpg.py`: Check and delete empty txt files and their corresponding image files with the same name
- `delete_txt_files.py`: Batch delete all txt files in a specified directory
- `remove_string.py`: Remove specified strings or phrases from txt files

### File Management Tools

- `create_nested_folders.py`: Create nested folder hierarchies according to specified structure
- `move_files.py`: Move files from subfolders to parent folders for centralized management
- `sequential_file_renamer.py`: Rename files sequentially to maintain a uniform naming format
- `split_files_into_folders.py`: Split large quantities of files into multiple subfolders based on specified counts

### Image Processing Tools

#### Classification Tools
- `classify_images_by_orientation.py`: Automatically recognize image orientation (landscape, portrait, square) and classify into different folders
- `fractional_image_extractor.py`: Randomly extract a certain percentage (e.g., 10%) of images to a new directory for validation or test sets

#### Cropping Tools
- `center_crop.py`: Perform center cropping on images, preserving the central area
- `aspect_ratio_cropper.py`: Crop images to a specific aspect ratio
- `remove_black_borders.py`: Automatically detect and remove black borders around images

#### Optimization Tools
- `batch_image_compression.py`: Batch compress images to a specified KB size to save storage space
- `PhotoOptimizer.py`: Batch optimize images, including removing white borders and other enhancements

#### Sampling Tools
- `image_sampler.py`: Intelligent sampling from image datasets for data analysis or subset creation

### Video Processing Tools

- `video_frame_extractor.py`: Extract frames from video files at specified intervals to generate image sequences

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/dataset-management-tools.git
    cd dataset-management-tools
    ```

2. Ensure you have Python environment and required dependencies installed:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main menu program and select the tool you want to execute through the interactive interface:

```bash
python core/run.py
```

The program will display a categorized menu. Follow the prompts to select the appropriate tool:

```
===== Image Processing Toolkit =====

Please select a script to run:

Text File Processing Tools:
1. Add trigger words to txt files (remember to add commas)
2. Delete empty txt files and their corresponding images
3. Append any character to the end
4. Remove specified strings from txt files
5. Delete txt files

File Management Tools:
6. Split folders
7. Move images to parent folder
8. Create nested folders
9. Sequential file renaming

Image Processing Tools:
10. Randomly extract 10% of images to a new directory for regularization or validation
11. Batch remove white borders
12. Classify images as landscape, portrait, or square
13. Center crop
14. Compress images to specified KB
15. Image sampler
16. Remove black borders from images
17. Aspect ratio cropping

Video Processing Tools:
18. Extract frames from video

0. Exit

Enter option: 
```

## Notes

- Before running tools, make sure you have backed up important data as some tools perform irreversible file operations
- All scripts will prompt for confirmation before execution to prevent accidental operations
- If you encounter path issues, check if the folder structure matches expectations

## Contributing

Contributions of new tools or improvements to existing tools are welcome. Please submit PRs or create Issues to discuss new features or report problems.

## License

This project is licensed under the MIT License. For more information, please refer to the LICENSE file.