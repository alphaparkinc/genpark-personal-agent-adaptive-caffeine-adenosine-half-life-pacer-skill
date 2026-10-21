# -*- coding: utf-8 -*-
"""Adaptive Caffeine Adenosine Half-Life & Sleep Latency Pacer for GenPark Personal Agent."""
import json
import math
from typing import Dict, Any, List

class AdaptiveCaffeineAdenosinePacer:
    @staticmethod
    def calculate_circulating_caffeine_at_bedtime(caffeine_intakes: List[Dict[str, Any]], bedtime_hh_mm: str, metabolizer_phenotype: str = "normal_cyp1a2") -> Dict[str, Any]:
        half_life = 4.0 if metabolizer_phenotype == "fast_cyp1a2" else (8.0 if metabolizer_phenotype == "slow_cyp1a2" else 5.5)
        bed_h, bed_m = map(int, bedtime_hh_mm.split(":"))
        bed_minutes = bed_h * 60 + bed_m
        residual_total_mg = 0.0
        for entry in caffeine_intakes:
            dose_h, dose_m = map(int, entry["time_hh_mm"].split(":"))
            elapsed_h = max(0.0, (bed_minutes - (dose_h * 60 + dose_m)) / 60.0)
            residual_total_mg += entry["mg"] * (0.5 ** (elapsed_h / half_life))
        residual_total_mg = round(residual_total_mg, 1)
        sleep_impact = "SEVERE_SWS_SUPPRESSION" if residual_total_mg > 50 else ("MILD_LATENCY_DELAY" if residual_total_mg > 25 else "MINIMAL_IMPACT_OPTIMAL")
        return {"bedtime": bedtime_hh_mm, "half_life_hours": half_life, "circulating_caffeine_bedtime_mg": residual_total_mg, "sleep_architecture_risk": sleep_impact}

    @staticmethod
    def prescribe_caffeine_curfew(target_bedtime_hh_mm: str, typical_dose_mg: float = 200.0) -> Dict[str, Any]:
        # Required elapsed time to decay to < 25mg: 200 * 0.5^(t/5.5) = 25 -> 3 half lives = 16.5 hours
        bed_h, bed_m = map(int, target_bedtime_hh_mm.split(":"))
        curfew_h = (bed_h - 10) % 24
        return {"target_bedtime": target_bedtime_hh_mm, "recommended_caffeine_curfew": f"{curfew_h:02d}:00", "rule": f"Cease caffeine 10 hours prior to sleep ({curfew_h:02d}:00) to clear adenosine A1/A2A receptors."}
