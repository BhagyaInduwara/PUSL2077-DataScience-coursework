import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Default style
sns.set_theme(style="whitegrid")


def plot_distribution(df: pd.DataFrame, column: str, bins: int = 30) -> None:
    """Plot a histogram with KDE for a numeric column."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Plot a correlation heatmap for all numeric columns."""
    corr = df.select_dtypes(include="number").corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def plot_boxplot(df: pd.DataFrame, x: str, y: str) -> None:
    """Plot a boxplot of y grouped by x."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y, ax=ax)
    ax.set_title(f"{y} by {x}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_countplot(df: pd.DataFrame, column: str) -> None:
    """Plot a count bar chart for a categorical column."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index, ax=ax)
    ax.set_title(f"Count of {column}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_scatter(df: pd.DataFrame, x: str, y: str, hue: str = None) -> None:
    """Plot a scatter plot between two numeric columns."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(f"{y} vs {x}")
    plt.tight_layout()
    plt.show()
