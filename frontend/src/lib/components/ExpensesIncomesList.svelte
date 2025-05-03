<script lang="ts">
	import { onMount } from 'svelte';
	import { financialData, fetchFinancialData, isLoading } from '$lib/stores/financialData';
	// @ts-ignore
	import feather from 'feather-icons';

	const thrashIcon = feather.icons.trash.toSvg({
		width: 20,
		height: 20
	});

	async function handleDelete(type: string, id: number) {
		try {
			const baseUrl = 'http://127.0.0.1:8000/api/v1';
			const url = type === 'income' ? `${baseUrl}/incomes/${id}` : `${baseUrl}/expenses/${id}`;
			const response = await fetch(url, {
				method: 'DELETE',
				credentials: 'include'
			});

			if (!response.ok) {
				throw new Error(`Failed to delete ${type}`);
			}
			refresh();
		} catch (error) {
			console.error(`Error deleting ${type}:`, error);
		}
	}

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
			<div
				class="group flex flex-row gap-2 overflow-hidden rounded-lg border border-dashed border-gray-300 hover:border-gray-600"
			>
				{#if item.type === 'income'}
					<div class="flex w-full flex-col">
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
					</div>
				{:else if item.type === 'expense'}
					<div class="flex w-full flex-col">
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
					</div>
				{/if}
				<button
					class="hidden items-center justify-center rounded-r-lg bg-red-600 px-5 text-white group-hover:flex"
					on:click={() => handleDelete(item.type, item.id)}
				>
					{@html thrashIcon}
				</button>
			</div>
		{/each}
	{:else}
		<div class="py-4 text-center text-gray-500">
			<p>No transactions found.</p>
		</div>
	{/if}
</div>
