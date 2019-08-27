# https://leetcode.com/problems/invalid-transactions/description/

# 1169. Invalid Transactions

# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), 
# amount, and city of the transaction.

# Given a list of transactions, return a list of transactions that are possibly invalid.  
# You may return the answer in any order.


# Example 1:
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, 
# have the same name and is in a different city. Similarly the second one is invalid too.

# Example 2:
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]

# Example 3:
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]
 

# Constraints:
# transactions.length <= 1000
# Each transactions[i] takes the form "{name},{time},{amount},{city}"
# Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
# Each {time} consist of digits, and represent an integer between 0 and 1000.
# Each {amount} consist of digits, and represent an integer between 0 and 2000.


from collections import defaultdict
def invalidTransactions(transactions):
	res = set()
	d = defaultdict(list)
	for transaction in transactions:
		name, time, amount, city = transaction.split(",")
		d[name].append([time, amount, city])
		if int(amount) > 1000:
			res.add(transaction)

	for name, v in d.items():
		n = len(v)
		if n > 1:
			for i in range(n):
				for j in range(i + 1, n):
					if abs(int(v[i][0]) - int(v[j][0])) <= 60 and v[i][2] != v[j][2]:
						res.add(','.join([name] + v[i]))
						res.add(','.join([name] + v[j]))
	return res


