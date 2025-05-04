# Billing functionality commented out

from typing import Dict, Optional, Tuple

# Dummy functions to replace the original billing functionality
async def get_account_subscription(client, account_id: str) -> Optional[Dict]:
    """Dummy function that always returns None."""
    return None

async def calculate_monthly_usage(client, account_id: str) -> float:
    """Dummy function that always returns 0."""
    return 0.0

async def check_billing_status(client, account_id: str) -> Tuple[bool, str, Optional[Dict]]:
    """Dummy function that always allows running."""
    subscription = {
        'price_id': 'free_tier',
        'plan_name': 'Free'
    }
    return True, "OK", subscription

async def get_account_id_from_thread(client, thread_id: str) -> Optional[str]:
    """Get the account ID associated with a thread."""
    result = await client.table('threads') \
        .select('account_id') \
        .eq('thread_id', thread_id) \
        .limit(1) \
        .execute()

    if result.data and len(result.data) > 0:
        return result.data[0]['account_id']
    return None
