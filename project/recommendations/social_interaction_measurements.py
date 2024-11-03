def analyze_social_interaction(social_count, quality_of_interactions=None, engagement_in_community=None):
    print(f"Debug - Social interaction analysis: social_count={social_count}, quality_of_interactions={quality_of_interactions}, engagement_in_community={engagement_in_community}")

    # Recommend increasing social interactions if below threshold
    if social_count < 2:
        advice = [
            "Your social interaction frequency is low. Consider joining community groups or participating in activities that interest you.",
            "Strengthen connections by reaching out to friends or family members you haven't seen in a while."
        ]
        if quality_of_interactions and quality_of_interactions < 3:
            advice.append("Focus on deepening the quality of your current social interactions for more meaningful connections.")
        if not engagement_in_community:
            advice.append("Participating in volunteer work or local events can enhance your social network and improve emotional well-being.")
        return " ".join(advice)

    # Acknowledge sufficient social interactions and provide positive reinforcement
    else:
        feedback = [
            "You have a healthy level of social interactions. Keep nurturing these connections.",
            "Engagement in meaningful activities helps maintain mental and emotional health."
        ]
        if engagement_in_community:
            feedback.append("Your active participation in community events is excellent for fostering resilience and overall well-being.")
        return " ".join(feedback)

# Example usage:
# result = analyze_social_interaction(1, quality_of_interactions=2, engagement_in_community=False)
# print(result)




def analyze_social_interaction(social_count, quality_of_interactions=None, engagement_in_community=None,
                                emotional_support=None, digital_social_activity=None, social_event_frequency=None,
                                family_interactions=None, online_vs_in_person_ratio=None, social_network_size=None,
                                trust_in_friends=None, time_spent_socializing=None, shared_activities=None,
                                new_connections=None, work_social_balance=None, volunteering_hours=None,
                                social_media_sentiment=None, interaction_diversity=None, conversation_quality=None,
                                group_involvement=None, social_responsibilities=None):
    recommendations = []

    # Basic check for social count
    if social_count < 2:
        recommendations.append("Your social interaction frequency is low. Consider joining community groups or participating in activities that interest you.")

    # Assess the quality of interactions
    if quality_of_interactions and quality_of_interactions < 3:
        recommendations.append("Focus on deepening the quality of your current social interactions for more meaningful connections.")

    # Check for engagement in community activities
    if not engagement_in_community:
        recommendations.append("Participating in volunteer work or local events can enhance your social network and improve emotional well-being.")

    # Emotional support analysis
    if not emotional_support:
        recommendations.append("Seek emotional support by talking to close friends or joining support groups to build resilience.")

    # Balance between digital and in-person social activity
    if digital_social_activity and digital_social_activity > 4:
        recommendations.append("While digital interactions are beneficial, try to balance them with face-to-face interactions for more personal connections.")

    # Frequency of attending social events
    if social_event_frequency and social_event_frequency < 1:
        recommendations.append("Consider attending more social events or gatherings to increase your exposure to different social settings.")

    # Family interactions
    if family_interactions and family_interactions < 2:
        recommendations.append("Strengthen family ties by scheduling regular meetups or calls with loved ones.")

    # Ratio of online to in-person interactions
    if online_vs_in_person_ratio and online_vs_in_person_ratio > 2:
        recommendations.append("Aim to have more in-person interactions as they can have a more positive impact on your mental health.")

    # Social network size
    if social_network_size and social_network_size < 5:
        recommendations.append("Expanding your social network can provide more diverse support and opportunities for engagement.")

    # Trust in friends
    if trust_in_friends and trust_in_friends < 3:
        recommendations.append("Building trust within your social circle can enhance the quality of your relationships.")

    # Time spent socializing
    if time_spent_socializing and time_spent_socializing < 2:
        recommendations.append("Allocate more time to socializing to boost your mood and strengthen bonds.")

    # Shared activities with friends or groups
    if shared_activities and shared_activities < 2:
        recommendations.append("Engaging in shared activities can deepen relationships and create memorable experiences.")

    # Building new connections
    if not new_connections:
        recommendations.append("Consider joining new social or professional groups to build fresh connections.")

    # Balance between work and social life
    if work_social_balance and work_social_balance < 5:
        recommendations.append("Ensure you balance work and social activities to avoid isolation and burnout.")

    # Volunteering hours
    if volunteering_hours and volunteering_hours < 1:
        recommendations.append("Volunteering can provide a sense of purpose and foster community bonds. Try incorporating it into your routine.")

    # Sentiment analysis of social media
    if social_media_sentiment and social_media_sentiment < 0:
        recommendations.append("Consider curating your social media activity to focus on positive interactions.")

    # Interaction diversity
    if interaction_diversity and interaction_diversity < 3:
        recommendations.append("Interacting with diverse groups of people can broaden your perspectives and strengthen social adaptability.")

    # Quality of conversations
    if conversation_quality and conversation_quality < 3:
        recommendations.append("Aim for deeper, meaningful conversations that foster connection and understanding.")

    # Group involvement
    if group_involvement and group_involvement < 2:
        recommendations.append("Participating in group activities can improve teamwork skills and provide a sense of belonging.")

    # Social responsibilities
    if social_responsibilities and social_responsibilities > 5:
        recommendations.append("While being socially active is positive, ensure your social responsibilities do not become overwhelming.")

    if not recommendations:
        return "Your social interactions appear balanced. Keep nurturing your relationships and participating in activities that bring you joy."

    return " ".join(recommendations)

print(f"Debug - Social interaction analysis: social_count={social_count}, quality_of_interactions={quality_of_interactions}, engagement_in_community={engagement_in_community}, emotional_support={emotional_support}, digital_social_activity={digital_social_activity}, social_event_frequency={social_event_frequency}, family_interactions={family_interactions}, online_vs_in_person_ratio={online_vs_in_person_ratio}, social_network_size={social_network_size}, trust_in_friends={trust_in_friends}, time_spent_socializing={time_spent_socializing}, shared_activities={shared_activities}, new_connections={new_connections}, work_social_balance={work_social_balance}, volunteering_hours={volunteering_hours}, social_media_sentiment={social_media_sentiment}, interaction_diversity={interaction_diversity}, conversation_quality={conversation_quality}, group_involvement={group_involvement}, social_responsibilities={social_responsibilities}")

