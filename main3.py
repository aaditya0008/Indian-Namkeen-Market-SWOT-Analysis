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

@app.get("/E1_Strength/High_Brand_Search_Volume_Rank/")
async def search_volume_rank() -> Dict[str, Any]:
    return await search_volume_rank_logic()

@app.get("/E2_Strength/Positive_Overall_Sentiment_Score/")
async def analyze_sentiment_score() -> Dict[str, Any]:
    return await analyze_sentiment_score_logic()

@app.get("/E3_Strength/Wide_Product_Range_Visibility/")
async def product_range_visibility() -> Dict[str, Any]:
    return await product_range_visibility_logic()

@app.get("/E4_Strength/Strong_Ecommerce_Presence/Ratings/")
async def analyze_ecommerce_presence() -> Dict[str, Any]:
    return await analyze_ecommerce_presence_logic()

@app.get("/E5_Strength/High_review_volume/")
async def high_review_volume() -> Dict[str, Any]:
    return await high_review_volume_logic()

@app.get("/E6_Weakness/Key_Negative_Review_Themes_Frequency")
def analyze_review_themes() -> Dict[str, Any]:
    return analyze_review_themes_logic()

@app.get("/E7_Weakness/Lower_Engagement_Rate_vs_Select_Competitors/")
def analyze_social_media_metrics() -> Dict[str, Any]:
    return analyze_social_media_metrics_logic()

@app.get("/E8_Weakness/Identified_Website_usability_issues/")
def analyze_website_issues() -> Dict[str, Any]:
    return analyze_website_issues_logic()

@app.get("/E9_Weakness/Gaps_in_Online_Customer_Service_Response/")
async def analyze_response_rates() -> Dict[str, Any]:
    return await analyze_response_rates_logic()

@app.get("/E10_Weakness/Negative_News_Sentiment_Spikes/")
async def news_sentiment_spikes() -> Dict[str, Any]:
    return await news_sentiment_spikes_logic()

@app.get("/E11_Opportunities/High_Growth_Rate_In_Adjacent_Categories/")
async def analyze_high_growth_adjacent_categories() -> Dict[str, Any]:
    return await analyze_high_growth_adjacent_categories_logic()

@app.get("/E12_Opportunities/Rising_Trend_Alignment/")
async def analyze_trend_alignment() -> Dict[str, Any]:
    return await analyze_trend_alignment_logic()

@app.get("/E13_Opportunities/Unmet_Needs_Identified_In_Reviews/")
async def analyze_unmet_needs() -> Dict[str, Any]:
    return await analyze_unmet_needs_logic()

@app.get("/E14_Opportunities/Competitor_Weaknesses_Identified/")
async def analyze_competitor_weaknesses() -> Dict[str, Any]:
    return await analyze_competitor_weaknesses_logic()

@app.get("/E15_Opportunities/Untapped_Geographic_Search_Interest/")
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

# Advanced Consumer Behavior & Journey Insights (OSINT) 
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse

from services.basket_composition_service import get_basket_composition_chart
from services.Influence_Attribution import generate_mentions_by_platform_image
from services.Trust_Analysis import generate_trust_analysis_plot
from services.Search_Behaviour_Evolution import generate_search_behavior_evolution_chart
from services.Community_Engagement import community_engagement_chart
from services.User_Segmentation_Proxy import user_segmentation_proxy
from services.Post_Purchase_Dissonance import PostPurchaseDissonance
from services.Subscription_Intrest_Level import generate_subscription_pie_chart
from services.Mobile_vs_Desktop_interaction import generate_mobile_desktop_bar_chart
from services.Keyword_performancce import generate_high_intent_keyword_trend_chart
from services.Brand_switching import generate_switch_trigger_chart
from services.Platform_role import get_platform_funnel_kpi_chart
from services.Purchase_frequency import generate_purchase_frequency_chart
from services.Return_refund_issue import generate_issue_type_chart
from services.Generation_wise_usage import generate_cross_generation_chart
from services.health_awareness_spectrum import get_health_awareness_chart
from services.Recipe_Integration import get_recipe_usage_figure_bytes
from services.Homemade_vs_local import create_chart_image
from services.Impulse_purchase import generate_impulse_kpi_chart
from services.Unboxing_review import get_chart_response
from services.Digital_Payment import generate_payment_issues_chart
from services.Gift_card_mention import create_user_type_pie_chart 
from services.food_hack import generate_hacktype_bar_chart
from services.cultural_discussion import generate_contextual_indicators_chart
from services.Variety_information import generate_information_overload_chart
from services.online_influence import load_and_process_data, plot_kpi_bar_chart
from services.Price_increase_reactions import load_reactions, create_pie_chart

