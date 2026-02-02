import requests
import pandas as pd

url = 'https://simpledebit.gocardless.io/api/'
token = 'EXAMPLE'

# Fetch merchants
def fetch_merchants():
    r = requests.get(f'{url}merchant', headers={'Authorization' : f'Bearer {token}'})
    r.raise_for_status()
    return r.json()

# Fetch transactions for specific merchant
def fetch_transactions(merchant_id):
    r = requests.get(f"{url}transaction", params={"merchant_id": merchant_id}, headers={'Authorization': f'Bearer {token}'})
    r.raise_for_status()
    return r.json()

# Calculate payouts for all merchants
def calculate_payouts():
    # Fetch all merchants
    merchants = fetch_merchants()
    
    payout_data = []
    
    for merchant in merchants:
        merchant_id = merchant['id']
        
        # Fetch transactions for this merchant
        transactions = fetch_transactions(merchant_id)
        
        # Filter completed transactions
        completed_transactions = []
        for t in transactions:
            if t['status'] == 'completed':
                completed_transactions.append(t)

        # Calculate metrics
        transaction_count = len(completed_transactions)
        total_amount = 0
        for t in completed_transactions:
            total_amount += t['amount']
        
        # Apply discount if transaction_count >= 5
        if transaction_count >= 5:
            discount_applied = total_amount * 0.1
        else:
            discount_applied = 0
        
        final_payout = total_amount - discount_applied
        
        # Add to payout data
        payout_data.append({
            'merchant_id': merchant_id,
            'merchant_name': merchant['name'],
            'total_amount': total_amount,
            'transaction_count': transaction_count,
            'discount_applied': discount_applied,
            'final_payout': final_payout,
            'currency': merchant['currency']
        })
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(payout_data)
    df = df.sort_values('final_payout', ascending=False)
    df.loc[df['discount_applied'] == 0, 'discount_applied'] = 'zero'
    df.to_csv('payouts.csv', index=False)

    return df

if __name__ == "__main__":
    try:
        df = calculate_payouts()
        print('Created payouts.csv!')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
