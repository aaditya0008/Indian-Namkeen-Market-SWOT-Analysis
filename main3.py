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




# Competitive and advanced competitive analysis endpoints
from fastapi.responses import StreamingResponse, Response
from adv_comp.backlink import backlink_endpoint
from adv_comp.Content_Marketing_Sophistication import content_marketing_endpoint
from adv_comp.emp_rating import emp_rating_endpoint
from adv_comp.geo_expan import geo_expansion_endpoint
from adv_comp.innovation_rate import innovation_rate_endpoint
import io
from adv_comp.leadership_visibility import leadership_visibility_endpoint
from adv_comp.LitigationRegulatory import litigation_issue_data, litigation_issue_plot
from fastapi.responses import StreamingResponse
from adv_comp.marketing_msg_consistency import marketing_message_scores, marketing_message_consistency_plot
import io
from adv_comp.narrative_control import narrative_control_data, narrative_control_plot
from adv_comp.niche_targeting import niche_targeting_plot
from adv_comp.patnership_network import get_partnership_data
from adv_comp.pivot import get_strategic_pivot_dossier
from adv_comp.pricing_strat_agg import get_pricing_aggressiveness_table, get_pricing_aggressiveness_plot
from adv_comp.product_issue import analyze_product_issues
from adv_comp.response import load_competitor_responses
from adv_comp.social_listening_eng import load_and_process_engagement
from adv_comp.talent import load_talent_acquisition_data
from adv_comp.tech import load_tech_adoption_summary
from adv_comp.vulnerability import load_and_rank_competitors
from fastapi.responses import JSONResponse
from adv_comp.backlink import process_backlink_data



@app.get("/api/backlink-quality")
def get_backlink_quality():
    csv_path = "data/Competitor Website Backlink Qua.csv"
    result_df = process_backlink_data(csv_path)
    return JSONResponse(content=result_df.to_dict(orient="records"))

@app.get("/api/content-marketing-sophistication")
def get_content_marketing_sophistication():
    return content_marketing_endpoint()

@app.get("/api/emp-rating")
async def get_emp_rating():
    return await emp_rating_endpoint()

@app.get("/api/geo-expansion")
def get_geo_expansion():
    img_bytes = geo_expansion_endpoint()
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/png")

@app.get("/api/innovation-rate")
def get_innovation_rate():
    return innovation_rate_endpoint()

@app.get("/api/leadership-visibility")
def get_leadership_visibility():
    return leadership_visibility_endpoint()

@app.get("/api/litigation-issues/plot")
def get_litigation_issues_plot():
    image_bytes = litigation_issue_plot()
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")

@app.get("/api/marketing-message-scores")
def get_marketing_scores():
    return marketing_message_scores()

@app.get("/api/marketing-message-consistency-plot")
def get_marketing_plot():
    img_bytes = marketing_message_consistency_plot()
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/png")
@app.get("/api/narrative-control-data")
def get_narrative_control_data():
    return narrative_control_data()

@app.get("/api/narrative-control-plot")
def get_narrative_control_plot():
    img_bytes = narrative_control_plot()
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/png")

@app.get("/api/niche-targeting-plot")
def get_niche_targeting_plot():
    img_bytes = niche_targeting_plot()
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/png")
@app.get("/api/partnership-network")
def partnership_network():
    data = get_partnership_data()
    return {"partnerships": data}
@app.get("/api/strategic-pivot-dossier")
def strategic_pivot_dossier():
    data = get_strategic_pivot_dossier()
    return {"dossiers": data}

@app.get("/api/pricing-aggressiveness-table")
def pricing_aggressiveness_table():
    data = get_pricing_aggressiveness_table()
    return {"pricing_aggressiveness": data}

@app.get("/api/pricing-aggressiveness-plot")
def pricing_aggressiveness_plot():
    img_bytes = get_pricing_aggressiveness_plot()
    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/png")

@app.get("/run-product-issue-analysis")
def run_product_issue_analysis():
    analyze_product_issues()
    return {"message": "Product issue analysis run successfully. Check console output and plot window."}

@app.get("/api/competitor-responses")
def get_competitor_responses():
    data = load_competitor_responses()
    return data
@app.get("/api/social-listening-engagement")
def social_listening_engagement():
    data = load_and_process_engagement()
    return {"engagement_data": data}

@app.get("/api/talent-acquisition")
def get_talent_acquisition():
    data = load_talent_acquisition_data()
    return {"talent_acquisition": data}

@app.get("/api/tech-adoption")
def get_tech_adoption():
    data = load_tech_adoption_summary()
    return {"tech_adoption": data}