ppd = PostPurchaseDissonance()


@app.get("I-10_basket-composition-clues")
def basket_composition_kpi():
    img_bytes = get_basket_composition_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("I-11_Influence-Attribution-Guesses")
def influence_platform_mentions():
    img_buf = generate_mentions_by_platform_image()
    return StreamingResponse(img_buf, media_type="image/png")

@app.get("I-28_search-behavior-evolution")
def get_search_behavior_evolution():
    img_bytes = generate_search_behavior_evolution_chart()
    return Response(content=img_bytes, media_type="image/png")

CSV_FILE_PATH = "KPI_Data/Trust_Analysis.csv"
@app.get("I-27_Trust-Indicator-Analysis", response_class=Response)
async def trust_analysis():
    img_bytes = generate_trust_analysis_plot(CSV_FILE_PATH)
    return Response(content=img_bytes, media_type="image/png")

@app.get("I-26_Post-Purchase-Dissonance-Signals")
def get_dissonance_chart():
    img = ppd.generate_dissonance_chart()
    return Response(content=img, media_type="image/png")

@app.get("I-8_Community-Engagement-Level")
def show_chart():
    return community_engagement_chart()

@app.get("I-7_User-Segmentation-Proxy", response_class=Response)
def segmentation_chart():
    return user_segmentation_proxy()

@app.get("I-13_Subscription_Interest_Signals")
def subscription_interest_pie_chart():
    img_bytes = generate_subscription_pie_chart()
    return Response(content=img_bytes, media_type="image/png")

@app.get("I-6_mobile-desktop-interaction")
def mobile_desktop_interaction():
    img_buf = generate_mobile_desktop_bar_chart()
    return StreamingResponse(img_buf, media_type="image/png")

@app.get("I-4_high-intent-keyword-trends")
def get_high_intent_keyword_trends():
    csv_path = 'KPI_Data/Keyword_Performance.csv'
    image_bytes = generate_high_intent_keyword_trend_chart(csv_path)
    return Response(content=image_bytes, media_type="image/png")

@app.get("I-3_Brand_switching_triggers")
def get_switch_trigger_chart():
    chart_path = generate_switch_trigger_chart()
    return FileResponse(chart_path, media_type="image/png")

@app.get("I-2_Platform_Role_in_Purchase_Funnel ")
def platform_funnel_kpi_chart():
    return get_platform_funnel_kpi_chart()

@app.get("I-9_Purchase-Frequency-Indicators")
def get_purchase_frequency_image():
    generate_purchase_frequency_chart()
    return FileResponse("purchase_frequency_mentions.png", media_type="image/png")

CSV_PATH = "KPI_Data/Return_refund_issues.csv"
@app.get("I-12_Return_refund_issues")
def issue_type_chart():
    img_bytes = generate_issue_type_chart(CSV_PATH)
    return Response(content=img_bytes, media_type="image/png")

CSV_FILE = "KPI_data/Generation_wise_Consumption.csv"  # Adjust path as needed
@app.get("I-15_cross-generation-usage")
def cross_generation_usage_kpi():
    img = generate_cross_generation_chart(CSV_FILE)
    return Response(content=img.read(), media_type="image/png")

@app.get("I-16_Health_Consciousness_Spectrum")
def health_awareness_endpoint():
    return get_health_awareness_chart()

