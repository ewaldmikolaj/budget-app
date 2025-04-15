<script lang="ts">
	import { onMount } from 'svelte';
	import { financialData, fetchFinancialData, isLoading } from '$lib/stores/financialData';

	export function refresh() {
		fetchFinancialData();
	}

	onMount(() => {
		fetchFinancialData();
	});
</script>

<div class="flex max-h-full flex-col gap-1 overflow-y-auto">
	{#if $isLoading}
		<div class="flex justify-center py-4">
			<p>Loading...</p>
		</div>
	{:else if $financialData.length > 0}
		{#each $financialData as item}
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
		<div class="py-4 text-center text-gray-500">
			<p>No transactions found.</p>
		</div>
	{/if}
</div>
