import thresholdmonitor
import train
import processing
import optimize


def test_train_dataset(input_temp, input_velocity):
    train.create_dataset()
    train.train_model()
    print("Training complete, prediction: ", train.predict_model(input_temp, input_velocity))

def test_processing(input_temp, input_velocity):
    results = processing.process_data(input_temp, input_velocity)
    print("Processing complete: ", results)
    return results

def test_optimize(input_temp, input_velocity):
    results = optimize.minArgs(input_temp, input_velocity)
    print("Optimizing complete: ", results)
    return results

def test_processing_optimize(input_temp, input_velocity):
    input_temp, input_velocity, finalT = processing.process_data(input_temp, input_velocity)
    results = optimize.minArgs(input_temp, input_velocity)
    print("Processing and Optimizing complete: ", results)
    return results


def test_processing_optimize_threshold_monitor(input_temp, input_velocity):
    input_temp, input_velocity, finalT = processing.process_data(input_temp, input_velocity)
    results = thresholdmonitor.check_threshold(input_temp, input_velocity)
    print("Processing and Optimizing and Threshold monitor complete: ", results)
    return results

if __name__ == '__main__':
    test_train_dataset(1, 1)