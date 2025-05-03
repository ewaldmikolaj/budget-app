<script>
	import { getContext } from 'svelte';

	const { data, xGet, yGet, xScale, yScale, width, height } = getContext('LayerCake');

	$: padding = $xScale.bandwidth() * 0.2;
	$: barWidth = $xScale.bandwidth() - padding * 2;
</script>

{#each $data as d, i}
	<g class="bar-group" transform="translate({$xGet(d)},{$yGet(d)})">
		<rect
			class={d.type === 'income' ? 'bar income' : 'bar expense'}
			x={padding}
			y={0}
			width={barWidth}
			height={$height - $yGet(d)}
		/>
		<text class="bar-label" x={$xScale.bandwidth() / 2} y={-5} text-anchor="middle">
			{d.amount}
		</text>
		<text
			class="bar-category"
			x={$xScale.bandwidth() / 2}
			y={$height - $yGet(d) + 15}
			text-anchor="middle"
		>
			{d.type === 'income' ? d.source : d.category || 'Other'}
		</text>
	</g>
{/each}

<style>
	.bar {
		fill-opacity: 0.7;
	}
	.bar.income {
		fill: #10b981; /* emerald-500 */
	}
	.bar.expense {
		fill: #ef4444; /* red-500 */
	}
	.bar:hover {
		fill-opacity: 1;
	}
	.bar-label {
		font-size: 12px;
		font-weight: bold;
		fill: #4b5563; /* gray-600 */
	}
	.bar-category {
		font-size: 10px;
		fill: #6b7280; /* gray-500 */
	}
</style>
