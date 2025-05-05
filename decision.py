import pandas as pd
import math

def entropy(column):
    values = column.unique()
    total = len(column)
    ent = 0
    for val in values:
        count = column[column == val].count()
        p = count / total
        ent -= p * math.log2(p)
    return ent

def info_gain(df, feature, target, total_entropy):
    print(f"\nCalculating information gain for feature: {feature}")
    values = df[feature].unique()
    weighted_entropy = 0

    for val in values:
        subset = df[df[feature] == val]
        prob = len(subset) / len(df)
        print(f"\t\tValue: {val} -> {entropy(subset[target]):.3f}")
        weighted_entropy += prob * round(entropy(subset[target]), 3)
    print(f"\n\tWeighted entropy: {weighted_entropy:.3f}")
    
    gain = total_entropy - weighted_entropy
    print(f"\tInformation gain: {gain:.3f}")
    return gain

def build_tree(df, target, features):
    # Base case 1: all target values are the same
    if len(df[target].unique()) == 1:
        unique_target = df[target].iloc[0]

        feature_values = ", ".join(f"{col} = {df[col].iloc[0]}" for col in df.columns if col != target and col not in features)
        print(f"Since for ({feature_values}), the class '{target}' is always '{unique_target}',")
        print(f"we can assign the class '{unique_target}' here.")

        return unique_target

    if len(features) == 0:
        return df[target].mode()[0]
    
    print(f"Building tree with features: {features}")
    total_entropy = entropy(df[target])
    print(f"Total entropy: {total_entropy:.3f}")

    # Find best feature using info gain
    gains = {feature: info_gain(df, feature, target, total_entropy) for feature in features}
    best_feature = max(gains, key=gains.get)


    print(f"\nBest feature: {best_feature} with gain: {gains[best_feature]:.3f}")

    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]

    for val in df[best_feature].unique():
        print(f"\nProcessing {best_feature}: {val}")
        subtree = build_tree(df[df[best_feature] == val], target, remaining_features)
        tree[best_feature][val] = subtree

    return tree

def print_pretty_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→ " + str(tree))
        return
    
    for feature, branches in tree.items():
        for value, subtree in branches.items():
            print(f"{indent}[{feature} = {value}]")
            print_pretty_tree(subtree, indent + "    ")

# Main
def main():
    file_path = input("Enter Excel file path: ")
    df = pd.read_excel(file_path)

    target = df.columns[-1]
    features = list(df.columns[:-1])

    tree = build_tree(df, target, features)

    print("\nDecision Tree:")
    print(tree)

    print_pretty_tree(tree)

if __name__ == "__main__":
    main()