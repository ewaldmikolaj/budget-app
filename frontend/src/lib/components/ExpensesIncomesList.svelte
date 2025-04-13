<script lang="ts">
	import { onMount } from 'svelte';

	type Income = {
		id: number;
		summary: string;
		amount: number;
		transaction_date: string;
		source: string;
		type?: 'income';
	};

	type Expense = {
		id: number;
		summary: string;
		amount: number;
		transaction_date: string;
		category: string;
		type?: 'expense';
	};

	let incomesExpenses: (Income | Expense)[] = [];

	async function fetchIncomesExpenses() {
		const urls = ['http://127.0.0.1:8000/api/v1/incomes', 'http://127.0.0.1:8000/api/v1/expenses'];
		try {
			const responses = await Promise.all(
				urls.map((url) => fetch(url, { method: 'GET', credentials: 'include' }))
			);
			const data = await Promise.all(responses.map((response) => response.json()));

			const incomes = data[0].map((item: Income) => ({ ...item, type: 'income' }));
			const expenses = data[1].map((item: Expense) => ({ ...item, type: 'expense' }));

			const flattenedData = [...incomes, ...expenses].sort(
				(a, b) => new Date(b.transaction_date).getTime() - new Date(a.transaction_date).getTime()
			);
			incomesExpenses = flattenedData;
			console.log('Fetched data:', incomesExpenses);
		} catch (error) {
			console.error('Error fetching data:', error);
		}
	}

	export function refresh() {
		fetchIncomesExpenses();
	}

	onMount(() => {
		fetchIncomesExpenses();
	});
</script>

<div class="flex max-h-full flex-col gap-1 overflow-y-auto">
	{#if incomesExpenses.length > 0}
		{#each incomesExpenses as item}
			<div class="flex flex-col rounded-lg border border-dashed border-gray-300 p-2">
				{#if item.type === 'income'}
					<div class="flex flex-row items-center justify-between text-green-600">
						<h2 class="font-medium">{item.summary}</h2>
						<p>{item.amount} zł</p>
					</div>
					<div class="flex flex-row items-center justify-between text-sm text-gray-500">
						<p>{item.source}</p>
						<p>
							{new Date(item.transaction_date).toLocaleString('pl-PL', {
								day: '2-digit',
								month: '2-digit',
								year: 'numeric',
								hour: '2-digit',
								minute: '2-digit',
								second: '2-digit'
							})}
						</p>
					</div>
				{:else if item.type === 'expense'}
					<div class="flex flex-row items-center justify-between text-red-600">
						<h2 class="font-medium">{item.summary}</h2>
						<p>-{item.amount} zł</p>
					</div>
					<div class="flex flex-row items-center justify-between text-sm text-gray-500">
						<p>{item.category}</p>
						<p>
							{new Date(item.transaction_date).toLocaleString('pl-PL', {
								day: '2-digit',
								month: '2-digit',
								year: 'numeric',
								hour: '2-digit',
								minute: '2-digit',
								second: '2-digit'
							})}
						</p>
					</div>
				{/if}
			</div>
		{/each}
	{:else}
		<div><p></p></div>
	{/if}
</div>
