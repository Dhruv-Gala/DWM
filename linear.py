import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = input("Enter file path: ")
    df = pd.read_excel(file_path)
    print(df)

    n = len(df)
    sum_x = df['X'].sum()
    sum_y = df['Y'].sum()

    mean_x = sum_x / n
    mean_y = sum_y / n

    sum_xy = ((df['X']-mean_x) * (df['Y']-mean_y)).sum()
    sum_x2 = ((df['X']-mean_x)**2).sum()

    beta = sum_xy / sum_x2
    alpha = mean_y - beta*mean_x

    def predict(x):
        return alpha + beta * x
    
    x = int(input("Enter value of x: "))
    y = predict(x)
    
        
    print(f"The predicted value of y is {y} for x = {x}")
    y_predict = predict(df['X'].values)

    plt.scatter(df['X'].values, df['Y'].values, color='blue', label='Actual points')
    plt.plot(df['X'].values, y_predict, color='red', label='Best Fit Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Linear Regression')
    plt.show()

if __name__ == "__main__":
    main()