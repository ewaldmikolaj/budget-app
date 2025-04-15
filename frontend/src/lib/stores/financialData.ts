import { writable } from 'svelte/store';

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

export const financialData = writable<(Income | Expense)[]>([]);
export const isLoading = writable<boolean>(false);

export async function fetchFinancialData() {
	isLoading.set(true);
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

		financialData.set(flattenedData);
	} catch (error) {
		console.error('Error fetching financial data:', error);
	} finally {
		isLoading.set(false);
	}
}
