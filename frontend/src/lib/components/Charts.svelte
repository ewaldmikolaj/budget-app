<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import Chart from 'chart.js/auto';
	import { fetchFinancialData, financialData } from '$lib/stores/financialData';

	interface MonthlyData {
		monthKey: string;
		month: string;
		expenses: number;
		incomes: number;
	}

	let chartCanvas: HTMLCanvasElement;
	let chartInstance: Chart | undefined;

	let startDate: string;
	let endDate: string;
	let todayIsoString: string;

	onMount(() => {
		const today = new Date();
		todayIsoString = today.toISOString().split('T')[0];
		endDate = today.toISOString().split('T')[0];

		const sixMonthsAgo = new Date();
		sixMonthsAgo.setMonth(today.getMonth() - 6);
		startDate = sixMonthsAgo.toISOString().split('T')[0];
	});

	let expenses: number[] = [];
	let incomes: number[] = [];
	let months: string[] = [];

	$: {
		const monthlyData: Record<string, MonthlyData> = {};

		const filteredData = $financialData.filter((item: any) => {
			const transactionDate = new Date(item.transaction_date);
			const start = startDate ? new Date(startDate) : new Date(0);
			const end = endDate ? new Date(endDate) : new Date();

			end.setHours(23, 59, 59, 999);

			return transactionDate >= start && transactionDate <= end;
		});

		filteredData.forEach((item: any) => {
			const date = new Date(item.transaction_date);
			const monthKey = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}`;

			if (!monthlyData[monthKey]) {
				monthlyData[monthKey] = {
					monthKey,
					month: new Date(date.getFullYear(), date.getMonth(), 1).toLocaleDateString('en-US', {
						month: 'short',
						year: 'numeric'
					}),
					expenses: 0,
					incomes: 0
				};
			}

			if (item.type === 'expense') {
				monthlyData[monthKey].expenses += Number(item.amount);
			} else if (item.type === 'income') {
				monthlyData[monthKey].incomes += Number(item.amount);
			}
		});

		const sortedData: MonthlyData[] = Object.values(monthlyData).sort((a, b) => {
			return a.monthKey.localeCompare(b.monthKey);
		});

		months = sortedData.map((item) => item.month);
		expenses = sortedData.map((item) => item.expenses);
		incomes = sortedData.map((item) => item.incomes);
	}

	export function refresh(): void {
		fetchFinancialData();
	}

	onMount(async (): Promise<void> => {
		if ($financialData.length === 0) {
			await fetchFinancialData();
		}
		updateChart();
	});

	$: if ((months.length > 0 && chartCanvas) || (startDate && endDate)) {
		updateChart();
	}

	function updateChart(): void {
		if (chartInstance) {
			chartInstance.destroy();
		}

		if (!chartCanvas) return;

		const ctx = chartCanvas.getContext('2d');
		if (!ctx) return;

		chartInstance = new Chart(ctx, {
			type: 'bar',
			data: {
				labels: months,
				datasets: [
					{
						label: 'Expenses',
						data: expenses,
						backgroundColor: 'rgba(231, 0, 11, 0.5)',
						borderColor: 'rgba(231, 0, 11, 1)',
						borderWidth: 1
					},
					{
						label: 'Income',
						data: incomes,
						backgroundColor: 'rgba(0, 166, 62, 0.5)',
						borderColor: 'rgba(0, 166, 62, 1)',
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				scales: {
					y: {
						beginAtZero: true,
						title: {
							display: true,
							text: 'Amount'
						}
					},
					x: {
						title: {
							display: true,
							text: 'Month'
						}
					}
				}
			}
		});
	}

	onDestroy(() => {
		if (chartInstance) {
			chartInstance.destroy();
		}
	});
</script>

<div class="flex justify-center pt-5 sm:pt-10">
	<div class="mb-4 flex flex-col gap-4 sm:flex-row">
		<div class="flex-row items-center justify-between gap-2">
			<label for="start-date">Start Date</label>
			<input
				type="date"
				id="start-date"
				class="border border-gray-300 bg-gray-100 px-3 py-0.5 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
				bind:value={startDate}
				max={endDate}
			/>
		</div>
		<div class="flex-row items-center justify-between gap-2">
			<label for="end-date">End Date</label>
			<input
				type="date"
				id="end-date"
				class="border border-gray-300 bg-gray-100 px-3 py-0.5 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
				bind:value={endDate}
				min={startDate}
				max={todayIsoString}
			/>
		</div>
	</div>
</div>

<canvas bind:this={chartCanvas}></canvas>