@app.get("I-17_Recipe_Usage/Integration_Mentions")
def recipe_usage_png():
    csv_path = "KPI_Data/Recipe_Integration_Mentions.csv"
    img_bytes = get_recipe_usage_figure_bytes(csv_path)
    return Response(content=img_bytes, media_type="image/png")

@app.get("I-18_Comparison-with-Homemade/Local-Alternatives")
def get_chart():
    img_bytes = create_chart_image()
    return Response(content=img_bytes, media_type="image/png")

@app.get("I-19_Impulse_Purchase_Indicators")
def impulse_kpi():
    img_bytes = generate_impulse_kpi_chart()
    return Response(content=img_bytes, media_type="image/png")

@app.get("I-20_Unboxing_Experience_Mentions")
async def chart_png():
    return get_chart_response()

@app.get("I-21_Digital_Payment_Preference/Issues")
def payment_issues_chart():
    png_bytes = generate_payment_issues_chart()
    return Response(content=png_bytes, media_type="image/png")

@app.get("/kpi/user-types")
def user_types_pie_chart():
    return create_user_type_pie_chart()

@app.get("I-23_Food_Hack_Mentions")
def get_hacktype_chart():
    img_buf = generate_hacktype_bar_chart()
    return Response(content=img_buf.read(), media_type="image/png")

@app.get("/kpi/contextual-indicators")
async def get_contextual_indicators_chart():
    return generate_contextual_indicators_chart()

@app.get("/kpi/information-overload")
def get_information_overload_chart():
    image_path = generate_information_overload_chart()
    return FileResponse(image_path, media_type="image/png")

CSV_PATH = "KPI_Data/online_influence.csv"  # Adjust path as needed
@app.get("/online_influence")
def get_kpi_bar_chart():
    summary_df = load_and_process_data(CSV_PATH)
    img_buf = plot_kpi_bar_chart(summary_df)
    return Response(content=img_buf.read(), media_type="image/png")

CSV_PATH = "KPI_Data/Price_increase_reactions.csv" 
@app.get("/price-increase-sentiment")
def price_increase_sentiment_pie():
    labels, sizes = load_reactions(CSV_PATH)
    img_buf = create_pie_chart(labels, sizes)
    return Response(content=img_buf.read(), media_type="image/png")



#H_KPI_FastAPI
from fastapi import FastAPI, Response, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse, StreamingResponse

import numpy as np

from H_adv_analysis_kpi.KPI1 import get_attribute_frequency_chart
from H_adv_analysis_kpi.KPI2 import get_attribute_frequency_chart_kpi2_with_sentiment
from H_adv_analysis_kpi.KPI3 import get_kpi3_sheet1_campaign_timeline_chart
from H_adv_analysis_kpi.KPI4 import router as kpi4_router
from H_adv_analysis_kpi.KPI5 import get_kpi5_chart
from H_adv_analysis_kpi.KPI6 import read_kpi6_excel
from H_adv_analysis_kpi.KPI7 import get_brand_personality_radar
from H_adv_analysis_kpi.KPI8 import get_kpi8_dashboard_chart_and_data
from H_adv_analysis_kpi.KPI9 import get_kpi9_reviews_data
from H_adv_analysis_kpi.KPI10 import get_comparison_sheet_sections
from H_adv_analysis_kpi.KPI11 import get_docx_file_response
from H_adv_analysis_kpi.KPI12 import analyze_kpi12_data
from H_adv_analysis_kpi.KPI13 import get_conversion_funnel_chart_improved
from H_adv_analysis_kpi.KPI14 import analyze_data
from H_adv_analysis_kpi.KPI15 import get_sheet2_data
from H_adv_analysis_kpi.KPI16 import get_value_perception_charts
from H_adv_analysis_kpi.KPI17 import get_sheet1_data
from H_adv_analysis_kpi.KPI18 import get_kpi18_sheet5_data
from H_adv_analysis_kpi.KPI19 import get_kpi19_sheet1_data
from H_adv_analysis_kpi.KPI20 import get_kpi20_sheet2_data
from H_adv_analysis_kpi.KPI21 import get_kpi21_sheet1_data
from H_adv_analysis_kpi.KPI22 import get_category_pie_chart
from H_adv_analysis_kpi.KPI23 import get_kpi23_sheet1_data
from H_adv_analysis_kpi.KPI24 import get_kpi24_sheet3_data, get_kpi24_qualitative_assessment_details
from H_adv_analysis_kpi.KPI25 import get_crisis_sentiment_trends_chart

