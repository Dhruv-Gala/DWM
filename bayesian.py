import pandas as pd

def main():
    file_path = input("Enter file path: ")
    df = pd.read_excel(file_path)
    print("Dataframe:")
    print(df)

    class_col = df.columns[-1]
    features = df.columns[:-1]

    class_counts = df[class_col].value_counts().to_dict()
    total_samples = len(df)

    input_data = {}
    print("\nUser Input:")
    for feature in features:
        value = input(f"\t{feature}: ")
        input_data[feature] = value

    priors = {cls: count / total_samples for cls, count in class_counts.items()}

    print("\nPrior Probabilities:")
    for cls, prob in priors.items():
        print(f"\tP({class_col} = {cls}) = {prob:.3f}")

    conditional_prob = {}
    for feature in input_data.keys():
        conditional_prob[feature] = {}
        for cls in df[class_col].unique():
            subset = df[df[class_col] == cls]
            feature_counts = {}
            for val in subset[feature].unique():
                if val == input_data[feature]:
                    feature_counts[val] = subset[subset[feature] == val].shape[0]
            total_counts = len(subset)
            conditional_prob[feature][cls] = {val: count / total_counts for val, count in feature_counts.items()}

    print("\nConditional Probabilities:")
    for feature, probs in conditional_prob.items():
        print(f"\tP({feature} = {input_data[feature]} | {class_col})")
        for cls, values in probs.items():
            for val, prob in values.items():
                print(f"\t\tP({feature} = {val} | {class_col} = {cls}) = {prob:.3f}")

    print("\nPosterior Probabilities:")
    max = 0
    max_cls = None

    for cls in df[class_col].unique():
        posterior = priors[cls]
        for feature in features:
            if input_data[feature] in conditional_prob[feature][cls]:
                posterior *= conditional_prob[feature][cls][input_data[feature]]
        print(f"\tP({class_col} = {cls} | {input_data}) = {posterior:.3f}")
        if posterior > max:
            max = posterior
            max_cls = cls

    print(f"The most likely class is {class_col} = {max_cls} for the given {input_data} with probability of {max:.3f}")
            

if __name__ == "__main__":
    main()
