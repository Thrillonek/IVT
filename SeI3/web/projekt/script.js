let nav;
document.addEventListener('scroll', (e) => {
	if (!nav) nav = document.getElementsByTagName('nav')[0];
	nav.toggleAttribute('data-fixed', window.scrollY > 50);
});

const weekDays = document.getElementById('week-days');
const date = new Date();
[...weekDays.children].forEach((day, idx) => {
	day.toggleAttribute('data-active', date.getDay() == idx + 1);
});

function toggleNavbar() {
	const navbar = document.getElementsByTagName('nav')[0];
	navbar.toggleAttribute('data-visible');
}
