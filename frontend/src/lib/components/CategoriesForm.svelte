<script lang="ts">
	import { onMount } from 'svelte';
	// @ts-ignore
	import feather from 'feather-icons';

	export let onClose: () => void;

	const thrashIcon = feather.icons.trash.toSvg({
		width: 20,
		height: 20
	});

	export let categories: { id: number; name: string }[] = [];
	let name: string = '';

	async function fetchCategories() {
		try {
			const response = await fetch('http://127.0.0.1:8000/api/v1/categories', {
				method: 'GET',
				credentials: 'include'
			});
			if (!response.ok) {
				throw new Error('Failed to fetch categories');
			}
			categories = await response.json();
		} catch (error) {
			console.error('Error fetching categories:', error);
		}
	}

	async function handleSubmit() {
		try {
			const response = await fetch('http://127.0.0.1:8000/api/v1/categories', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				credentials: 'include',
				body: JSON.stringify({ name: name })
			});

			if (!response.ok) {
				throw new Error('Failed to add category');
			}

			await fetchCategories();
		} catch (error) {
			console.error('Error adding category:', error);
		}
	}

	async function handleDelete(id: number) {
		try {
			const response = await fetch(`http://127.0.0.1:8000/api/v1/categories/${id}`, {
				method: 'DELETE',
				credentials: 'include'
			});

			if (!response.ok) {
				throw new Error('Failed to delete category');
			}

			await fetchCategories();
		} catch (error) {
			console.error('Error deleting category:', error);
		}
	}

	onMount(() => {
		fetchCategories();
	});
</script>

<div class="fixed inset-0 flex items-center justify-center">
	<div class="absolute inset-0 bg-opacity-90 backdrop-blur-lg"></div>

	<div
		class="relative z-10 mx-auto flex max-h-[40vh] w-full max-w-2xl flex-col items-center rounded-lg bg-white p-10 shadow-xl sm:w-3/4 lg:w-1/2"
	>
		<form
			class="mb-6 flex w-full flex-row gap-2"
			autocomplete="off"
			on:submit|preventDefault={handleSubmit}
		>
			<input
				type="text"
				class="block w-full flex-1 border border-gray-300 bg-gray-100 p-2 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
				bind:value={name}
			/>
			<button
				type="submit"
				class="flex-none rounded bg-emerald-500 px-4 py-2 text-white hover:bg-emerald-600"
			>
				Add
			</button>
			<button
				type="button"
				class="flex-none rounded bg-red-500 px-4 py-2 text-white hover:bg-red-600"
				on:click={onClose}
			>
				Close
			</button>
		</form>
		{#if categories.length > 0}
			<div class="flex max-h-[30vh] w-full flex-col gap-2 overflow-y-auto">
				<h3 class="font-bold text-emerald-600">Available categories</h3>
				{#each categories as item}
					<div
						class="flex flex-row items-center justify-between rounded-lg border border-dashed border-gray-300"
					>
						<p class="p-2 font-medium">{item.name}</p>
						<div class="rounded-e-lg bg-red-500 p-2 hover:bg-red-600">
							<button type="button" class="text-white" on:click={() => handleDelete(item.id)}>
								{@html thrashIcon}
							</button>
						</div>
					</div>
				{/each}
			</div>
		{/if}
	</div>
</div>
