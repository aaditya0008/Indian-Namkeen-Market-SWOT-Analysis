from fastapi import FastAPI
from typing import Dict, Any
from SWOTkpi.Source import (
    analyze_review_themes as analyze_review_themes_logic,
    analyze_social_media_metrics as analyze_social_media_metrics_logic,
    analyze_website_issues as analyze_website_issues_logic,
    analyze_response_rates as analyze_response_rates_logic,
    news_sentiment_spikes as news_sentiment_spikes_logic,
    search_volume_rank as search_volume_rank_logic,
    analyze_sentiment_score as analyze_sentiment_score_logic,
    product_range_visibility as product_range_visibility_logic,
    analyze_ecommerce_presence as analyze_ecommerce_presence_logic,
    high_review_volume as high_review_volume_logic,
    analyze_high_growth_adjacent_categories as analyze_high_growth_adjacent_categories_logic,
    analyze_trend_alignment as analyze_trend_alignment_logic,
    analyze_unmet_needs as analyze_unmet_needs_logic,
    analyze_competitor_weaknesses as analyze_competitor_weaknesses_logic,
    geographic_search_opportunity as geographic_search_opportunity_logic,
)

app = FastAPI(title="SWOT Specific Indicators APIs")

@app.get("/kpi/review-theme-analysis")
def analyze_review_themes() -> Dict[str, Any]:
    return analyze_review_themes_logic()

@app.get("/Lower_Engagement_Rate/")
def analyze_social_media_metrics() -> Dict[str, Any]:
    return analyze_social_media_metrics_logic()

@app.get("/website_usability_issues/")
def analyze_website_issues() -> Dict[str, Any]:
    return analyze_website_issues_logic()

@app.get("/analyze_response_rates/")
async def analyze_response_rates() -> Dict[str, Any]:
    return await analyze_response_rates_logic()

@app.get("/news_sentiment_spikes/")
async def news_sentiment_spikes() -> Dict[str, Any]:
    return await news_sentiment_spikes_logic()

@app.get("/search_volume_rank/")
async def search_volume_rank() -> Dict[str, Any]:
    return await search_volume_rank_logic()

@app.get("/analyze_sentiment_score/")
async def analyze_sentiment_score() -> Dict[str, Any]:
    return await analyze_sentiment_score_logic()

@app.get("/product_range_visibility/")
async def product_range_visibility() -> Dict[str, Any]:
    return await product_range_visibility_logic()

@app.get("/analyze_ecommerce_presence/")
async def analyze_ecommerce_presence() -> Dict[str, Any]:
    return await analyze_ecommerce_presence_logic()

@app.get("/high_review_volume/")
async def high_review_volume() -> Dict[str, Any]:
    return await high_review_volume_logic()

@app.get("/analyze_high_growth_adjacent_categories/")
async def analyze_high_growth_adjacent_categories() -> Dict[str, Any]:
    return await analyze_high_growth_adjacent_categories_logic()

@app.get("/analyze_trend_alignment/")
async def analyze_trend_alignment() -> Dict[str, Any]:
    return await analyze_trend_alignment_logic()

@app.get("/analyze_unmet_needs/")
async def analyze_unmet_needs() -> Dict[str, Any]:
    return await analyze_unmet_needs_logic()

@app.get("/analyze_competitor_weaknesses/")
async def analyze_competitor_weaknesses() -> Dict[str, Any]:
    return await analyze_competitor_weaknesses_logic()

@app.get("/geographic_search_opportunity/")
def geographic_search_opportunity() -> Dict[str, Any]:
    return  geographic_search_opportunity_logic()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)