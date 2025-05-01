<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import Chart from 'chart.js/auto';
	import { fetchFinancialData, financialData } from '$lib/stores/financialData';

	// Define types for our data structures

	interface MonthlyData {
		monthKey: string;
		month: string;
		expenses: number;
		incomes: number;
	}

	let chartCanvas: HTMLCanvasElement;
	let chartInstance: Chart | undefined;

	let expenses: number[] = [];
	let incomes: number[] = [];
	let months: string[] = [];

	// Process financial data into monthly aggregates
	$: {
		// Map transactions to monthly data
		const monthlyData: Record<string, MonthlyData> = {};

		// Process all financial data
		$financialData.forEach((item: any) => {
			// Extract month from transaction date
			const date = new Date(item.transaction_date);
			const monthKey = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}`;

			// Initialize month entry if it doesn't exist
			if (!monthlyData[monthKey]) {
				monthlyData[monthKey] = {
					monthKey, // Keep the key for sorting
					month: new Date(date.getFullYear(), date.getMonth(), 1).toLocaleDateString('en-US', {
						month: 'short',
						year: 'numeric'
					}),
					expenses: 0,
					incomes: 0
				};
			}

			// Add amount to appropriate category
			if (item.type === 'expense') {
				monthlyData[monthKey].expenses += Number(item.amount);
			} else if (item.type === 'income') {
				monthlyData[monthKey].incomes += Number(item.amount);
			}
		});

		// Convert to array and sort by date
		const sortedData: MonthlyData[] = Object.values(monthlyData).sort((a, b) => {
			return a.monthKey.localeCompare(b.monthKey);
		});

		// Extract data for chart
		months = sortedData.map((item) => item.month);
		expenses = sortedData.map((item) => item.expenses);
		incomes = sortedData.map((item) => item.incomes);
	}

	// Add a refresh method
	export function refresh(): void {
		fetchFinancialData();
	}

	onMount(async (): Promise<void> => {
		if ($financialData.length === 0) {
			await fetchFinancialData();
		}
		updateChart();
	});

	// Update chart when data changes
	$: if (months.length > 0 && chartCanvas) {
		updateChart();
	}

	function updateChart(): void {
		if (chartInstance) {
			chartInstance.destroy();
		}

		chartInstance = new Chart(chartCanvas, {
			type: 'bar',
			data: {
				labels: months,
				datasets: [
					{
						label: 'Expenses',
						data: expenses,
						backgroundColor: 'rgba(255, 99, 132, 0.5)',
						borderColor: 'rgba(255, 99, 132, 1)',
						borderWidth: 1
					},
					{
						label: 'Incomes',
						data: incomes,
						backgroundColor: 'rgba(54, 162, 235, 0.5)',
						borderColor: 'rgba(54, 162, 235, 1)',
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				plugins: {
					legend: {
						position: 'top'
					}
				},
				scales: {
					x: {
						title: {
							display: true,
							text: 'Months'
						}
					},
					y: {
						title: {
							display: true,
							text: 'Amount'
						},
						beginAtZero: true
					}
				}
			}
		});
	}

	// Cleanup on component destroy
	onDestroy((): void => {
		if (chartInstance) {
			chartInstance.destroy();
		}
	});
</script>

<canvas bind:this={chartCanvas}></canvas>
