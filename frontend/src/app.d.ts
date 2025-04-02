// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
type User = {
	id: number;
	email: string;
	name: string;
	surname: string;
};

declare global {
	namespace App {
		interface Locals {
			user: User | null;
		}
	}
}

export {};
