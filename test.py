from imageai.Prediction.Custom import CustomImagePrediction
import os
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to image file.")
    args = parser.parse_args()

    print(f"ARGUMENTS\n{args}")

    if args.filename:
        execution_path = os.getcwd()

        prediction = CustomImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath("../files/idenprof_061-0.7933.h5")
        prediction.setJsonPath("idenprof_model_class.json")
        prediction.loadModel(num_objects=10)

        predictions, probabilities = prediction.predictImage(args.filename, result_count=3)

        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction, " : ", eachProbability)
    else:
        raise Exception("Please provide an image file to check")
