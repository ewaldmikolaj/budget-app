<script lang="ts">
	import { onMount } from 'svelte';
	// @ts-ignore
	import feather from 'feather-icons';
	import CategoriesForm from './CategoriesForm.svelte';

	export let onClose: () => void = () => {};

	const plusIcon = feather.icons.plus.toSvg({
		width: 20,
		height: 20
	});

	let availableCategories: Array<{ id: string; name: string }> = [];
	let showCategoryForm = false;

	// Form Data
	let summary: string = '';
	let amount: number = 0;
	let transactionDate: string = '';
	let category: string = '';

	async function fetchCategories() {
		try {
			const response = await fetch('http://127.0.0.1:8000/api/v1/categories', {
				method: 'GET',
				credentials: 'include'
			});

			if (!response.ok) {
				throw new Error('Failed to fetch categories');
			}

			const data = await response.json();
			availableCategories = data.map((category: { id: string; name: string }) => ({
				id: category.id,
				name: category.name
			}));
		} catch (err: any) {
			console.error(err);
		}
	}

	async function handleSubmit() {
		try {
			const response = await fetch('http://127.0.0.1:8000/api/v1/expenses', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					accept: 'application/json'
				},
				body: JSON.stringify({
					summary: summary,
					amount: amount,
					transaction_date: transactionDate,
					category_id: category
				}),
				credentials: 'include'
			});

			if (!response.ok) {
				const errorData = await response.json();
				throw new Error(errorData.detail || 'Failed to add expense');
			}

			onClose();
		} catch (err: any) {
			console.error('Error submitting form:', err);
		}
	}

	function toggleCategoryForm() {
		showCategoryForm = !showCategoryForm;
	}

	onMount(() => {
		fetchCategories();
	});
</script>

<form autocomplete="off" on:submit|preventDefault={handleSubmit}>
	<h3 class="font-bold text-emerald-600">Add new expense</h3>
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
	<label for="transactionDate" class="block text-sm font-medium text-gray-700">
		Transaction Date
	</label>
	<input
		class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
		type="datetime-local"
		id="transactionDate"
		name="transactionDate"
		placeholder="Select the transaction date"
		required
		bind:value={transactionDate}
	/>
	<label for="category" class="block text-sm font-medium text-gray-700">Category</label>
	<div class="flex items-center space-x-2">
		<select
			class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
			name="category"
			id="category"
			bind:value={category}
		>
			<option value="" disabled selected>Select a category</option>
			{#each availableCategories as { id, name }}
				<option value={id}>{name}</option>
			{/each}
		</select>
		<button
			class="flex h-10 w-10 items-center justify-center rounded bg-emerald-500 p-2 text-white hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-500"
			type="button"
			on:click={toggleCategoryForm}
		>
			{@html plusIcon}
		</button>
	</div>
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
{#if showCategoryForm}
	<CategoriesForm onClose={toggleCategoryForm} />
{/if}
