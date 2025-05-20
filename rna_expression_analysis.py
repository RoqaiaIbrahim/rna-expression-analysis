# RNA Expression Analysis Script (Beginner Level)

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the expression data
data = pd.read_csv("rna_expression_data.csv")  # make sure to have a CSV file

print("First few rows of the data:")
print(data.head())

# Step 2: Check for missing values
print("\nMissing values per column:")
print(data.isnull().sum())

# Step 3: Basic statistics
print("\nBasic statistics of expression levels:")
print(data.describe())

# Step 4: Visualize expression of a gene (e.g., 'GeneA')
gene_name = "GeneA"
if gene_name in data.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(data[gene_name].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Expression Distribution of {gene_name}")
    plt.xlabel("Expression Level")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("gene_expression_plot.png")
    plt.show()
else:
    print(f"\n{gene_name} not found in the dataset.")

# Step 5: Filter genes with high average expression
mean_expression = data.mean()
high_expression_genes = mean_expression[mean_expression > 10].index.tolist()

print("\nGenes with average expression > 10:")
print(high_expression_genes)
