<script lang="ts">
	import ExpensesForm from './ExpensesForm.svelte';
	import IncomesForm from './IncomesForm.svelte';

	export let onClose: () => void;

	let type: string = 'expense';
</script>

<div class="fixed inset-0 flex items-center justify-center">
	<div class="absolute inset-0 bg-emerald-500 bg-opacity-70 backdrop-blur-md"></div>

	<div
		class="lg:w-1/ relative z-10 mx-auto flex w-full max-w-2xl flex-col items-center rounded-lg bg-white p-10 shadow-lg sm:w-3/4"
	>
		<form class="flex w-full flex-col space-y-1">
			<select
				class="mb-6 block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
				name="type"
				id="type"
				bind:value={type}
			>
				<option value="expense">Expense</option>
				<option value="income">Income</option>
			</select>
			{#if type == 'expense'}
				<ExpensesForm {onClose} />
			{/if}
			{#if type == 'income'}
				<IncomesForm />
			{/if}
		</form>
	</div>
</div>
