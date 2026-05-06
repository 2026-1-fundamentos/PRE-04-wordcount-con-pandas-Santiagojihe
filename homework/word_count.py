"""Taller evaluable"""

import glob
import os
import pandas as pd


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job(input_directory, output_directory):
    """Job"""

    input_pattern = os.path.join(input_directory, "*")
    file_paths = sorted(glob.glob(input_pattern))

    words = []
    for path in file_paths:
        with open(path, "r", encoding="utf-8") as input_file:
            text = input_file.read().lower()
            cleaned = pd.Series([text]).str.replace(r"[^a-z0-9\s]", " ", regex=True).iloc[0]
            words.extend(cleaned.split())

    dataframe = pd.DataFrame({"word": words})
    dataframe = dataframe[dataframe["word"] != ""]
    counts = dataframe["word"].value_counts().sort_index()

    os.makedirs(output_directory, exist_ok=True)

    output_path = os.path.join(output_directory, "part-00000")
    counts.to_csv(output_path, sep="\t", header=False)

    success_path = os.path.join(output_directory, "_SUCCESS")
    with open(success_path, "w", encoding="utf-8") as success_file:
        success_file.write("")


if __name__ == "__main__":

    run_job(
        "files/input/",
        "files/output/",
    )
