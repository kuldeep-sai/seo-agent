import pandas as pd

# Expected CTR benchmark (simple model)
def expected_ctr(position):
    if position <= 3:
        return 0.25
    elif position <= 10:
        return 0.12
    else:
        return 0.05


def detect_ctr_opportunities(df):

    df["expected_ctr"] = df["position"].apply(expected_ctr)

    opportunities = df[
        (df["position"] <= 12) &
        (df["impressions"] > 500) &
        (df["ctr"] < df["expected_ctr"])
    ]

    opportunities["opportunity_score"] = (
        opportunities["impressions"]
        * (opportunities["expected_ctr"] - opportunities["ctr"])
    )

    return opportunities.sort_values(
        "opportunity_score", ascending=False
    )


def detect_growth_topics(df):

    return df[
        (df["impressions"] > 1000) &
        (df["position"] > 20)
    ].sort_values("impressions", ascending=False)
