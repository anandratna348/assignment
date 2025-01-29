import pandas as pd
from datetime import datetime

def analytics_ideas(group_info, member_info, message_info):
    """
    This function contains 20 analytics ideas implemented as functions.
    Parameters:
        group_info (pd.DataFrame): DataFrame containing group information.
        member_info (pd.DataFrame): DataFrame containing member information.
        message_info (pd.DataFrame): DataFrame containing message information.
    Returns:
        dict: A dictionary with the results of each analytic.
    """
    results = {}

    # 1. Daily Messages Sent
    results['daily_messages_sent'] = message_info.groupby(message_info['timestamp'].dt.date).size().to_dict()

    # 2. Group Member Growth
    results['group_member_growth'] = member_info.groupby('group_id')['user_id'].count().to_dict()

    # 3. Top Active Groups
    results['top_active_groups'] = message_info['group_id'].value_counts().head(5).to_dict()

    # 4. Messages Per Member
    messages_per_member = message_info.groupby('sender_id').size().mean()
    results['messages_per_member'] = messages_per_member

    # 5. Admin-to-Member Ratio
    admin_count = member_info[member_info['role'] == 'admin'].groupby('group_id')['user_id'].count()
    member_count = member_info.groupby('group_id')['user_id'].count()
    admin_to_member_ratio = (admin_count / member_count).fillna(0).to_dict()
    results['admin_to_member_ratio'] = admin_to_member_ratio

    # 6. Bot Usage Analysis
    bot_messages = message_info[message_info['sender_id'].isin(member_info[member_info['is_bot'] == True]['user_id'])].shape[0]
    results['bot_usage_analysis'] = bot_messages

    # 7. Pinned Message Trends
    results['pinned_message_trends'] = group_info[['group_id', 'pinned_messages', 'pinned_messages_timestamp']].dropna().to_dict('records')

    # 8. Member Retention Rate
    first_join_date = member_info.groupby('group_id')['join_date'].min()
    retention_rate = (member_info.groupby('group_id').size() / first_join_date.count()).to_dict()
    results['member_retention_rate'] = retention_rate

    # 9. Daily Join and Leave Rates
    daily_join_rate = member_info.groupby(member_info['join_date'].dt.date).size().to_dict()
    results['daily_join_rate'] = daily_join_rate

    # 10. Hashtag Usage Frequency
    hashtags = message_info['hashtags'].explode().value_counts().to_dict()
    results['hashtag_usage_frequency'] = hashtags

    # 11. Message Types Distribution
    message_types_distribution = message_info['message_type'].value_counts().to_dict()
    results['message_types_distribution'] = message_types_distribution

    # 12. Message Replies Analysis
    results['message_replies_analysis'] = message_info[['message_id', 'replies']].dropna().to_dict('records')

    # 13. Top Contributors
    top_contributors = message_info['sender_id'].value_counts().head(5).to_dict()
    results['top_contributors'] = top_contributors

    # 14. Inactive Members Count
    active_members = message_info['sender_id'].unique()
    inactive_members = member_info[~member_info['user_id'].isin(active_members)]['user_id'].count()
    results['inactive_members_count'] = inactive_members

    # 15. Bot-to-Human Ratio
    bot_count = member_info[member_info['is_bot'] == True].shape[0]
    human_count = member_info[member_info['is_bot'] == False].shape[0]
    results['bot_to_human_ratio'] = bot_count / human_count

    # 16. Group Visibility Trends
    visibility_trends = group_info['visibility'].value_counts().to_dict()
    results['group_visibility_trends'] = visibility_trends

    # 17. Message Forwarding Trends
    forwarding_trends = message_info.groupby('timestamp')['forwards'].sum().to_dict()
    results['message_forwarding_trends'] = forwarding_trends

    # 18. URL Sharing Frequency
    url_sharing_frequency = message_info['urls'].explode().value_counts().to_dict()
    results['url_sharing_frequency'] = url_sharing_frequency

    # 19. Daily Active Members
    daily_active_members = message_info.groupby(message_info['timestamp'].dt.date)['sender_id'].nunique().to_dict()
    results['daily_active_members'] = daily_active_members

    # 20. Average Message Views
    average_message_views = message_info['views'].mean()
    results['average_message_views'] = average_message_views

    return results
# Example usage (assuming you have DataFrames loaded):
# group_info_df = pd.read_csv('group_info.csv')
# member_info_df = pd.read_csv('member_info.csv')
# message_info_df = pd.read_csv('message_info.csv')
# analytics_results = analytics_ideas(group_info_df, member_info_df, message_info_df)
# print(analytics_results)


