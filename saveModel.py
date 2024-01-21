from gpModel import GpModel
import cloudpickle

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expr = "((((x1+x9)+41.432000)/ ((x10/ (x2+1e-6) )+1e-6) )+(x8+x8))"
    count = 0
    classifier = GpModel(expression=expr, accuracy=911789, complexity=15)
    with open(f"bikes_gp_{count}.pkl", "wb") as f:
        cloudpickle.dump(classifier, f)
