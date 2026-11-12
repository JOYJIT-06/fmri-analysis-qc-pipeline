import pandas as pd

def save_metadata_csv(metadata_dict, out_path):
    # Saves dictionary parameters cleanly into a CSV layout.
    df = pd.DataFrame([metadata_dict])
    df.to_csv(out_path, index=False)