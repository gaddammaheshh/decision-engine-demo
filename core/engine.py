from services.scoring_service import ScoringService
from pipelines.pipeline import ProcessingPipeline
from core.decision import make_decision

def run_engine(data: dict):
    signals = data.get("signals", [])

    scorer = ScoringService()
    pipeline = ProcessingPipeline(scorer, make_decision)

    return pipeline.run(signals)