@app.get("/api/vulnerability/ranks")
def get_competitor_ranks():
    ranked_competitors = load_and_rank_competitors()
    return {"competitor_ranks": ranked_competitors}




from SectionC.kpi1 import generate_search_volume_plot
from SectionC.kpi2 import generate_share_of_search_plot
from SectionC.kpi3 import generate_share_of_search_pie
from SectionC.kpi4 import generate_mention_volume_plot
from SectionC.kpi5 import generate_kpi5_plot
from SectionC.kpi6 import generate_kpi6_pie
from SectionC.kpi7 import generate_follower_count_table
from SectionC.kpi8 import generate_follower_growth_rate_plot
from SectionC.kpi9 import generate_posting_frequency_table
from SectionC.kpi10 import generate_engagement_rate_plot
from SectionC.kpi11 import generate_content_themes_plot
from SectionC.kpi12 import generate_traffic_estimate_table
from SectionC.kpi13 import generate_bounce_rate_table
from SectionC.kpi14 import generate_avg_visit_duration_table
from SectionC.kpi15 import generate_traffic_sources_pie
from SectionC.kpi16 import generate_seo_performance_plot
from SectionC.kpi17 import get_top_organic_keywords
from SectionC.kpi19 import generate_page_speed_table
from SectionC.kpi20 import generate_news_mention_frequency_plot
from SectionC.kpi22 import generate_total_reviews_table
from SectionC.kpi23 import generate_platform_ratings_bar
from SectionC.kpi24 import generate_positive_reviews_bar
from SectionC.kpi25 import generate_negative_reviews_bar
from SectionC.kpi26 import generate_response_rate_table
from SectionC.kpi28 import generate_comparison_table
from SectionC.kpi30 import generate_restaurant_presence_table
from SectionC.kpi29 import generate_qualitative_product_visibility_table
from SectionC.kpi21 import generate_news_sentiment_pie


@app.get("/kpi1/plot")
def get_search_volume_plot():
    img_bytes = generate_search_volume_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi2/plot")
def get_share_of_search_plot():
    img_bytes = generate_share_of_search_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi3/pie")
def get_share_of_search_pie():
    img_bytes = generate_share_of_search_pie()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi4/plot")
def get_mention_volume_plot():
    img_bytes = generate_mention_volume_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi5/pie")
def get_kpi5_plot():
    img_bytes = generate_kpi5_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi6/pie")
def get_kpi6_pie():
    img_bytes = generate_kpi6_pie()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi7/table")
def get_follower_count_table():
    img_bytes = generate_follower_count_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi8/plot")
def get_follower_growth_rate_plot():
    img_bytes = generate_follower_growth_rate_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi9/table")
def get_posting_frequency_table():
    img_bytes = generate_posting_frequency_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi10/plot")
def get_engagement_rate_plot():
    img_bytes = generate_engagement_rate_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi11/plot")
def get_content_themes_plot():
    img_bytes = generate_content_themes_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi12/table")
def get_traffic_estimate_table():
    img_bytes = generate_traffic_estimate_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi13/table")
def get_bounce_rate_table():
    img_bytes = generate_bounce_rate_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi14/table")
def get_avg_visit_duration_table():
    img_bytes = generate_avg_visit_duration_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi15/pie")
def get_traffic_sources_pie():
    img_bytes = generate_traffic_sources_pie()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi16/plot")
def get_seo_performance_plot():
    img_bytes = generate_seo_performance_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi17/top_keywords")
def top_organic_keywords():
    return get_top_organic_keywords()

@app.get("/kpi19/table")
def get_page_speed_table():
    img_bytes = generate_page_speed_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi20/plot")
def get_news_mention_frequency_plot():
    img_bytes = generate_news_mention_frequency_plot()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi21/pie")
def get_news_sentiment_pie():
    img_bytes = generate_news_sentiment_pie()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi22/table")
def get_total_reviews_table():
    img_bytes = generate_total_reviews_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi23/bar")
def get_platform_ratings_bar():
    img_bytes = generate_platform_ratings_bar()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi24/bar")
def get_positive_reviews_bar():
    img_bytes = generate_positive_reviews_bar()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi25/bar")
def get_negative_reviews_bar():
    img_bytes = generate_negative_reviews_bar()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi26/table")
def get_response_rate_table():
    img_bytes = generate_response_rate_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi28/table")
def get_comparison_table():
    img_bytes = generate_comparison_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi29/table")
def qualitative_product_visibility_table():
    img_bytes = generate_qualitative_product_visibility_table()
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi30/table")
def get_restaurant_presence_table():
    img_bytes = generate_restaurant_presence_table()
    return Response(content=img_bytes, media_type="image/png")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)