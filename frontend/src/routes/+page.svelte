<script lang="ts">
	import type { PageData } from './$types';
	import ExpensesIncomesForm from '$lib/components/ExpensesIncomesForm.svelte';
	import ExpensesIncomesList from '$lib/components/ExpensesIncomesList.svelte';

	let showExpensesIncomesForm: boolean = false;
	let expensesIncomesList: ExpensesIncomesList;

	function toggleExpensesIncomesForm() {
		if (showExpensesIncomesForm && expensesIncomesList) {
			expensesIncomesList.refresh();
		}
		showExpensesIncomesForm = !showExpensesIncomesForm;
	}

	export let data: PageData;
</script>

<main
	class="fixed inset-0 flex items-center justify-center overflow-hidden bg-emerald-500 p-4 md:p-10"
>
	{#if showExpensesIncomesForm}
		<ExpensesIncomesForm onClose={toggleExpensesIncomesForm} />
	{/if}
	<div class="grid h-full w-full grid-cols-1 gap-4 overflow-hidden md:grid-cols-10">
		<div class="flex h-full flex-col overflow-hidden rounded-lg bg-white shadow md:col-span-4">
			<div class="flex-none border-b border-gray-200 p-4">
				<div class="flex flex-row items-center justify-between">
					<h2 class="text-xl font-bold">Expenses and Incomes</h2>
					<div>
						<button
							class="rounded bg-emerald-500 px-5 py-2 text-white hover:bg-emerald-600"
							on:click={toggleExpensesIncomesForm}
						>
							Add
						</button>
					</div>
				</div>
			</div>

			<div class="flex-1 overflow-hidden">
				<div class="h-full overflow-y-auto px-4 py-2">
					<ExpensesIncomesList bind:this={expensesIncomesList} />
				</div>
			</div>
		</div>

		<div class="h-full overflow-hidden rounded-lg bg-white shadow md:col-span-6"></div>
	</div>
</main>
