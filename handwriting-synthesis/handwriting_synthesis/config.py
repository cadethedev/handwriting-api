import os

# Get the directory where this module is located
_module_dir = os.path.dirname(os.path.abspath(__file__))
# Model is in the parent directory of handwriting_synthesis
_package_root = os.path.dirname(_module_dir)

BASE_PATH = os.path.join(_package_root, "model")
BASE_DATA_PATH = "data"

data_path: str = os.path.join(BASE_PATH, BASE_DATA_PATH)
processed_data_path: str = os.path.join(data_path, "processed")
raw_data_path: str = os.path.join(data_path, "raw")
ascii_data_path: str = os.path.join(raw_data_path, "ascii")

checkpoint_path: str = os.path.join(BASE_PATH, "checkpoint")
prediction_path: str = os.path.join(BASE_PATH, "prediction")
style_path: str = os.path.join(BASE_PATH, "style")
