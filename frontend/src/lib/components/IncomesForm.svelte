<script lang="ts">
	let summary: string = '';
	let amount: number = 0;
	let transactionDate: string = '';
	let source: string = '';

	export let onClose: () => void = () => {};

	async function handleSubmit() {
		try {
			const response = await fetch('http://127.0.0.1:8000/api/v1/incomes', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					accept: 'application/json'
				},
				body: JSON.stringify({
					summary: summary,
					amount: amount,
					transaction_date: transactionDate,
					source: source
				}),
				credentials: 'include'
			});

			if (!response.ok) {
				const errorData = await response.json();
				throw new Error(errorData.detail || 'Failed to add income');
			}

			onClose();
		} catch (err: any) {
			console.error(err);
		}
	}
</script>

<form autocomplete="off" on:submit|preventDefault={handleSubmit}>
	<h3 class="font-bold text-emerald-600">Add new income</h3>
	<label for="summary" class="block text-sm font-medium text-gray-700">Summary</label>
	<input
		class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
		type="text"
		id="summary"
		name="summary"
		placeholder="Enter a brief description of the expense"
		required
		bind:value={summary}
	/>
	<label for="amount" class="block text-sm font-medium text-gray-700">Amount</label>
	<input
		class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
		type="number"
		id="amount"
		name="amount"
		min="0.00"
		step="0.01"
		placeholder="Enter the amount spent"
		required
		bind:value={amount}
	/>
	<label for="transactionDate" class="block text-sm font-medium text-gray-700"
		>Transaction Date
	</label>
	<input
		class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
		type="date"
		id="transactionDate"
		name="transactionDate"
		placeholder="Select the transaction date"
		required
		bind:value={transactionDate}
	/>
	<label for="source" class="block text-sm font-medium text-gray-700">Source</label>
	<input
		class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
		type="text"
		id="source"
		name="source"
		placeholder="Enter the source of the expense"
		required
		bind:value={source}
	/>
	<div class="flex w-full flex-row space-x-3">
		<button
			type="submit"
			class="mt-4 w-full bg-emerald-500 px-4 py-2 text-white hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-500"
		>
			Add
		</button>
		<button
			type="button"
			class="mt-4 w-full bg-red-500 px-4 py-2 text-white hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-emerald-500"
			on:click={onClose}
		>
			Cancel
		</button>
	</div>
</form>
