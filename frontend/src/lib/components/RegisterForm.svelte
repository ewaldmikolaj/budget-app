<script lang="ts">
	import { goto } from '$app/navigation';

	let name: string = '';
	let surname: string = '';
	let email: string = '';
	let password: string = '';

	let error: string = '';

	async function handleRegister() {
		try {
			const registerResponse = await fetch('http://127.0.0.1:8000/api/v1/users', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					accept: 'application/json'
				},
				body: JSON.stringify({
					name: name,
					surname: surname,
					email: email,
					password: password
				})
			});

			if (!registerResponse.ok) {
				const errorData = await registerResponse.json();
				throw new Error(errorData.detail || 'Registration failed');
			}

			const loginResponse = await fetch('http://127.0.0.1:8000/api/v1/auth/token', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded',
					accept: 'application/json'
				},
				body: new URLSearchParams({
					grant_type: 'password',
					username: email,
					password: password
				}),
				credentials: 'include'
			});

			if (!loginResponse.ok) {
				const errorData = await loginResponse.json();
				throw new Error(errorData.detail || 'Login failed after registration');
			}

			goto('/dashboard');
		} catch (err: any) {
			if (err instanceof Error) {
				error = err.message;
			}
		}
	}
</script>

<div
	class="mx-auto flex w-full max-w-2xl flex-col items-center rounded-lg bg-white p-10 shadow-lg sm:w-3/4 lg:w-1/2"
>
	<div class="mb-4">
		<h1 class="text-3xl font-bold text-emerald-600">Registration</h1>
		<div></div>
	</div>
	<form
		class="flex w-full flex-col space-y-1"
		autocomplete="off"
		on:submit|preventDefault={handleRegister}
	>
		<input
			class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
			type="text"
			id="name"
			name="name"
			placeholder="Name"
			required
			bind:value={name}
		/>
		<input
			class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
			type="text"
			id="surname"
			name="surname"
			placeholder="Surname"
			required
			bind:value={surname}
		/>
		<input
			class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
			type="email"
			id="email"
			name="email"
			placeholder="Email"
			required
			bind:value={email}
		/>
		<input
			class="block w-full border border-gray-300 bg-gray-100 px-3 py-2 text-base text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-600"
			type="password"
			id="password"
			name="password"
			placeholder="Password"
			required
			bind:value={password}
		/>
		{#if error}
			<p class="text-sm text-red-500">{error}</p>
		{/if}
		<button
			type="submit"
			class="mt-4 w-full bg-emerald-500 px-4 py-2 text-white hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-500"
		>
			Register
		</button>
		<a class="text-emerald-600 underline" href="/login">Already have an account? Log in here.</a>
	</form>
</div>
