# DatasetManagementScripts

This project provides a Python launcher script that allows users to choose and run different sub-scripts.

## Project Structure

```
DatasetManagementScripts/
│
├── add_prefix_to_txt_files.py
├── delete_empty_txt_and_jpg.py
├── extract_and_cleanup_images.py
├── PhotoOptimizer.py
└── run.py
```

- `add_prefix_to_txt_files.py`: Adds trigger words to txt files, remember to add commas.
- `delete_empty_txt_and_jpg.py`: Deletes txt files and their corresponding images if the txt file is empty.
- `extract_and_cleanup_images.py`: Randomly extracts 10% of images to a new directory for normalization or validation.
- `PhotoOptimizer.py`: Batch removes white edges from images.
- `run.py`: The launcher script that allows you to select and run the above sub-scripts.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/DatasetManagementScripts.git
    cd DatasetManagementScripts
    ```

2. Ensure you have a Python environment installed.

## Usage

Run the launcher script `run.py` and follow the prompts to select the sub-script you want to execute.

```bash
python run.py
```

After launching the script, enter the option based on the prompt:

```
Please select a script to run:
1. Add trigger words to txt files, remember to add commas.
2. Delete txt files and their corresponding images if the txt file is empty.
3. Randomly extract 10% of images to a new directory for normalization or validation.
4. Batch remove white edges
0. Exit
Enter your choice:
```

Enter the corresponding number and press Enter to run the selected sub-script.

## Example

If you choose to run the `add_prefix_to_txt_files.py` script:

```
Enter your choice: 1
```

The system will display:

```
Running add_prefix_to_txt_files.py...
```

And the script will be executed.

## Notes

- Ensure all sub-scripts are placed in the same directory as `run.py`.
- If a file not found error occurs, please check the script filenames and paths.

## Contributing

Feel free to submit PRs to improve this project. If you have any suggestions or find any issues, please create an Issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

This README provides an overview of the project, installation steps, usage instructions, examples, notes, contributing guidelines, and license information. You can further modify and refine it based on your specific requirements.