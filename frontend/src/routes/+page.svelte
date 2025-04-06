<script lang="ts">
	import type { PageData } from './$types';
	import CategoriesForm from '$lib/components/CategoriesForm.svelte';
	import ExpensesIncomesForm from '$lib/components/ExpensesIncomesForm.svelte';

	let showCategoryForm: boolean = false;
	let showExpensesIncomesForm: boolean = true;

	function handleShowCategoryForm() {
		showCategoryForm = true;
	}

	function handleHideCategoryForm() {
		showCategoryForm = false;
	}

	function handleShowExpensesIncomesForm() {
		showExpensesIncomesForm = true;
	}

	function handleHideExpensesIncomesForm() {
		showExpensesIncomesForm = false;
	}

	export let data: PageData;
</script>

<main class="flex h-screen items-center justify-center bg-emerald-500 p-10">
	{#if showCategoryForm}
		<CategoriesForm onClose={handleHideCategoryForm} />
	{/if}
	{#if showExpensesIncomesForm}
		<ExpensesIncomesForm onClose={handleHideExpensesIncomesForm} />
	{/if}
	<div class="grid h-full w-full grid-cols-1 gap-4 md:grid-cols-10">
		<div class="rounded-lg bg-white p-4 shadow md:col-span-4">
			<div class="mb-2 flex flex-row items-center justify-between">
				<h2 class="text-xl font-bold">Expenses and Incomes</h2>
				<div>
					<button
						class="rounded bg-emerald-500 px-5 py-2 text-white hover:bg-emerald-600"
						on:click={handleShowExpensesIncomesForm}
					>
						Add
					</button>
				</div>
			</div>
			<div class="h-64 border border-dashed border-gray-300 p-4"></div>
		</div>

		<div class="rounded-lg bg-white p-4 shadow md:col-span-6"></div>
	</div>
</main>
