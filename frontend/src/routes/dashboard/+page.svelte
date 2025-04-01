<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	let user = null;

	async function fetchUser() {
		try {
			const response = await fetch('http://127.0.0.1:8000/api/v1/users/me', {
				method: 'GET',
				credentials: 'include'
			});

			if (!response.ok) {
				throw new Error('Failed to fetch user data');
			}

			user = await response.json();
			console.log(user);
		} catch (err) {
			goto('/login');
		}
	}

	onMount(() => {
		fetchUser();
	});
</script>

<div>Hello</div>
