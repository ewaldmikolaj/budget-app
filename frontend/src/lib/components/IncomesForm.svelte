<script lang="ts"></script>

<h3 class="font-bold text-emerald-600">Add new income</h3>
<label for="summary" class="block text-sm font-medium text-gray-700">Summary</label>
<input
	class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
	type="text"
	id="summary"
	name="summary"
	placeholder="Enter a brief description of the expense"
	required
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
/>
<label for="source" class="block text-sm font-medium text-gray-700">Source</label>
<input
	class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
	type="text"
	id="source"
	name="source"
	placeholder="Enter the source of the expense"
	required
/>
<button
	type="submit"
	class="mt-4 w-full bg-emerald-500 px-4 py-2 text-white hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-500"
>
	Add
</button>
