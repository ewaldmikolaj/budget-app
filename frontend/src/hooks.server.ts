import cookie from 'cookie';
import { redirect, type Handle } from '@sveltejs/kit';

const privateRoutes = ['/'];
const publicRoutes = ['/login', '/register'];

export const handle: Handle = async ({ event, resolve }) => {
	const url = new URL(event.url);

	const token = cookie.parse(event.request.headers.get('cookie') || '');
	const userResponse = await fetch('http://127.0.0.1:8000/api/v1/users/me', {
		method: 'GET',
		headers: {
			Cookie: `access_token=${token.access_token}`
		}
	});

	if (!userResponse.ok && privateRoutes.includes(url.pathname)) {
		throw redirect(303, '/login');
	}

	if (userResponse.ok && publicRoutes.includes(url.pathname)) {
		throw redirect(303, '/');
	}

	if (userResponse.ok) {
		event.locals.user = await userResponse.json();
	}

	const response = await resolve(event);
	return response;
};
