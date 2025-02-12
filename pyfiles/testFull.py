import thresholdmonitor
import train
import processing
import optimize


def test_train_createdataset():
    train.create_dataset()
    train.train_model()

def test_processing():
    processing.processing()