app.include_router(kpi4_router)

@app.get("/H/kpi1/attribute-frequency")
def attribute_frequency_kpi():
    img_bytes = get_attribute_frequency_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi2/sentiment-breakdown")
def sentiment_breakdown_kpi2():
    img_bytes = get_attribute_frequency_chart_kpi2_with_sentiment()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi3/sheet2-chart")
def kpi3_sheet2_chart():
    img_bytes = get_kpi3_sheet1_campaign_timeline_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/")
def main():
    return {"message": "Main function called"}

@app.get("/H/kpi5/chart")
def kpi5_chart():
    img_bytes = get_kpi5_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi6/data")
def get_kpi6_data():
    df = read_kpi6_excel()
    if df is None:
        raise HTTPException(status_code=400, detail="Error reading Excel file")
    df = df.replace([np.nan, np.inf, -np.inf], None)
    return df.to_dict(orient="records")

@app.get("/H/kpi7/brand-personality-radar")
def brand_personality_radar_kpi():
    img_bytes = get_brand_personality_radar()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi8/dashboard-image")
def get_dashboard_image():
    img_bytes, _ = get_kpi8_dashboard_chart_and_data()
    if not img_bytes:
        raise HTTPException(404, "No data available to generate chart")
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi8/dashboard-data")
def get_dashboard_data():
    img_bytes, df = get_kpi8_dashboard_chart_and_data()
    if df.empty:
        raise HTTPException(404, "No data available in Sheet3")
    return JSONResponse({
        "chart_url": "/H/kpi8/dashboard-image",
        "sheet3_data": df.replace({np.nan: None}).to_dict(orient="records")
    })

@app.get("/H/kpi9/reviews")
def kpi9_reviews():
    try:
        return get_kpi9_reviews_data()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading KPI-9 file: {e}")

@app.get("/H/kpi10/comparison-full")
def comparison_full():
    try:
        return get_comparison_sheet_sections()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing Comparison sheet: {e}")

@app.get("/H/kpi11/doc-file")
def serve_docx():
    response = get_docx_file_response()
    if response is None:
        raise HTTPException(status_code=404, detail="File not found")
    return response

@app.get("/H/kpi12/results")
def get_kpi12_results():
    results = analyze_kpi12_data()
    if not results:
        raise HTTPException(status_code=404, detail="KPI data not found")
    return results

@app.get("/H/kpi13/conversion-funnel")
def conversion_funnel_kpi():
    img_bytes = get_conversion_funnel_chart_improved()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi14/results")
def get_kpi14_results():
    results = analyze_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="KPI data not found",
            headers={"X-Error": "KPI14_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/H/kpi15/sheet2")
def get_kpi15_sheet2():
    results = get_sheet2_data()
    if not results:
        raise HTTPException(status_code=404, detail="No data found in Sheet2 of KPI-15.xlsx")
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/H/kpi16/value-perception-charts")
def value_perception_kpi():
    img_bytes = get_value_perception_charts()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi17/sheet1")
def get_kpi17_sheet1():
    try:
        results = get_sheet1_data()
        if not results:
            raise HTTPException(status_code=404, detail="No data found in Sheet1 of KPI-17.xlsx")
        return {"status": "success", "results": results, "count": len(results)}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Excel file not found")

@app.get("/H/kpi18/sheet5")
def get_kpi18_sheet5():
    results = get_kpi18_sheet5_data()
    if not results:
        raise HTTPException(status_code=404, detail="No data found in Sheet5 of KPI-18.xlsx")
    return {"status": "success", "results": results, "count": len(results)}

