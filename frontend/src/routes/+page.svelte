<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<main>
	{#if data.user}
		<p>Welcome, {data.user.name} {data.user.surname}</p>
	{/if}
</main>
