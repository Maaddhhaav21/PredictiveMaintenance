from src.pipeline.training_pipeline import run_training


def test_pipeline():

    model = run_training()

    assert model is not None