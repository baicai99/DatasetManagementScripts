# DatasetManagementScripts

This project provides a Python launcher script that allows users to choose and run different sub-scripts.

## Project Structure

```
DatasetManagementScripts/
├── add_prefix_to_txt_files.py
├── append_comma.py
├── batch_image_compression.py
├── center_crop.py
├── classify_images_by_orientation.py
├── delete_empty_txt_and_jpg.py
├── fractional_image_extractor.py
├── move_files.py
├── PhotoOptimizer.py
├── README.md
├── README.zh.md
├── run.py
└── split_files_into_folders.py
```

- `add_prefix_to_txt_files.py`: Adds a specified prefix to the filenames of all txt files.
- `append_comma.py`: Appends a comma to the end of each line in txt files.
- `batch_image_compression.py`: Compresses images to a specified size in KB.
- `center_crop.py`: Crops the center of images.
- `classify_images_by_orientation.py`: Automatically identifies the orientation of images (1:1, portrait, or landscape) and moves them to corresponding folders.
- `delete_empty_txt_and_jpg.py`: Checks if txt files are empty and deletes the empty txt files along with their corresponding jpg images.
- `fractional_image_extractor.py`: Randomly extracts a certain percentage (e.g., 10%) of images from an existing dataset for creating validation or test sets.
- `move_files.py`: Moves files to different directories based on specified rules.
- `PhotoOptimizer.py`: Optimizes images in batches, such as removing white borders.
- `README.md`: The English version of the README file, providing basic information and usage guidelines for the scripts.
- `README.zh.md`: The Chinese version of the README file, providing basic information and usage guidelines for the scripts.
- `run.py`: The main execution script that allows running the various data management scripts.
- `split_files_into_folders.py`: Divides files into different folders according to specified rules.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/DatasetManagementScripts.git
    cd DatasetManagementScripts
    ```

2. Ensure you have a Python environment installed.

## Usage

Run the launcher script `run.py` and choose the sub-script you want to execute based on the prompts.

```bash
python run.py
```

After starting the script, follow the prompts to select an option:

```
Please choose a script to run:
1. Add prefix to txt files
2. Delete empty txt and corresponding images
3. Randomly extract 10% images for a new directory (e.g., for validation or test sets)
4. Batch remove white borders
5. Split files into folders
6. Classify images by orientation
7. Move files to parent directory
8. Append comma to txt files
9. Center crop images
10. Compress images to specified KB
0. Exit
Enter option:
```

Input the corresponding number and press Enter to run the selected sub-script.

## Example

Suppose you choose to run the `add_prefix_to_txt_files.py` script:

```
Enter option: 1
```

The system will prompt:

```
Running add_prefix_to_txt_files.py ...
```

and execute the script.

## Notes

- Ensure all sub-scripts are in the same directory as `run.py`.
- If you encounter file not found errors, check the script filenames and paths.

## Contribution

Contributions are welcome. Please submit a PR to improve this project. If you have any suggestions or find any issues, please create an Issue.

## License

This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

---

This README file provides an overview of the project, installation steps, usage instructions, examples, notes, contribution guidelines, and licensing information. Feel free to modify and refine it according to your specific needs.