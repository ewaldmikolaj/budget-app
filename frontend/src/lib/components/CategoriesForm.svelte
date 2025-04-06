<script lang="ts">
	export let onClose: () => void;
</script>

<div class="fixed inset-0 flex items-center justify-center">
	<div class="absolute inset-0 bg-emerald-500 bg-opacity-70 backdrop-blur-md"></div>

	<div class="relative z-10 rounded-lg bg-white p-6 shadow-lg">
		<button class="absolute right-2 top-2 text-gray-500 hover:text-gray-700" on:click={onClose}>
			Close
		</button>

		<form class="flex flex-row gap-2">
			<input type="text" class="rounded border p-2" />
			<button
				type="submit"
				class="rounded bg-emerald-500 px-4 py-2 text-white hover:bg-emerald-600"
			>
				Add
			</button>
		</form>
	</div>
</div>
