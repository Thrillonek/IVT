let nav;
document.addEventListener('scroll', (e) => {
	if (!nav) nav = document.getElementsByTagName('nav')[0];
	nav.toggleAttribute('data-active', window.scrollY > 50);
});

const weekDays = document.getElementById('week-days');
const date = new Date();
[...weekDays.children].forEach((day, idx) => {
	day.toggleAttribute('data-fixed', date.getDay() == idx + 1);
});
