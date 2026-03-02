from data_pipeline.fetch_gsc import fetch_gsc_data
from opportunity_engine.opportunities import (
    detect_ctr_opportunities,
    detect_growth_topics
)
from agent.seo_agent import run_seo_agent


def prepare_summary(ctr_ops, growth_ops):

    return f"""
CTR Opportunities (Top 10):
{ctr_ops.head(10).to_string()}

Growth Topic Opportunities:
{growth_ops.head(10).to_string()}
"""


def main():

    print("Fetching GSC data...")
    df = fetch_gsc_data()

    print("Detecting opportunities...")
    ctr_ops = detect_ctr_opportunities(df)
    growth_ops = detect_growth_topics(df)

    summary = prepare_summary(ctr_ops, growth_ops)

    print("Running SEO Agent...")
    insights = run_seo_agent(summary)

    print("\n===== SEO INSIGHTS =====\n")
    print(insights)


if __name__ == "__main__":
    main()
