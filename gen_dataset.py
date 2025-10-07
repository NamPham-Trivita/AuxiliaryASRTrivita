import pandas as pd
import os


df = pd.read_parquet("all_vivoice_600_new.parquet")
def gen_train_test(df, train_ratio=0.8):
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle the DataFrame
    train_size = int(len(df) * train_ratio)
    train_df = df[:train_size]
    test_df = df[train_size:]

    with open('Data/train.txt', 'w', encoding="utf-8") as f:
        for _, row in train_df.iterrows():
            f.write(f"{row['path']}|{row['new_text']}|{row['speaker']}\n")
    with open('Data/test.txt', 'w', encoding="utf-8") as f:
        for _, row in test_df.iterrows():
            f.write(f"{row['path']}|{row['new_text']}|{row['speaker']}\n")
    print(f"Train set size: {len(train_df)}")

if __name__ == "__main__":
    gen_train_test(df)
    print("Train and test sets generated successfully.")