@app.get("/H/kpi19/sheet1")
def get_kpi19_sheet1():
    results = get_kpi19_sheet1_data()
    if not results:
        raise HTTPException(status_code=404, detail="No data found in Sheet1 of KPI-19.xlsx")
    return {"status": "success", "results": results, "count": len(results)}

@app.get("/H/kpi20/sheet2")
def get_kpi20_sheet2():
    results = get_kpi20_sheet2_data()
    if not results:
        raise HTTPException(status_code=404, detail="No data found in Sheet2 of KPI-20.xlsx")
    return {"status": "success", "results": results, "count": len(results)}

@app.get("/H/kpi21/sheet1")
def get_kpi21_sheet1():
    results = get_kpi21_sheet1_data()
    if not results:
        raise HTTPException(status_code=404, detail="No data found in Sheet1 of KPI-21.xlsx")
    return {"status": "success", "results": results, "count": len(results)}

@app.get("/H/kpi22/category-pie-chart")
def category_pie_chart_kpi():
    img_bytes = get_category_pie_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/H/kpi23/sheet1")
def get_kpi23_sheet1():
    results = get_kpi23_sheet1_data()
    if not results:
        raise HTTPException(status_code=404, detail="No data found in Sheet1 of KPI-23.xlsx")
    return {"status": "success", "results": results, "count": len(results)}

# Uncomment this if needed
# @app.get("/H/kpi24/sheet3")
# def get_kpi24_sheet3():
#     results = get_kpi24_sheet3_data()
#     if not results:
#         raise HTTPException(status_code=404, detail="No valid data found in Sheet3 of KPI-24.xlsx")
#     return {"status": "success", "results": results, "count": len(results)}

@app.get("/H/kpi24/qualitative-assessment")
def get_kpi24_qualitative_assessment():
    results = get_kpi24_qualitative_assessment_details()
    if not results:
        raise HTTPException(status_code=404, detail="No qualitative assessment details found")
    return {"status": "success", "results": results, "count": len(results)}

@app.get("/H/kpi25/brand-resilience-score")
def brand_resilience_score():
    img_bytes = get_crisis_sentiment_trends_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

#D_KPI

from fastapi import FastAPI
from PhysicalKPI import (
    KPI1, KPI2, KPI3, KPI4, KPI5, KPI6, KPI7, KPI8,
    KPI9, KPI10, KPI11, KPI12, KPI13, KPI14, KPI15
)

# ✅ Register all 15 KPI Routers
app.include_router(KPI1.router, prefix="/KPI1", tags=["D_KPI 1"])
app.include_router(KPI2.router, prefix="/KPI2", tags=["D_KPI 2"])
app.include_router(KPI3.router, prefix="/KPI3", tags=["D_KPI 3"])
app.include_router(KPI4.router, prefix="/KPI4", tags=["D_KPI 4"])
app.include_router(KPI5.router, prefix="/KPI5", tags=["D_KPI 5"])
app.include_router(KPI6.router, prefix="/KPI6", tags=["D_KPI 6"])
app.include_router(KPI7.router, prefix="/KPI7", tags=["D_KPI 7"])
app.include_router(KPI8.router, prefix="/KPI8", tags=["D_KPI 8"])
app.include_router(KPI9.router, prefix="/KPI9", tags=["D_KPI 9"])
app.include_router(KPI10.router, prefix="/KPI10", tags=["D_KPI 10"])
app.include_router(KPI11.router, prefix="/KPI11", tags=["D_KPI 11"])
app.include_router(KPI12.router, prefix="/KPI12", tags=["D_KPI 12"])
app.include_router(KPI13.router, prefix="/KPI13", tags=["D_KPI 13"])
app.include_router(KPI14.router, prefix="/KPI14", tags=["D_KPI 14"])
app.include_router(KPI15.router, prefix="/KPI15", tags=["D_KPI 15"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# To run the FastAPI application, use the command: uvicorn main3:app --reload
