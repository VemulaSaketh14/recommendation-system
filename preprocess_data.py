import pandas as pd
import numpy as np

def clean_data(path):

    # ---------------------------
    # Load dataset
    # ---------------------------
    df = pd.read_csv(path)

    # ---------------------------
    # Remove duplicates
    # ---------------------------
    df.drop_duplicates(inplace=True)

    # ---------------------------
    # Replace empty strings → NaN
    # ---------------------------
    df.replace("", np.nan, inplace=True)

    # ---------------------------
    # Convert ID columns to numeric
    # ---------------------------
    df["User's ID"] = pd.to_numeric(df["User's ID"], errors="coerce")
    df["ProdID"] = pd.to_numeric(df["ProdID"], errors="coerce")

    # ---------------------------
    # Remove rows where IDs missing
    # ---------------------------
    df = df[df["User's ID"].notna()]
    df = df[df["ProdID"].notna()]

    # ---------------------------
    # Remove invalid IDs
    # ---------------------------
    df = df[(df["User's ID"] > 0) & (df["ProdID"] > 0)]

    # ---------------------------
    # Convert IDs to integers
    # ---------------------------
    df["User's ID"] = df["User's ID"].astype(int)
    df["ProdID"] = df["ProdID"].astype(int)

    # ---------------------------
    # Fill text columns
    # ---------------------------
    text_cols = df.select_dtypes(include="object").columns
    df[text_cols] = df[text_cols].fillna("")

    # ---------------------------
    # Clean image URLs
    # ---------------------------
    if "ImageURL" in df.columns:
        df["ImageURL"] = df["ImageURL"].str.replace("|", "", regex=False)

    # ---------------------------
    # Reset index
    # ---------------------------
    df.reset_index(drop=True, inplace=True)

    return df
